# -*- coding: utf-8 -*-
"""
@author: Katiely
"""
# !/usr/bin/python3
from tkinter import *
import sys

root = Tk()
root.title("Amazon Dashboard")
root.geometry("750x700")
#root.configure(bg="white")

lbl = Label(root,width = 30, text = "Insira o asin do produto aqui: ")
lbl.place(x = 0, y = 50)
#funcao para pegar qual radioButton foi escolhido e o texto da entrada do usuario
def search():
    searchStr =  inputText.get().strip()
    typeSearch = var.get()
    if(typeSearch== 1):
        #result = mg.executeSelectStmt(Query.A_QUERY.format(asin="B00004YNH2", asin1="B00004YNH2"))
        messagebox.showinfo("Resultado Busca", "o resultado da busca aqui " + searchStr)
        print(typeSearch)
    if(typeSearch== 2):
       
        messagebox.showinfo("Resultado Busca", "o resultado da busca aqui " + searchStr)
        print(typeSearch)    
    if(typeSearch== 3):
       
        messagebox.showinfo("Resultado Busca", "o resultado da busca C " + searchStr)
        print(typeSearch)     
    print(searchStr)
    
bttn1 = Button(root,text = "Pesquisar",fg = "darkblue",command = search)
bttn1.place(x = 600, y = 49)

inputText = Entry(root,width = 60,bg="lightgrey")
inputText.place(x = 200, y = 50)


def sel():
   selection = str(var.get())

var = IntVar()
R1 = Radiobutton(root, text="Listar os 5 comentarios  mais uteis: com maior e menor avaliacao", variable=var, value=1,
                  command=sel)
R1.select()
R1.place(x = 10, y = 70)


R2 = Radiobutton(root, text="listar os produtos similares com maiores vendas", variable=var, value=2,
                  command=sel)
R2.place(x = 10, y = 90)

R3 = Radiobutton(root, text="evolucao diaria das medias de avaliacao ao longo do intervalo de tempo", variable=var, value=3,
                  command=sel)
R3.place(x = 10, y = 110)

Lb1 = Listbox(root, width = 85)
Lb1.insert(1, "Listar os 10 produtos lideres de venda em cada grupo de produtos")
Lb1.insert(2, "Listar os 10 produtos com a maior média de avaliações úteis positivas por produto")
Lb1.insert(3, "Listar a 5 categorias de produto com a maior média de avaliações úteis positivas por produto")
Lb1.insert(4, "Listar os 10 clientes que mais fizeram comentários por grupo de produto")
Lb1.place(x = 30 , y = 150)

#
def listButt():
    Lb1.get(ACTIVE)
    if(len(Lb1.curselection())>0):
        selectL= Lb1.curselection()[0]
        if(selectL==0):
             messagebox.showinfo("Resultado Busca", "o resultado da busca D ")
        if(selectL==1):
             messagebox.showinfo("Resultado Busca", "o resultado da busca E ")        
        if(selectL==2):
             messagebox.showinfo("Resultado Busca", "o resultado da busca F ")
        if(selectL==3):
             messagebox.showinfo("Resultado Busca", "o resultado da busca G ")     
     
        print(selectL)

btnList = Button(root,text="Listar",fg = "darkblue",command = listButt)
btnList.place(x = 600, y = 170)



root.mainloop()
