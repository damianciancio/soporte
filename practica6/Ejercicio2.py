from tkinter import *
entry=0

def calcular():
    global entry
    entry = entryMain.get()
    entryMain.delete(0,END)
    entryMain.insert(0,eval(entry))

"""Funciones que realizan las operaciones sobre los valores obtenidos."""
def addToEntry(toAdd):
    print(toAdd)
    entryMain.insert(END,toAdd)

"""Ventana principal y algunos de sus atrubutos"""
root = Tk()
root.title("Calculadora intermedia")

"""Frame va a contener los elementos de nuestra interfaz"""
"""bd -> define el tamaño del borde * relief -> define tipo de borde * widht y height -> dimensiones"""
mainFrame = Frame(root,bd=3,relief=SUNKEN,width=500,height=500)
mainFrame.pack()

#Fila 0
entryMain = Entry(mainFrame,bd=5,justify=RIGHT,relief=SUNKEN)
entryMain.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

#Fila 1
bot7 = Button(mainFrame,text="7", width=3,command=lambda: addToEntry(7))
bot7.grid(row=1,column=0,padx=3,pady=3)
bot8 = Button(mainFrame,text="8", width=3,command=lambda: addToEntry("8"))
bot8.grid(row=1,column=1,padx=3,pady=3)
bot9 = Button(mainFrame,text="9", width=3,command=lambda: addToEntry("9"))
bot9.grid(row=1,column=2,padx=3,pady=3)
botSuma = Button(mainFrame,text="+", width=3,command=lambda: addToEntry("+"))
botSuma.grid(row=1,column=3,padx=3,pady=3)

#Fila 2
bot4 = Button(mainFrame,text="4", width=3,command=lambda: addToEntry("4"))
bot4.grid(row=2,column=0,padx=3,pady=3)
bot5 = Button(mainFrame,text="5", width=3,command=lambda: addToEntry("5"))
bot5.grid(row=2,column=1,padx=3,pady=3)
bot6 = Button(mainFrame,text="6", width=3,command=lambda: addToEntry("6"))
bot6.grid(row=2,column=2,padx=3,pady=3)
botResta = Button(mainFrame,text="-", width=3,command=lambda: addToEntry("-"))
botResta.grid(row=2,column=3,padx=3,pady=3)

#Fila 3
bot1 = Button(mainFrame,text="1", width=3,command=lambda: addToEntry("1"))
bot1.grid(row=3,column=0,padx=3,pady=3)
bot2 = Button(mainFrame,text="2", width=3,command=lambda: addToEntry("2"))
bot2.grid(row=3,column=1,padx=3,pady=3)
bot3 = Button(mainFrame,text="3", width=3,command=lambda: addToEntry("3"))
bot3.grid(row=3,column=2,padx=3,pady=3)
botMult = Button(mainFrame,text="*", width=3,command=lambda: addToEntry("*"))
botMult.grid(row=3,column=3,padx=3,pady=3)

#Fila 4
bot0 = Button(mainFrame,text="0", width=3,command=lambda: addToEntry("0"))
bot0.grid(row=4,column=0,padx=3,pady=3)
botIgual = Button(mainFrame,text="=", width=3,command=lambda: calcular())
botIgual.grid(row=4,column=1,padx=3,pady=3,columnspan=2)
botDiv = Button(mainFrame,text="/", width=3,command=lambda: addToEntry("/"))
botDiv.grid(row=4,column=3,padx=3,pady=3)

root.mainloop()