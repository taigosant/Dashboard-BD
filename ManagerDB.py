import psycopg2 as pg

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



