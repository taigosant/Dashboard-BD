# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 11:03:42 2018

@author: Katiely
"""
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
    
def query2():
    print("\n\n\n")
    print("Informe o ASIN do produto:  ")
    productASIN = input()
    
def query3():
    print("\n\n\n")
    print("Informe o ASIN do produto:  ")
    productASIN = input()

def query4():
    print("\n\n\n")
    
def query5():
    print("\n\n\n")
    
def query6():
    print("\n\n\n")
   
def query7():
    print("\n\n\n")
         
    
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
    choiceInput = -1323323
    while(1):
        showMenu()
        choiceInput = int(input("-->"))
        if(choiceInput == 0):
            showBye()
            break
        else:
            choiceUser(choiceInput)
    