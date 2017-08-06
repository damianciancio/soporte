from tkinter import *
valor1=0
valor2=0

"""Funcion que obtiene los valores con los que se van a realizar las operaciones"""
def get_valores():
    global valor1
    valor1=0
    if (entryValor1.get()!=''):
        valor1 = int(entryValor1.get())
    global valor2
    valor2=0
    if entryValor2.get()!='':
        valor2 = int(entryValor2.get())

"""Funciones que realizan las operaciones sobre los valores obtenidos."""
def calcular_suma():
    get_valores()
    entryResultado.delete(0,END)
    entryResultado.insert(0,valor1+valor2)

def calcular_resta():
    get_valores()
    entryResultado.delete(0,END)
    entryResultado.insert(0,valor1-valor2)

def calcular_mult():
    get_valores()
    entryResultado.delete(0,END)
    entryResultado.insert(0,valor1*valor2)

def calcular_division():
    get_valores()
    entryResultado.delete(0,END)
    if (valor2 != 0):
        entryResultado.insert(0,valor1/valor2)
    else:
        entryResultado.insert(0,"ERROR")


"""Ventana principal y algunos de sus atrubutos"""
root = Tk()
root.title("Calculadora sencilla")

"""Frame va a contener los elementos de nuestra interfaz"""
"""bd -> define el tamaño del borde * relief -> define tipo de borde * widht y height -> dimensiones"""
mainFrame = Frame(root,bd=3,relief=SUNKEN,width=500,height=500)
mainFrame.pack()

#Fila 1
label1 = Label(mainFrame,text="Primer Operando",width=25)
label1.grid(row=0,column=0)
label2= Label(mainFrame,text="Segundo Operando",width=25)
label2.grid(row=0,column=1)

#Fila 2
entryValor1 = Entry(mainFrame,justify=RIGHT)
entryValor1.grid(row=1,column=0)
entryValor2 = Entry(mainFrame,justify=RIGHT)
entryValor2.grid(row=1,column=1)

#Fila 3
labelResultado= Label(mainFrame,text="Resultado -->")
labelResultado.grid(row=2,column=0)
entryResultado = Entry(mainFrame,bd=5,justify=RIGHT,relief=SUNKEN)
entryResultado.grid(row=2,column=1)

"""Botones de la interfaz."""
botonSuma = Button(mainFrame,text="+",width=3,command=calcular_suma)
botonSuma.grid(row=1,column=2)
botonResta = Button(mainFrame,text="-",width=3,command=calcular_resta)
botonResta.grid(row=1,column=3)
botonMultiplicacion = Button(mainFrame,text="*",width=3,command=calcular_mult)
botonMultiplicacion.grid(row=1,column=4)
botonDivision = Button(mainFrame,text="/",width=3,command=calcular_division)
botonDivision.grid(row=1,column=5)

root.mainloop()