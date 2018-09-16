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

        result = mg.executeSelectStmt(Query.A_QUERY.format(asin="B00004YNH2", asin1="B00004YNH2"))
        print(result, '\n')
        result1 = mg.executeSelectStmt(Query.B_QUERY.format(ASIN="B00004YNH2"))
        print(result1, '\n')

        result2 = mg.executeSelectStmt(Query.C_QUERY.format(asin="B00004YNH2"))
        print(result2, '\n')

        result3 = mg.executeSelectStmt(Query.D_QUERY)
        print(result3, '\n')

        result4 = mg.executeSelectStmt(Query.E_QUERY)
        print(result4, '\n')

        result5 = mg.executeSelectStmt(Query.F_QUERY)
        print(result5, '\n')

        result6 = mg.executeSelectStmt(Query.G_QUERY)
        print(result6, '\n')



