from practica4.AccesoDatos import *
from practica4.Socio import *
from pymysql import *

class CDSocios():

    def alta_socio(self,socio):
        """
        Inserta un nuevo socio en la base de datos.
        :param socio: Objeto Socio a insertar.
        :return: 
        """
        consulta = "INSERT INTO socios(dni, nombre, apellido) VALUES (%s, %s, %s)"
        try:
            datos = AccesoDatos()
            cur = datos.conectar()
            cur.execute(consulta, (socio.dni, socio.nombre, socio.apellido))
            datos.desconectar()
        except OperationalError as e:
            raise Exception("ERROR FATAL")
        except Exception as a:
            raise Exception("Error al conectar a la base de datos")

    def modificar_socio(self,socio):
        """
        Modifica un socio de la base de datos.
        :param socio: Objeto Socio con los nuevos valores a guardar.
        :return: 
        """
        consulta = "UPDATE socios SET socios.dni = %s, socios.nombre = %s, socios.apellido = %s" \
                   "WHERE socios.idsocio = %s"
        try:
            datos = AccesoDatos()
            cur = datos.conectar()
            cur.execute(consulta,(socio.dni, socio.nombre, socio.apellido, socio.id))
            datos.desconectar()
        except OperationalError as e:
            raise Exception("ERROR FATAL")
        except Exception as a:
            raise Exception("Error al conectar a la base de datos")

    def baja_socio(self,idSocio):
        """
        Elimina un socio en la base de datos.
        :param idSocio: Numero de ID del socio a eliminar.
        :return: 
        """
        consulta = "DELETE FROM socios WHERE idsocio = %s"
        try:
            datos = AccesoDatos()
            cur = datos.conectar()
            cur.execute(consulta,(idSocio))
            datos.desconectar()
        except OperationalError as e:
            raise Exception("ERROR FATAL")
        except Exception as a:
            raise Exception("Error al conectar a la base de datos")

    def buscar_por_id(self,idSocio):
        """
        Busca un socio en la base de datos.
        :param idSocio: Numero de ID del socio a buscar.
        :return: El socio si es encontrado, None si no lo encuentra.
        """
        consulta = "SELECT * FROM socios WHERE idsocio = %s"
        try:
            datos = AccesoDatos()
            cur = datos.conectar()
            cur.execute(consulta,(idSocio))
            d = cur.fetchone()
            encontrado = Socio(d[1],d[2],d[3],d[0])
            datos.desconectar()
        except OperationalError as e:
            raise Exception("ERROR FATAL")
        except Exception as a:
            raise Exception("Error al conectar a la base de datos")
        return encontrado

    def buscar_todos(self):
        """
        Busca todos los socios y su informacion de la base de datos.
        :return: Una lista con todos los objetos Socio obtenidos.
        """
        consulta = "SELECT * FROM socios"
        encontrados = []
        try:
            datos = AccesoDatos()
            cur = datos.conectar()
            cur.execute(consulta)
            data = cur.fetchall()
            for d in data:
                encontrados.append(Socio(d[1],d[2],d[3],d[0]))
            datos.desconectar()
        except OperationalError as e:
            raise Exception("ERROR FATAL")
        except Exception as a:
            raise Exception("Error al conectar a la base de datos")
        return encontrados

    def print_todos(self,encontrados):
        """
        Muestra en pantalla todos los elementos de una lista de objetos Socio.
        :param encontrados: Lista de objetos Socio a imprimir
        """
        for row in encontrados:
            print("ID : ",row.id," Nombre: ",row.nombre," Apellido: ", row.apellido," DNI: ",row.dni)

    def siguiente(self,id):
        """
        Dada una id de socio, obtiene el socio con la siguiente id.
        :param id: El numero de ID del socio a buscar.
        """
        consulta = "select * from socios m " \
                   "where m.idsocio = (select min(idsocio) from socios s " \
                   "where s.idsocio > %s);"
        try:
            datos = AccesoDatos()
            cur = datos.conectar()
            cur.execute(consulta,(id))
            d = cur.fetchone()
            socio = Socio(d[1],d[2],d[3],d[0])
            datos.desconectar()
        except OperationalError as e:
            raise Exception("ERROR FATAL")
        except Exception as a:
            raise Exception("Error al conectar a la base de datos")
        print("ID : ", socio.id, "\nNombre: ", socio.nombre, "\nApellido: ", socio.apellido, "\nDNI: ", socio.dni)

    def anterior(self,id):
        """
        Dada una id de socio, obtiene el socio con la id anterior.
        :param id: El numero de ID del socio a buscar.
        """
        consulta = "select * from socios m " \
                   "where m.idsocio = (select min(idsocio) from socios s " \
                   "where s.idsocio < %s);"
        try:
            datos = AccesoDatos()
            cur = datos.conectar()
            cur.execute(consulta,(id))
            d = cur.fetchone()
            socio = Socio(d[1],d[2],d[3],d[0])
            datos.desconectar()
        except OperationalError as e:
            raise Exception("ERROR FATAL")
        except Exception as a:
            raise Exception("Error al conectar a la base de datos")
        print("ID : ", socio.id, "\nNombre: ", socio.nombre, "\nApellido: ", socio.apellido, "\nDNI: ", socio.dni)

    def primero(self):
        """
        Muestra en pantalla el socio con el menor id.
        """
        consulta = "select * from socios order by idsocio asc limit 1"
        try:
            datos = AccesoDatos()
            cur = datos.conectar()
            cur.execute(consulta)
            d = cur.fetchone()
            socio = Socio(d[1],d[2],d[3],d[0])
            datos.desconectar()
        except OperationalError as e:
            raise Exception("ERROR FATAL")
        except Exception as a:
            raise Exception("Error al conectar a la base de datos")
        print("ID : ", socio.id, "\nNombre: ", socio.nombre, "\nApellido: ", socio.apellido, "\nDNI: ", socio.dni)

    def ultimo(self):
        """
        Muestra en pantalla el socio con el mayor id.
        """
        consulta = "select * from socios order by idsocio desc limit 1"
        try:
            datos = AccesoDatos()
            cur = datos.conectar()
            cur.execute(consulta)
            d = cur.fetchone()
            socio = Socio(d[1],d[2],d[3],d[0])
            datos.desconectar()
        except OperationalError as e:
            raise Exception("ERROR FATAL")
        except Exception as a:
            raise Exception("Error al conectar a la base de datos")
        print("ID : ", socio.id, "\nNombre: ", socio.nombre, "\nApellido: ", socio.apellido, "\nDNI: ", socio.dni)

    def contarDNI(self, dniSocio):
        """
        Busca la cantidad de socios con el numero de DNI dado.
        :param dniSocio: Numero de DNI a usar como parametro de busqueda.
        """
        consulta = "select count(*), nombre, apellido, dni from socios where dni=%s"
        try:
            datos = AccesoDatos()
            cur = datos.conectar()
            cur.execute(consulta,(dniSocio))
            encontrado = cur.fetchone()
            datos.desconectar()
        except OperationalError as e:
            raise Exception("ERROR FATAL")
        except Exception as a:
            raise Exception("Error al conectar a la base de datos")
        print("Repeticiones : ", encontrado[0], "\nNombre: ", encontrado[1], "\nApellido: ", encontrado[2], "\nDNI: ", encontrado[3])

    def crear_socio_sin_id(self):
        """
        Crea un socio sin especificar su numero de ID
        :return: Un objeto socio con los datos ingresados.
        """
        dni=input("Ingrese dni del socio: ")
        nombre=input("Ingrese nombre del socio: ")
        apellido=input("Ingrese apellido del socio: ")
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

    def menu(self):
        """
        Interfaz principal del programa, donde se pueden ejecutar todas las consultas
        requeridas en la practica.
        """
        print("**************************MENU*****************************")
        print("1 . Alta de socio.")
        print("2 . Modificar socio.")
        print("3 . Baja de socio.")
        print("4 . Buscar socio por ID.")
        print("5 . Listar todos los socios.\n")
        print("6 . Mostrar socio siguiente.")
        print("7 . Mostrar socio anterior.")
        print("8 . Mostrar primer socio.")
        print("9 . Mostrar ultimo socio.")
        print("0 . Buscar repeticiones de un DNI.")
        print()
        opt = int(input("Ingrese una opcion: "))

        if (opt==1):
            self.alta_socio(self.crear_socio_sin_id())
        elif (opt == 2):
            self.modificar_socio(self.crear_socio_con_id())
        elif (opt == 3):
            self.baja_socio(input("Ingrese la id del socio a eliminar: "))
        elif (opt == 4):
            socio = self.buscar_por_id(input("Ingrese la id del socio a buscar: "))
            print("ID : ",socio.id,"\nNombre: ",socio.nombre,"\nApellido", socio.apellido,"\nDNI: ",socio.dni)
        elif (opt == 5):
            self.print_todos(self.buscar_todos())
        elif (opt == 6):
            self.siguiente(input("Ingrese el ID del socio que desea buscar: "))
        elif (opt == 7):
            self.anterior(input("Ingrese el ID del socio que desea buscar: "))
        elif (opt == 8):
            self.primero()
        elif (opt == 9):
            self.ultimo()
        elif (opt == 0):
            self.contarDNI(input("Ingrese el DNI del socio que desea buscar: "))
        else:
            self.menu()

practica4 = CDSocios()
practica4.menu()