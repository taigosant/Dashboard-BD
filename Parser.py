#number of products: 548552
import pickle
import re
from models.Product import Product
from models.Category import Category

# path = '/home/taigo/Documents/2018.2/BD/Dashboard-BD/data/amazon-meta.txt'
path = '/home/taigo/Documents/2018.2/BD/Dashboard-BD/tokens.pkl'

#regexes
ASIN = r"ASIN: (.*)"
TITLE = r"title: (.*)"
GROUP = r"group: (\w*)"
SALESRANK = r"salesrank: (\d*)"
CATEGORY_CHUNK = r"categories:((.|\n)*)reviews"
# CATEGORY_CHUNK = r"categories: \d+\n(\|(\w| | \W)*\[\d*\]|\n|)*s"


class Parser(object):
    def __init__(self):
        self.__mapProduct = {}
        self.__mapCategorioes = {}

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
                    currentCategory = Category(int(id), title)
                    categoryList.append(currentCategory)
                    self.__mapCategorioes[id] = currentCategory

                except Exception as e:
                    print(e)
        return categoryList



    def parse(self, path):
        with open(path, 'rb') as pFile:
            tokens = pickle.load(pFile)
            id = 0
            for token in tokens:
                # print(token)
                asins = re.findall(ASIN, token, re.MULTILINE)
                titles = re.findall(TITLE, token, re.MULTILINE)
                groups = re.findall(GROUP, token, re.MULTILINE)
                salesranks = re.findall(SALESRANK, token, re.MULTILINE)
                categoryChunk = re.findall(CATEGORY_CHUNK, token, re.MULTILINE)
                productCategories = []
                if len(categoryChunk) > 0:
                    try:
                        text = categoryChunk[0][0]  # categoryChuncategoryChunkk eh uma lista de tuplas, a primeira posição da tupla corresponde ao texto
                        text = text.replace("\n", "")
                        categories = text.split("|")
                        productCategories = self.__extractCategories(categories)
                    except Exception as e:
                        print(e, '\n', text)


                print('ID:', id)
                print('ASIN:', asins)
                print('TITLE:', titles)
                print('GROUP:', groups)
                print('SALESRANK:', salesranks)
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

                    currentProduct = Product(id, asin, title, salesrank, group)
                    currentProduct.setCategoryList(productCategories)
                    print(productCategories)
                    self.__mapProduct[id] = currentProduct
                    # print(currentProduct.toString())
                except Exception as e:
                    print(e)
                id += 1

    def getProductsMap(self):
        return self.__mapProduct

    def getCategoriesMap(self):
        return self.__mapCategorioes


if __name__ == '__main__':
    p = Parser()
    try:
        p.parse(path)
        print("Number of products: ", len(p.getProductsMap()))
        print("Number of categories: ", len(p.getCategoriesMap()))

        for key, value in p.getCategoriesMap().items():
            print(value.toString())
    except Exception as e:
        print(e)




