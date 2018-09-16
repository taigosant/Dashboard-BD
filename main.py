from Parser import Parser
from ManagerDB import Manager
from Query import Query
import sys
import time

host = sys.argv[1]
user = sys.argv[2]
db_name = sys.argv[3]
password = sys.argv[4]
path = sys.argv[5]

if __name__ == '__main__':
    print(host, user, db_name, password, path)
    manager = Manager(host, user, db_name, password)
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
        manager.bulkInsertGroupList(parser.groupList)
        manager.bulkInsertCustomerList(parser.customerSet)
        manager.bulkInsertMap(parser.mapCategorioes)
        end = time.time()
        print("Finished! Elapsed time: ", (end-begin))




