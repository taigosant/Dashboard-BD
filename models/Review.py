class Review(object):
    def __init__(self, date, votes, rating, helpful, productId, costumerId):
        self.__date = str(date).strip()
        self.__votes =  str(votes).strip()
        self.__rating = str(rating).strip()
        self.__helpful = str(helpful).strip()
        self.__productId = productId
        self.__constumerId= str(costumerId).strip()

    def toString(self):
        stringToReturn = "\n"
        stringToReturn += "date= " +  self.__date  + '\n'
        stringToReturn += "votes =" + str(self.__votes) + '\n'
        stringToReturn += "rating =" + str(self.__rating) + "\n"
        stringToReturn += "helpful =" + str(self.__helpful) + "\n"
        stringToReturn += "prod_id =" + str(self.__productId) + "\n"
        stringToReturn += "constumerId =" + self.__constumerId + "\n"
        return stringToReturn

    def executeInsertStatement(self, cursor):  # Todo "ExecuteInsertStatement"
        try:
            statement = "INSERT INTO review (r_date, votes, rating, helpful, prod_id, ID_Costumer)" \
                        " VALUES ('{date}',{votes},{rating},{helpful},{p_id}, '{id_cost}');".format(
                date=self.__date,
                votes=int(self.__votes),
                rating=int(self.__rating),
                helpful=int(self.__helpful),
                p_id=int(self.__productId),
                id_cost=self.__constumerId
            )
            # print('executing statement: ', statement)
            cursor.execute(statement)
            return True
        except Exception as e:
            print(e)
            return False

