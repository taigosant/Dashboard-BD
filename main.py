from models.Product import Product
from models.Review import Review
from Parser import Parser
from ManagerDB import Manager
path = 'tokens.pkl'

if __name__ == '__main__':
    p =  Review(10, "20-10-2008", 3, 4, 10,15,"4834")
    print(p.toString())
    # print('loading data...') #Todo talvez contabilizar tempo de loading e percentual, isso é só frescura pra caso não tenha mais nada pra fazer
    # parser = Parser()
    # parser.parse(path)
    # mapProd = parser.getProductsMap()
    # print('Products length: ', len(mapProd))
    # # print(mapProd[693].toString())
    # manager = Manager('bdzinho', 'dashboard', 'rorschach')
    # manager.connect()
    # if manager.isConnected():
    #     manager.bunkInsert(mapProd)



