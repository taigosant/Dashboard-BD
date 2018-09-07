#number of products: 548552
import pickle
import re
from models.Product import Product
from models.Category import Category
from models.Review import Review
path = 'tokens.pkl'

#regexes
ASIN = r"ASIN: (.*)"
TITLE = r"title: (.*)"
SIMILAR = r"similar: (.*)"
GROUP = r"group: (\w*)"
SALESRANK = r"salesrank: (\d*)"
CATEGORY_CHUNK = r"categories:((.|\n)*)reviews"


class Parser(object):
    def __init__(self, manager=None):
        self.__percents = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
        self.__mapProduct = {}
        self.__mapCategorioes = {}
        self.__groupList = []
        self.__customerSet = set()
        self.__manager = manager

    def __extractCategories(self, stringList):
        categoryList = []

        for string in stringList:
            if '[' in string and ']' in string:
                try:
                    # print(string)
                    idInitPos = string.find('[')
                    # print(idInitPos)
                    idEndPos = string.find(']')
                    # print(idEndPos)
                    id = string[idInitPos+1:idEndPos]
                    title = string[0: idInitPos]

                    if str(id).isnumeric():
                        currentCategory = Category(int(id), title)
                        categoryList.append(currentCategory)
                        self.__mapCategorioes[id] = currentCategory

                    else: # tratando um caso chato em que a string vem assim "title [guitar][213213]"
                        string = string.replace("[", "(", 1)
                        string = string.replace("]", ")", 1)
                        idInitPos = string.find('[')
                        idEndPos = string.find(']')
                        id = string[idInitPos + 1:idEndPos]
                        title = string[0: idInitPos]

                        if str(id).isnumeric():
                            currentCategory = Category(int(id), title)
                            categoryList.append(currentCategory)
                            self.__mapCategorioes[id] = currentCategory
                        else:
                            print("inconsistent category: ", string)

                except Exception as e:
                    print(e)

        return categoryList

    def __extractReview(self, stringList, prod_id, cursor):
        helpful = -1
        costumer = -1
        date = -1
        rating = -1
        votes = -1
        aux = -1

        if len(stringList) > 1 :
            stringList = stringList[1:]
            
        for string in stringList:
            date = string.find("cutomer:")
            if (date != -1):
                date = string[4:date-1]

            costumer = string.find("cutomer:")
            aux = string.find("rating:")

            if(costumer!=-1):
                costumer = string[costumer+9:aux]

            rating = string.find("rating:")
            aux = string.find("votes:")

            if rating!=-1:
                rating = string[rating+8:aux]

            votes = string.find("votes:")
            aux = string.find("helpful:")

            if(votes!=-1):
                votes = string[votes+6:aux]

            aux = string.find("helpful:")

            if aux!=-1:
                helpful = string[aux+8:len(string)]


            if costumer != -1:
                self.__customerSet.add(costumer)

                r = Review(date, votes, rating, helpful, prod_id, costumer)
                if r.executeInsertStatement(cursor):
                    pass
                else:
                    print("error inserting:\n", r.toString())
                    print(string)
                    break

        # print("Sucess!")

    def __printCompletePercent(self, id):
        if id > 0:
            percent = (id * 100) / 548552
            if int(percent) in self.__percents:
                print(int(percent), "% loaded and inserted...")
                self.__percents = self.__percents[1:]
                self.__manager.getConnector().commit()

    def parse(self, path):
        cursor = self.__manager.getConnector().cursor()
        pFile = open(path, 'rb')
        tokens = pickle.load(pFile)
        pFile.close()
        id = 0
        for token in tokens:

            #print(token)
            self.__printCompletePercent(id)
            asins = re.findall(ASIN, token, re.MULTILINE)
            titles = re.findall(TITLE, token, re.MULTILINE)
            similars = re.findall(SIMILAR, token, re.MULTILINE)
            groups = re.findall(GROUP, token, re.MULTILINE)
            salesranks = re.findall(SALESRANK, token, re.MULTILINE)
            categoryChunk = re.findall(CATEGORY_CHUNK, token, re.MULTILINE)
            productCategories = []

            reviewChunk =  token.split("reviews:")
            if (len(reviewChunk)>1):
                try:
                    review =  reviewChunk[1].split("\n")
                    #print("REVIEW ",(review))
                    self.__extractReview(review, id, cursor)
                except Exception as e:
                    print(e, '\n', review)

            categories = []
            if len(categoryChunk) > 0:
                try:
                    text = categoryChunk[0][0]  # categoryChuncategoryChunkk eh uma lista de tuplas, a primeira posição da tupla corresponde ao texto
                    text = text.replace("\n", "")
                    categories = text.split("|")
                    productCategories = self.__extractCategories(categories)
                except Exception as e:
                    print(e, '\n', text)

            # print('ID:', id)
            # print('ASIN:', asins)
            # print('TITLE:', titles)
            # print('SIMILAR:', similars)
            # print('GROUP:', groups)
            # print('SALESRANK:', salesranks)
            # print('CATEGORY_CHUNK:', categories)

            try:
                title = "empty"
                asin = "empty"
                group = "empty"
                salesrank = 0

                if len(titles) > 0:
                    title = titles[0]
                    title = title.replace("'", "")
                if len(groups) > 0:
                    group = groups[0]
                if len(salesranks) > 0:
                    salesrank = salesranks[0]
                if len(asins) > 0:
                    asin = asins[0]
                idGroup = -1

                if group not in self.__groupList:
                    self.__groupList.append(group)
                    idGroup = len(self.__groupList) -1
                else:
                    idGroup = self.__groupList.index(group)

                similarList = []  # similares
                if len(similars) > 0:
                    match = similars[0]
                    match = match.split()
                    if len(match) > 1:
                        similarList = match[1:]

                currentProduct = Product(id, asin, title, salesrank, idGroup, similarList)
                currentProduct.setCategoryList(productCategories)
                # print(productCategories)
                # self.__mapProduct[id] = currentProduct
                if currentProduct.executeInsertStatement(cursor):
                    pass
                else:
                    print("error inserting product: ", id)
                    return
                # print(currentProduct.toString())
            except Exception as e:
                print(e)
            id += 1

        cursor.close()
        self.__manager.getConnector().commit()


    def getCategoriesMap(self):
        return self.__mapCategorioes

    def getGroupsList(self):
        return self.__groupList

    # def getReviewList(self):
    #     return self.__reviewList

    def getCostumerSet(self):
        return self.__customerSet

# if __name__ == '__main__':
#     p = Parser()
#     try:
#         p.parse(path)
#         with open('productsMap.pkl', 'wb') as pico:
#             pickle.dump(p.getProductsMap(), pico)
#
#         with open('categoryMap.pkl', 'wb') as pico1:
#             pickle.dump(p.getCategoriesMap(), pico1)
#
#         with open('reviewMap.pkl', 'wb') as pico2:
#             pickle.dump(p.getReviewMap(), pico2)
#
#         with open('groupList.pkl', 'wb') as pico3:
#             pickle.dump(p.getGroupsList(), pico3)
#
#         # print("Number of products: ", len(p.getProductsMap()))
#         # print("Number of categories: ", len(p.getCategoriesMap()))
#         #
#         # for key, value in p.getCategoriesMap().items():
#         #     print(value.toString())
#     except Exception as e:
#         print(e)




