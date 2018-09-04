class Category(object): 
	def __init__ (self,categoryId,title):
		self.__categoryId= categoryId
		self.__title = title
	def toString(self):
		stringToReturn  = "CategoryID = " + self.__categoryId + "\n"
		stringToReturn += " Title = " + self.__title  + "\n"
		return stringToReturn	