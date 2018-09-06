
class Category(object):
    def __init__(self, categoryId, title):
        self.__categoryId = categoryId
        self.__title = title.replace("'", "")

    def toString(self):
        stringToReturn  = "CategoryID = " + str(self.__categoryId) + "\n"
        stringToReturn += " Title = " + self.__title + "\n"
        return stringToReturn

    def getId(self):
        return self.__categoryId

    def getTitle(self):
        return self.__title

    def executeInsertStatement(self, cursor):
        try:
            statement = "INSERT INTO category (id_category, title)" \
                        " VALUES ({id},'{title}');".format(
                                                            id=self.__categoryId,
                                                            title=self.__title
                                                            )
            print('executing statement: ', statement)
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