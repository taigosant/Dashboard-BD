from typing import Any


class Product(object):

    def __init__(self, productId, assin, title, salesrank, groupId):
        self.__productId = productId
        self.__assin = assin
        self.__title = title
        self.__salesrank = salesrank
        self.__groupId = groupId

    def toString(self):
        out = "Title: {title}\n" \
              "ASSIN: {assin}\n" \
              "SalesRank: {salesrank}\n" \
              "".format(
                        title=self.__title,
                        assin=self.__assin,
                        salesrank=self.__salesrank
                        )
        return out
