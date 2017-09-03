from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from practica5.CNSocios import CNSocios
from practica5.Socio import Socio


class MainWindow():

    tree = None

    def refrescar(self):
        try:
            socios = CNSocios().todos()
            for row in self.tree.get_children():
                self.tree.delete(row)
            socios = CNSocios().todos()
            for s in socios:
                self.tree.insert("",s.id,text=s.id,values=(s.nombre, s.apellido, s.dni))
        except Exception as e:
            pass

    def open_edit_window(self,isAlta):
        socio = None
        if not isAlta:
            socio = self.get_socio_from_table()
            if socio == None:
                return None
        EditWindow(isAlta, socio, self)

    def get_socio_from_table(self):
        curItem = self.tree.focus()
        if curItem == '':
            return None
        dict = self.tree.item(curItem)
        socio = Socio(dict["values"][2],dict["values"][0],dict["values"][1],dict["text"])
        return socio


    def delete(self):
        socio = self.get_socio_from_table()
        if socio == None:
            return None
        else:
            try:
                CNSocios().eliminar(socio)
            except Exception as e:
                pass
            self.refrescar()

    def __init__(self):
        root = Tk()
        frame = Frame(root)
        self.tree = ttk.Treeview(frame)

        self.tree["columns"]=("nombre","apellido","dni")
        self.tree.column("nombre", width=100)
        self.tree.column("apellido", width=100)
        self.tree.column("dni", width=100)
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("apellido", text="Apellido")
        self.tree.heading("dni", text="Dni")
        self.tree.heading("#0", text='Id', anchor='w')
        self.tree.column("#0", anchor="w")

        frameBotones = Frame(frame)
        botonAlta = Button( frameBotones, text = "Alta", command = lambda: self.open_edit_window(True))
        botonEditar = Button( frameBotones, text = "Editar", command = lambda: self.open_edit_window(False))
        botonEliminar = Button( frameBotones, text = "Eliminar", command = lambda: self.delete())

        self.refrescar()

        frame.pack()
        self.tree.pack()
        frameBotones.pack()
        botonAlta.pack()
        botonEditar.pack()
        botonEliminar.pack()

        root.mainloop()

class EditWindow():
    root_edit = None
    entry_nombre = None
    entry_apellido = None
    entry_dni = None
    isAlta = True
    idSocio = None
    socio = None
    parent = None

    def __init__(self,isAlta, socio, parent):
        self.isAlta = isAlta
        if not isAlta:
            self.socio = socio
            self.idSocio = socio.id
        self.parent = parent
        self.get_edit_window()

    def get_edit_window(self):
        self.root_edit = Tk()
        frame_edit = Frame(self.root_edit)

        Label(frame_edit, text="Nombre").grid(row=0)
        Label(frame_edit, text="Apellido").grid(row=1)
        Label(frame_edit, text="Dni").grid(row=2)


        self.entry_nombre = Entry(frame_edit)
        self.entry_apellido = Entry(frame_edit)
        self.entry_dni = Entry(frame_edit)

        self.entry_nombre.grid(row=0, column=1)
        self.entry_apellido.grid(row=1, column=1)
        self.entry_dni.grid(row=2, column=1)

        if not self.isAlta:
            self.map_socio_into_edit_window(self.socio)

        botonGuardar = Button( frame_edit, text = "Guardar", command = lambda: self.save_changes())
        botonCancelar = Button( frame_edit, text = "Cancelar", command = lambda: self.quit())


        botonGuardar.grid(row=3,column=0)
        botonGuardar.grid(row=3,column=1)


        frame_edit.pack()
        self.root_edit.mainloop()

    def map_socio_into_edit_window(self, socio):
        self.entry_nombre.insert(0,socio.nombre)
        self.entry_apellido.insert(0,socio.apellido)
        self.entry_dni.insert(0,socio.dni)

    def map_socio_from_window(self):
        dni = self.entry_dni.get()
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        socio = Socio(dni,nombre,apellido)
        return socio


    def quit(self):
        self.entry_apellido.insert(0,"")
        self.entry_nombre.insert(0,"")
        self.entry_dni.insert(0,"")
        self.socio = None
        self.idSocio = None
        self.isAlta = None
        self.parent.refrescar()
        self.root_edit.destroy()

    def save_changes(self):
        socio = self.map_socio_from_window()
        if not self.isAlta:
            socio.id = self.socio.id
            try:
                if ValidacionSocio(self).validarModificacion(socio):
                    CNSocios().modificar(socio)
            except Exception as e:
                pass
        else:
            try:
                if ValidacionSocio(self).validarAlta(socio):
                    CNSocios().alta(socio)
            except Exception as e:
                pass
        self.parent.refrescar()

class ValidacionSocio():

    parent = None
    cn= None
    def __init__(self, parent):
        self.parent = parent
        self.cn = CNSocios()

    def validarAlta(self, socio):
        if self.cn.existe_socio(socio):
            print("El socio ya existe.")
            return False
        if self.cn.llego_al_maximo_de_socios():
            print("Error","Se llego al maximo de socios")
            return False
        if not self.cn.validar_nombre_y_apellido(socio):
            print("Error","El nombre y el apellido deben tener al menos 3 y mas de 25 caracteres cada uno")
            return False
        if len(socio.dni) == 0:
            print("Ingrese dni")
            return False
        return True

    def validarModificacion(self,socio):
        if not self.cn.validar_nombre_y_apellido(socio):
            print("Error","El nombre y el apellido deben tener al menos 3 y mas de 25 caracteres cada uno")
            return False
        if len(socio.dni) == 0:
            print("Ingrese dni")
            return False
        return True



MainWindow()
