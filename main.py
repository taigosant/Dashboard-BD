from models.Product import Product
from Parser import Parser
from ManagerDB import Manager
path = 'tokens.pkl'

if __name__ == '__main__':
    print('loading data...') #Todo talvez contabilizar tempo de loading e percentual, isso é só frescura pra caso não tenha mais nada pra fazer
    parser = Parser()
    parser.parse(path)
    mapProd = parser.getProductsMap()
    print('Products length: ', len(mapProd))
    # print(mapProd[693].toString())
    manager = Manager('bdzinho', 'dashboard', 'rorschach')
    manager.connect()
    if manager.isConnected():
        for key, value in mapProd.items():
            if value.save(manager):
                print('Sucess!')
                pass
            else:
                break


