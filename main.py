from models.Product import Product
from models.Review import Review
from Parser import Parser
from ManagerDB import Manager
from Query import Query
import time
import pickle
path = 'tokens.pkl'

if __name__ == '__main__':
    manager = Manager('bdzinho', 'dashboard', 'rorschach')
    manager.connect()
    if manager.isConnected():
        print("creating database...")
        manager.executeArbitraryStatement(Query.CREATE_DATABASE_SCHEMA)
        begin = time.time()
        print('loading data...') #Todo talvez contabilizar tempo de loading e percentual, isso é só frescura pra caso não tenha mais nada pra fazer
        parser = Parser(manager)
        parser.parse(path)
        print("costumers quantity: ", len(parser.getCostumerSet()))
        print("548552 products inserted...\n\ninserting groups, categories and costumers now.... ")
        # print('Products length: ', len(mapProd))
        # print(mapProd[693].toString())
        manager.bulkInsertGroupList(parser.getGroupsList())
        manager.bulkInsertCustomerList(parser.getCostumerSet())
        manager.bulkInsertMap(parser.getCategoriesMap())
        end = time.time()
        print("Finished! Elapsed time: ", (end-begin))




