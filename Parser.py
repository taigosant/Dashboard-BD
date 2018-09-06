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
GROUP = r"group: (\w*)"
SALESRANK = r"salesrank: (\d*)"
CATEGORY_CHUNK = r"categories:((.|\n)*)reviews"


class Parser(object):
    def __init__(self):
        self.__mapProduct = {}
        self.__mapCategorioes = {}
        self.__mapReview = {}

    def __extractCategories(self, stringList):
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

                    self.__mapCategorioes[id] = currentCategory

                except Exception as e:
                    print(e)
    def __extractReview(self,stringList,id):
        helpful = None
        costumer = None
        date = None
        rating = None
        votes = None
        aux = None
        if(len(stringList) > 1 ):
            stringList = stringList[1:]
            
        for string in stringList:
            
            print(string)
            
            date = string.find("cutomer")
            if (date != -1):
                date = string[4:date-1]
                
            costumer = string.find("cutomer: ")
            aux =  string.find("  rating:")
            if(costumer!=-1):
                costumer =  string[costumer+9:aux]
            rating = string.find("rating: ")   
            aux = string.find("  votes")
            if(rating!=-1):
                rating = string[rating+8:aux]
            votes   = string.find("votes:   ") 
            aux = string.find("  helpful")
            if(votes!=-1):
                votes =  string[votes+9:aux]
            aux =  string.find("helpful:   ") 
            if(aux!=-1):
                helpful =  string[aux+11:len(string)]
            r = Review(date,votes,rating,helpful,id,costumer)
            print(r.toString())
            self.__mapReview[id] = r
            
                
                
                
                
             
            
                   

    def parse(self, path):
        with open(path, 'rb') as pFile:
            tokens = pickle.load(pFile)
            id = 0
            for token in tokens:
                #print(token)
                asins = re.findall(ASIN, token, re.MULTILINE)
                titles = re.findall(TITLE, token, re.MULTILINE)
                groups = re.findall(GROUP, token, re.MULTILINE)
                salesranks = re.findall(SALESRANK, token, re.MULTILINE)
                categoryChunk = re.findall(CATEGORY_CHUNK, token, re.MULTILINE)
                
                reviewChunk =  token.split("reviews:")
                if (len(reviewChunk)>1):
                    try:
                        review =  reviewChunk[1].split("\n")                
                        #print("REVIEW ",(review))
                        self.__extractReview(review,id)
                    except Exception as e:
                        print(e, '\n', review)    
                     
                categories = []
                if len(categoryChunk) > 0:
                    try:
                        text = categoryChunk[0][0]  # categoryChuncategoryChunkk eh uma lista de tuplas, a primeira posição da tupla corresponde ao texto
                        text = text.replace("\n", "")
                        categories = text.split("|")
                        self.__extractCategories(categories)
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




