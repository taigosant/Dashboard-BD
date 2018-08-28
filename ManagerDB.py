import psycopg2 as pg
import time

class Manager(object):

    def __init__(self, user, dbName, password):
        self.__config = {
            'user': user,
            'dbname': dbName,
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

    def bunkInsert(self, mapObj):
        try:
            startTime = time.time()
            conn = self.__conn
            cursor = conn.cursor()
            for key, value in mapObj.items():
                try:
                    value.executeStatement(cursor)
                    print('Sucess!')
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



