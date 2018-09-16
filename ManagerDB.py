import psycopg2 as pg
import time


class Manager(object):

    def __init__(self, host, user, dbName, password):
        self.__config = {
            'host': host,
            'user': user,
            'database': dbName,
            'password': password
        }
        self.__conn = None

    def connect(self):
        try:
            self.__conn = pg.connect(**self.__config)
            print('Sucessifuly connected to the database!')
        except Exception as e:
            print('Unable to connect to the database :/', e)

    def getConnector(self):
        return self.__conn

    def isConnected(self):
        if self.__conn is not None:
            return True
        else:
            return False

    def executeArbitraryStatement(self, statement):
        try:
            cursor = self.__conn.cursor()
            cursor.execute(statement)
            cursor.close()
            self.__conn.commit()
            print("Sucess!")
        except Exception as e:
            print(e)

    def executeSelectStmt(self, statement):
        try:
            cursor = self.__conn.cursor()
            cursor.execute(statement)
            result = cursor.fetchall()
            cursor.close()
            print("Success!")
            return result
        except Exception as e:
            print(e)

        return

    def bulkInsertGroupList(self, list):
        id = 0
        statement = "INSERT INTO groupproducts (id_group, title) VALUES ({idGroup}, '{groupTitle}')"
        conn = self.__conn
        cursor = conn.cursor()
        for group in list:
            toExec = statement.format(idGroup=id, groupTitle=group)
            try:
                print('executing statement: ', toExec)
                cursor.execute(toExec)
                id += 1
                print('Sucess!')
            except Exception as e:
                print(e)
                break
        cursor.close()
        conn.commit()

    def bulkInsertCustomerList(self, list):
        statement = "INSERT INTO costumer (id_costumer) VALUES ('{costumer}');"
        conn = self.__conn
        cursor = conn.cursor()
        for customer in list:
            toExec = statement.format(costumer=customer)
            try:
                print('executing statement: ', toExec)
                cursor.execute(toExec)
                print('Sucess!')
            except Exception as e:
                print(e)
                break
        cursor.close()
        conn.commit()

    def bulkInsertList(self, list):
        try:
            startTime = time.time()
            conn = self.__conn
            cursor = conn.cursor()
            for value in list:
                try:
                    bool = value.executeInsertStatement(cursor)
                    if bool:
                        print('Sucess!')
                    else:
                        print('statement execution failed!')
                        break
                except Exception as e:
                    print(e)
                    break

            cursor.close()
            conn.commit()
            endTime = time.time()
            timeElapsed = endTime - startTime
            print("{quantity} objects inserted! elapsed time: {time}".format(
                                                                             quantity=len(list),
                                                                             time=timeElapsed
            ))
        except Exception as e:
            print(e)

    def bulkInsertMap(self, mapObj):
        try:
            startTime = time.time()
            conn = self.__conn
            cursor = conn.cursor()
            for key, value in mapObj.items():
                try:
                    bool = value.executeInsertStatement(cursor)
                    if bool:
                        print('Sucess!')
                    else:
                        print('statement execution failed!')
                        break
                except Exception as e:
                    print(e)
                    break

            cursor.close()
            conn.commit()
            endTime = time.time()
            timeElapsed = endTime - startTime
            print("{quantity} objects inserted! elapsed time: {time}".format(
                                                                             quantity=len(mapObj),
                                                                             time=timeElapsed
            ))
        except Exception as e:
            print(e)



