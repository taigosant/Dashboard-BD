from models.CategoryByProduct import CategoryByProduct


class Product(object):

    def __init__(self, productId, assin, title, salesrank, groupId, similarList):
        self.__categoryList = []
        self.__productId = productId
        self.__assin = assin
        self.__title = title
        self.__salesrank = salesrank
        self.__groupId = groupId
        self.__similarList = similarList

        if str(self.__salesrank).isnumeric():
            pass
        else:
            self.__salesrank = 0

    def toString(self):
        out = "Title: {title}\n" \
              "ASIN: {assin}\n" \
              "SalesRank: {salesrank}\n" \
              "".format(
                        title=self.__title,
                        assin=self.__assin,
                        salesrank=self.__salesrank
                        )
        return out

    def setCategoryList(self, categoryList):
        self.__categoryList = categoryList

    def __insertSimilars(self,cursor):
        statement = "INSERT INTO similarbyproduct (ASIN_PRODUCT, ASIN_ProductSIMILAR) VALUES ('{asin_prod}','{asin_sim}');"
        for similar in self.__similarList:
            try:
                toExec = statement.format(asin_prod=self.__assin, asin_sim=similar)
                cursor.execute(toExec)
            except Exception as e:
                print(e, similar)
                break


    def __insertCategoryListOnDB(self, cursor):
        for obj in self.__categoryList:
            currentCatProd = CategoryByProduct(obj.getId(), self.__productId)
            if currentCatProd.executeInsertStatement(cursor):
                pass
            else:
                break

    def executeInsertStatement(self, cursor): #Todo "ExecuteInsertStatement"
        try:
            statement = "INSERT INTO product (id_product, asin, salesrank, title, groupid)" \
                        " VALUES ({id},'{asin}',{salesrank},'{title}', {g_id});".format(
                                                                                id=self.__productId,
                                                                                asin=self.__assin,
                                                                                salesrank=self.__salesrank,
                                                                                title=self.__title,
                                                                                g_id=self.__groupId
                                                                            )
            # print('executing statement: ', statement)
            cursor.execute(statement)
            self.__insertCategoryListOnDB(cursor)  # categoriesByProduct sendo inserido aqui
            if len(self.__similarList) > 0:
                self.__insertSimilars(cursor)
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def save(manager, func):
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
