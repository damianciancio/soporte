from practica5.CDSocios import *
from practica5.Socio import *

class CNSocios():

    max_cantidad_socios = 200

    def input_nombre(self):
        nombre = ''
        while (len(nombre) < 3 or len(nombre)>25):
            nombre = input('Ingrese nombre (longitud entre 3 y 25 caracteres) : ')
        return nombre

    def input_apellido(self):
        apellido = None
        while (len(apellido) < 3 or len(apellido)>25):
            apellido = input("Ingrese apellido (longitud entre 3 y 25 caracteres): ")
        return apellido

    def crear_socio_sin_id(self):
        """
        Crea un socio sin especificar su numero de ID
        :return: Un objeto socio con los datos ingresados.
        """
        dni=input("Ingrese dni del socio: ")
        nombre=self.input_nombre()
        apellido=self.input_apellido()
        return Socio(dni,nombre,apellido)

    def crear_socio_con_id(self):
        """
        Crea un socio especificando su numero de ID
        :return: Un objeto socio con los datos ingresados.
        """
        id=input("Ingrese la ID del socio a modificar: ")
        dni=input("Ingrese dni del socio: ")
        nombre=input("Ingrese nombre del socio: ")
        apellido=input("Ingrese apellido del socio: ")
        return Socio(dni,nombre,apellido,id)

    def existe_socio(self,socio):
        return (CDSocios().contarDNI(socio.dni) > 0)

    def llego_al_maximo_de_socios(self):
        return CDSocios().buscar_todos().count() < self.max_cantidad_socios

    def validar_data(self,socio):
        return (not self.existe_socio(socio) and self.llego_al_maximo_de_socios())

    def alta_socio(self,socio):
        if (self.validar_data(socio)):
            CDSocios().alta_socio(socio)

    def borrar_socio(self,socio):
        CDSocios().baja_socio(socio)

    def modificar_socio(self,socio):
        CDSocios().modificar_socio(socio)

    def buscar_por_id(self,idSocio):
        socio = CDSocios().buscar_por_id(idSocio)
        print("ID : ", socio.id, "\nNombre: ", socio.nombre, "\nApellido", socio.apellido, "\nDNI: ", socio.dni)

    def buscar_por_dni(self,dniSocio):
        socio = CDSocios().buscar_por_id(dniSocio)
        print("ID : ", socio.id, "\nNombre: ", socio.nombre, "\nApellido", socio.apellido, "\nDNI: ", socio.dni)

    def buscar_todos(self):
        return CDSocios().buscar_todos()

    def print_todos(self,encontrados):
        """
        Muestra en pantalla todos los elementos de una lista de objetos Socio.
        :param encontrados: Lista de objetos Socio a imprimir
        """
        for row in encontrados:
            print("ID : ",row.id," Nombre: ",row.nombre," Apellido: ", row.apellido," DNI: ",row.dni)

    def menu(self):
        """
        Interfaz principal del programa, donde se pueden ejecutar todas las consultas
        requeridas en la practica.
        """
        print("**************************MENU*****************************")
        print("1 . Alta de socio.")
        print("2 . Borrar socio.")
        print("3 . Modificar socio.")
        print("4 . Buscar socio por ID.")
        print("5 . Listar todos los socios.\n")
        print()
        opt = int(input("Ingrese una opcion: "))

        if (opt==1):
            self.alta_socio(self.crear_socio_sin_id())
        elif (opt == 2):
            self.borrar_socio(self.crear_socio_con_id())
        elif (opt == 3):
            self.modificar_socio(self.crear_socio_con_id())
        elif (opt == 4):
            self.buscar_por_id(input("Ingrese la id del socio a buscar: "))
        elif (opt == 5):
            self.print_todos(self.buscar_todos())
        else:
            self.menu()

cn = CNSocios()
cn.menu()