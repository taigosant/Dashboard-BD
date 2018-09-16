#number of products: 548552
import pickle
import re
from models.Product import Product
from models.Category import Category
from models.Review import Review
from models.CategoryByProduct import CategoryByProduct
path = "/home/taigo/Documents/2018.2/BD/Dashboard-BD/data/amazon-meta.txt"

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
        self.mapCategorioes = {}
        self.groupList = []
        self.customerSet = set()  # consjunto de costumers para evitar identificadores repetidos
        self.__manager = manager
        self.bulkStrProd = "INSERT INTO product (id_product, asin, salesrank, title, groupid) VALUES "
        self.bulkStrSimilar = "INSERT INTO similarbyproduct (ASIN_PRODUCT, ASIN_ProductSIMILAR) VALUES "
        self.bulkStrCatByProd = "INSERT INTO categoriesbyproduct (id_prod, id_cat) VALUES "
        self.bulkStrReview = "INSERT INTO review (r_date, votes, rating, helpful, prod_id, ID_Costumer) VALUES "
        self.bulkStrProdList = []
        self.bulkStrSimilarList = []
        self.bulkStrCatByProdList = []
        self.bulkStrReviewList = []

    def __extractCategories(self, stringList, cursor, prodId):
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
                        currentCategoryByProd = CategoryByProduct(int(id), prodId)
                        categoryList.append(currentCategoryByProd.getValuesString())

                        # if currentCategoryByProd.executeInsertStatement(cursor):
                        #     pass
                        # else:
                        #     print("insertion failed:", currentCategoryByProd.toString())
                        # categoryList.append(currentCategory)

                        self.mapCategorioes[id] = currentCategory

                    else: # tratando um caso chato em que a string vem assim "title [guitar][213213]"
                        string = string.replace("[", "(", 1)
                        string = string.replace("]", ")", 1)
                        idInitPos = string.find('[')
                        idEndPos = string.find(']')
                        id = string[idInitPos + 1:idEndPos]
                        title = string[0: idInitPos]

                        if str(id).isnumeric():
                            currentCategory = Category(int(id), title)
                            currentCategoryByProd = CategoryByProduct(int(id), prodId)
                            categoryList.append(currentCategoryByProd.getValuesString())

                            # if currentCategoryByProd.executeInsertStatement(cursor):
                            #     pass
                            # else:
                            #     print("insertion failed:", currentCategoryByProd.toString())
                            # categoryList.append(currentCategory)

                            self.mapCategorioes[id] = currentCategory
                        else:
                            print("inconsistent category: ", string)

                except Exception as e:
                    print(e)

        return ",".join(categoryList)

    def __extractReview(self, stringList, prod_id, cursor):  # extrai os dados de uma review
        helpful = -1
        costumer = -1
        date = -1
        rating = -1
        votes = -1
        aux = -1

        reviewList = []

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
                costumer = str(costumer).strip()
                self.customerSet.add(costumer)

                r = Review(date, votes, rating, helpful, prod_id, costumer)
                reviewList.append(r.getValuesString())
                # if r.executeInsertStatement(cursor):
                #     pass
                # else:
                #     print("error inserting:\n", r.toString())
                #     print(string)
                #     break

        return ",".join(reviewList)  # retorna a string para o bulk insert

        # print("Sucess!")

    def __printCompletePercent(self, id, cursor):

        percent = (id * 100) / 548551
        if int(percent) in self.__percents:
            print(int(percent), "% loaded and inserted...")
            self.__percents = self.__percents[1:]

            if len(self.bulkStrProdList) > 0:
                try:
                    values = ",".join(self.bulkStrProdList)
                    cursor.execute(str(self.bulkStrProd + values))
                except Exception as ex:
                    print(ex)
                    return False

            if len(self.bulkStrSimilarList) > 0:
                try:
                    values = ",".join(self.bulkStrSimilarList)
                    cursor.execute(self.bulkStrSimilar + values)
                except Exception as ex:
                    print(ex)
                    return False

            if len(self.bulkStrCatByProdList) > 0:
                try:
                    values = ",".join(self.bulkStrCatByProdList)
                    cursor.execute(self.bulkStrCatByProd + values)
                except Exception as ex:
                    print(ex)
                    return False

            if len(self.bulkStrReviewList) > 0:
                try:
                    values = ",".join(self.bulkStrReviewList)
                    cursor.execute(self.bulkStrReview + values)
                except Exception as ex:
                    print(ex)
                    return False

            self.__manager.getConnector().commit()

            self.bulkStrProdList = []
            self.bulkStrSimilarList = []
            self.bulkStrCatByProdList = []
            self.bulkStrReviewList = []
            return True
        else:
            pass

        return True

    def parse(self, path):
        cursor = self.__manager.getConnector().cursor()

        with open(path) as file:
            data = file.read()
            tokens = data.split('\n\n')
            tokens = tokens[:-1]
            id = 0
            for token in tokens:

                # print(token)
                asins = re.findall(ASIN, token, re.MULTILINE)
                titles = re.findall(TITLE, token, re.MULTILINE)
                similars = re.findall(SIMILAR, token, re.MULTILINE)
                groups = re.findall(GROUP, token, re.MULTILINE)
                salesranks = re.findall(SALESRANK, token, re.MULTILINE)
                categoryChunk = re.findall(CATEGORY_CHUNK, token, re.MULTILINE)
                # productCategories = []

                reviewChunk = token.split("reviews:")
                if len(reviewChunk) > 1:
                    try:
                        review = reviewChunk[1].split("\n")
                        reviewStr = self.__extractReview(review, id, cursor)
                        if len(reviewStr) > 0:
                            self.bulkStrReviewList.append(reviewStr)
                    except Exception as e:
                        print(e, '\n', review)

                categories = []

                if len(categoryChunk) > 0:
                    try:
                        text = categoryChunk[0][0]  # categoryChuncategoryChunkk eh uma lista de tuplas, a primeira posição da tupla corresponde ao texto
                        text = text.replace("\n", "")
                        categories = text.split("|")
                        catByProdStr = self.__extractCategories(categories, cursor, id)
                        if len(catByProdStr) > 0:
                            self.bulkStrCatByProdList.append(catByProdStr)
                    except Exception as e:
                        print(e, '\n', text)

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

                    if group not in self.groupList:
                        self.groupList.append(group)
                        idGroup = len(self.groupList) - 1
                    else:
                        idGroup = self.groupList.index(group)

                    similarList = []  # similares
                    if len(similars) > 0:
                        match = similars[0]
                        match = match.split()
                        if len(match) > 1:
                            similarList = match[1:]

                    currentProduct = Product(id, asin, title, salesrank, idGroup, similarList)

                    self.bulkStrProdList.append(currentProduct.getValuesString())
                    similarStr = currentProduct.getSimilarValueString()
                    if len(similarStr) > 0:
                        self.bulkStrSimilarList.append(similarStr)

                    # if currentProduct.executeInsertStatement(cursor):
                    #     pass
                    # else:
                    #     print("error inserting product: ", id)
                    #     return
                    # print(currentProduct.toString())
                    if not self.__printCompletePercent(id, cursor):
                        break

                except Exception as e:
                    print(e)
                id += 1

    def getCategoriesMap(self):
        return self.mapCategorioes

    def getGroupsList(self):
        return self.groupList

    def getCostumerSet(self):
        return self.customerSet


if __name__ == '__main__':
    p = Parser()
    try:
        with open(path) as file:
            data = file.read()
            tokens = data.split("\n\n")
            tokens = tokens[:-1]
            print(tokens[-1])

    except Exception as e:
        print(e)




