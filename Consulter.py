from ManagerDB import Manager
from Query import Query
import sys

host = sys.argv[1]
user = sys.argv[2]
db_name = sys.argv[3]
password = sys.argv[4]

if __name__ == '__main__':
    mg = Manager(host, user, db_name, password)
    mg.connect()
    if mg.isConnected():
        result = mg.executeSelectStmt(Query.B_QUERY.format(ASIN="B00004YNH2"))
        result1 = mg.executeSelectStmt(Query.E_QUERY)
        print(result, '\n')
        print(result1, '\n')

        for tuple in result1:
            print('title', tuple[0])
            print('avg rating', tuple[1])
            print('avg helpful', tuple[2])



