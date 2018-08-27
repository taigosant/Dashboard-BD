from typing import Any

class Product(object):

    def __init__(self, productId, assin, title, salesrank, groupId):
        self.__productId = productId
        self.__assin = assin
        self.__title = title
        self.__salesrank = salesrank
        self.__groupId = groupId

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


    def save(self, manager):
        try:
            conn = manager.getConnector()
            cursor = conn.cursor()
            statement = "INSERT INTO product (id_product, asin, salesrank, title)" \
                        " VALUES ({id},'{asin}',{salesrank},'{title}');".format(
                                                                            id=self.__productId,
                                                                            asin=self.__assin,
                                                                            salesrank=self.__salesrank,
                                                                            title=self.__title
                                                                            )
            print('executing statement: ', statement)
            cursor.execute(statement)
            cursor.close()
            conn.commit()
            return True
        except Exception as e:
            print(e)
            return False
