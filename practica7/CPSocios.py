from tkinter import ttk
from tkinter import *

root = Tk()
frame = Frame(root)
tree = ttk.Treeview(frame)

tree["columns"]=("nombre","apellido","dni")
tree.column("nombre", width=100)
tree.column("apellido", width=100)
tree.column("dni", width=100)
tree.heading("nombre", text="Nombre")
tree.heading("apellido", text="Apellido")
tree.heading("dni", text="Dni")
tree.heading("#0", text='Id', anchor='w')
tree.column("#0", anchor="w")

frameBotones = Frame(frame)
botonAlta = Button( frameBotones, text = "Alta", command = "hola")


frame.pack()
tree.pack()
frameBotones.pack()
botonAlta.pack()

root.mainloop()

def hola():
    print("hola")