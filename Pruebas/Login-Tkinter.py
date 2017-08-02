from Tkinter import *

raiz = Tk()
marco = Frame(raiz).grid(row=0, column=0)

usuario = StringVar()
clave = StringVar()

lblUsuario= Label(marco, text="Usuario:").grid(row=0, column=0, sticky="E")
txtUsuario = Entry(marco, textvariable=usuario).grid(row=0, column=1, columnspan=5)


lblContra= Label(marco, text="Contrasea:").grid(row=1, column=0, sticky="E")
txtContra = Entry(marco, textvariable=clave).grid(row=1, column=1, columnspan=5)

btnAceptar = Button(marco, text="Aceptar", command=aceptar).grid(row=3, column=3, columnspan=2)
btnCancelar = Button(marco, text="Cancelar").grid(row=3, column=5, columnspan=2)

lblIngreso = Label(marco, text="").grid(row=4, column=3)

raiz.mainloop()
