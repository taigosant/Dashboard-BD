#number of products: 548552
import pickle
import re
from models.Product import Product

# path = '/home/taigo/Documents/2018.2/BD/Dashboard-BD/data/amazon-meta.txt'
# path = '/home/taigo/Documents/2018.2/BD/Dashboard-BD/tokens.pkl'

#regexes
ASIN = r"ASIN: (.*)"
TITLE = r"title: (.*)"
GROUP = r"group: (\w*)"
SALESRANK = r"salesrank: (\d*)"


class Parser(object):
    def __init__(self):
        self.__mapProduct = {}

    def parse(self, path):
        with open(path, 'rb') as pFile:
            tokens = pickle.load(pFile)
            id = 0
            for token in tokens:
                asins = re.findall(ASIN, token, re.MULTILINE)
                titles = re.findall(TITLE, token, re.MULTILINE)
                groups = re.findall(GROUP, token, re.MULTILINE)
                salesranks = re.findall(SALESRANK, token, re.MULTILINE)

                print('ID:', id)
                print('ASIN:', asins)
                print('TITLE:', titles)
                print('GROUP:', groups)
                print('SALESRANK:', salesranks)

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
                    self.__mapProduct[id] = currentProduct
                    # print(currentProduct.toString())
                except Exception as e:
                    print(e)
                id += 1

    def getProductsMap(self):
        return self.__mapProduct



