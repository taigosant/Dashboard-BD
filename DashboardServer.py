# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 11:03:42 2018

@author: Katiely
"""
from ManagerDB import Manager
from Query import Query
host = "localhost"
user = "postgres"

#user = sys.argv[2]
db_name = "bdzinho"
#db_name = sys.argv[3]
#password = sys.argv[4]
password = "senha123"
#path = sys.argv[5]

def showWrongChoice():
    print("_____________________________________________________\n")
    print("Essa escolha nao esta disponivel no sistema\nPor favor, digite as opcoes dentro do menu\n")
    print("_____________________________________________________\n")
def showBye():
    print("______________________\n")
    print("SAINDO ...... TCHAU ")
    print("______________________")
def showWelcome():
    print("**************************************************\n")
    print("Amazon product co-purchasing network metadata")
    print("**************************************************\n")
def showMenu():
    print("-------------------------------\n")
    print("(1) listar os 5 comentarios mais uteis e com maior avaliacao e os 5 comentarios mais uteis e com menor avaliacao")
    print("(2) listar os produtos similares com maiores vendas do que ele")
    print("(3) mostrar a evolucao diaria das medias de avaliacao ao longo do intervalo de tempo")
    print("(4) Listar os 10 produtos lideres de venda em cada grupo de produtos")
    print("(5) Listar os 10 produtos com a maior media de avaliacoes uteis positivas por produto")
    print("(6) Listar a 5 categorias de produto com a maior media de avaliacoes uteis positivas por produto")
    print("(7) Listar os 10 clientes que mais fizeram comentarios por grupo de produto")
    print("(0) SAIR")
    print("-------------------------------\n")
def query1():
    print("\n\n\n")
    print("Informe o ASIN do produto:  ")
    productASIN = input()
    result = mg.executeSelectStmt(Query.A_QUERY.format(asin=productASIN, asin1=productASIN))
    print(result, '\n')
    
def query2():
    print("\n\n\n")
    print("->Informe o ASIN do produto:  ")
    productASIN = input()
    #"B00004YNH2"
    result1 = mg.executeSelectStmt(Query.B_QUERY.format(ASIN=productASIN))
    print(result1, '\n')
    
def query3():
    print("\n\n\n")
    print("Informe o ASIN do produto:  ")
    productASIN = input()
    result2 = mg.executeSelectStmt(Query.C_QUERY.format(asin=productASIN))
    print(result2, '\n')

def query4():
    print("\n\n\n")
    result3 = mg.executeSelectStmt(Query.D_QUERY)
    print(result3, '\n')
    
def query5():
    print("\n\n\n")
    result4 = mg.executeSelectStmt(Query.E_QUERY)
    print(result4, '\n')
    
def query6():
    print("\n\n\n")
    result5 = mg.executeSelectStmt(Query.F_QUERY)
    print(result5, '\n')
def query7():
    print("\n\n\n")
    result6 = mg.executeSelectStmt(Query.G_QUERY)
    print(result6, '\n')
         
    
def choiceUser(choiceInput):
    if(choiceInput==1):
        query1()
    elif(choiceInput==2):
        query2()
    elif(choiceInput==3):
        query3() 
    elif(choiceInput==4):
        query4()
    elif(choiceInput==5):
        query5() 
    elif(choiceInput==6):
        query6() 
    elif(choiceInput==7):
        query7() 
    else:
        
        showWrongChoice()
        
        
    
if __name__ == '__main__':
    showWelcome()
    mg = Manager(host, user, db_name, password)
    mg.connect()
    if mg.isConnected():
    	choiceInput = -1323323
    	while(1):
        	showMenu()
        	choiceInput = int(input("-->"))
        	if(choiceInput == 0):
        		showBye()
        		break
        	else:
        		choiceUser(choiceInput)
    