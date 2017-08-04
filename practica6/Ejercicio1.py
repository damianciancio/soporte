from tkinter import *

"""Definimos la ventana principal y algunos de sus atrubutos"""
root = Tk()
root.title("Calculadora prehistorica")
# root.protocol("WM_DELETE_WINDOW",pide_cerrar) """Llama al metodo pide_cerrar para cerrar la ventana"""
root.configure(background="lightgreen")

"""Definimos un Frame que vamos a poner dentro de la ventana principal"""
"""bd -> define el tamaño del borde
   relief -> define tipo de borde 
   widht y height -> dimensiones"""
mainFrame = Frame(root,bd=3,relief=SUNKEN,width=500,height=500)
mainFrame.pack()

Label(mainFrame,text="Primer Operando",width=25).grid(row=0,column=0)
Label(mainFrame,text="Segundo Operando",width=25).grid(row=0,column=1)

Entry(mainFrame,justify=RIGHT).grid(row=1,column=0)
Entry(mainFrame,justify=RIGHT).grid(row=1,column=1)

Button(mainFrame,text="+",width=3).grid(row=1,column=2)
Button(mainFrame,text="-",width=3).grid(row=1,column=3)
Button(mainFrame,text="*",width=3).grid(row=1,column=4)
Button(mainFrame,text="/",width=3).grid(row=1,column=5)

Label(mainFrame,text="Resultado -->").grid(row=2,column=0)
Entry(mainFrame,justify=RIGHT).grid(row=2,column=1)

root.mainloop()