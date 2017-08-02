from Tkinter import *

ventana = Tk()
marco = Frame(ventana).grid(row=0, column=0)

lblID = Label(marco, text="ID").grid(row=1, column=0, sticky="e")
txtID = Entry(marco).grid(row=1, column=1,columnspan=3)

lblDNI = Label(marco, text="DNI").grid(row=2, column=0, sticky="e")
txtDNI = Entry(marco).grid(row=2, column=1,columnspan=3)

lblNombre = Label(marco, text="Nombre").grid(row=3, column=0, sticky="e")
txtNombre = Entry(marco).grid(row=3, column=1,columnspan=3)

lblApellido = Label(marco, text="Apellido").grid(row=4, column=0, sticky="e")
txtApellido = Entry(marco).grid(row=4, column=1,columnspan=3)

#hijos = marco.winfo_children()
#for h in hijos:
#    if h.winfo_class() == lblApellido.__class__.__name__:
#        h.grid(sticky="E")

txtPrimero = Button(ventana,text="<<").grid(row=0, column=0)
txtAnterior = Button(ventana,text="<").grid(row=0, column=1)
txtSiguiente = Button(ventana,text=">").grid(row=0, column=2)
txtUltimo = Button(ventana,text=">>").grid(row=0, column=3)
ventana.mainloop()
