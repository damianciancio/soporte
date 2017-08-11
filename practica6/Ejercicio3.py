from tkinter import *
from tkinter.ttk import *

root = Tk()

tree = Treeview(root)

#Definimos las columnas y las cabeceras.
tree["columns"]=("one","two")
tree.column("#0",width="100")
tree.column("one",width=100)
tree.column("two",width=100)
tree.heading("#0",text="Porvincia")
tree.heading("one",text="Ciudad")
tree.heading("two",text="Codigo Postal")

#Creamos los desplegables raiz: Parametros: (parent, index, id,texto)
chaco=tree.insert("",1,"chaco",text="Chaco")
stafe=tree.insert("",2,"stafe",text="Santa Fe")
cordoba=tree.insert("",3,"cordoba",text="Cordoba")

#Agregamos elementos a los desplegables. Parametros: (parent, index, id, text, values)
tree.insert(chaco, 1, "rst", text="", values=("Resistencia","H3500"))
tree.insert(chaco, 2, "ptr", text="", values=("Puerto Tirol","H3505"))
tree.insert(chaco, 3, "mcg", text="", values=("Machagai","H3534"))

tree.insert(stafe, 1, "sfe", text="", values=("Santa Fe","S3000"))
tree.insert(stafe, 2, "ros", text="", values=("Rosario","S2000"))
tree.insert(stafe, 3, "vto", text="", values=("Venado Tuerto","S2600"))

tree.insert(cordoba, 1, "cba", text="", values=("Cordoba","X5000"))
tree.insert(cordoba, 2, "rct", text="", values=("Rio Cuarto","X5800"))
tree.insert(cordoba, 3, "vma", text="", values=("Villa Maria","H3534"))

tree.pack()
root.mainloop()
