class Review(object):
    def __init__(self,date, votes, rating, helpful,productId,costumerId):
        self.__date = date
        self.__votes =  votes
        self.__rating = rating
        self.__helpful = helpful
        self.__productId = productId
        self.__constumerId= costumerId

    def toString(self):
        stringToReturn = "\n"
        stringToReturn += "date= " +  self.__date  + '\n'
        stringToReturn += "votes =" + str(self.__votes) + '\n'
        stringToReturn += "rating =" + str(self.__rating) + "\n"
        stringToReturn += "helpful =" + str(self.__helpful )+ "\n"
        stringToReturn += "constumerId =" +  self.__constumerId + "\n"
        return stringToReturn    