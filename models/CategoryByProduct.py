
class CategoryByProduct(object):

    def __init__(self, categoryId, productId):
        self.__categoryId = categoryId
        self.__productId = productId

    def toString(self):
        stringToReturn = "CategoryID = " + str(self.__categoryId) + "\n"
        stringToReturn += "ProductId = " + str(self.__productId) + "\n"
        return stringToReturn

    def executeInsertStatement(self, cursor):
        try:
            statement = "INSERT INTO categoriesbyproduct (id_prod, id_cat)" \
                        " VALUES ({idP},{idC});".format(
                                                            idP=self.__productId,
                                                            idC=self.__categoryId
                                                            )
            # print('executing statement: ', statement)
            cursor.execute(statement)
            return True
        except Exception as e:
            print(e)
            return False

    def save(self, manager, func):
        try:
            conn = manager.getConnector()
            cursor = conn.cursor()
            func(cursor)
            cursor.close()
            conn.commit()
            return True
        except Exception as e:
            print(e)
            return False
