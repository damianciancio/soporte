from practica5.AccesoDatos import *
from practica5.Socio import *
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

    def baja_socio(self,socio):
        """
        Elimina un socio en la base de datos.
        :param idSocio: Numero de ID del socio a eliminar.
        :return: 
        """
        consulta = "DELETE FROM socios WHERE idsocio = %s"
        try:
            datos = AccesoDatos()
            cur = datos.conectar()
            cur.execute(consulta,(socio.id))
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

    def buscar_por_dni(self,socio):

        consulta = "SELECT * FROM socios WHERE dni = %s"
        encontrado = None
        try:
            datos = AccesoDatos()
            cur = datos.conectar()
            cur.execute(consulta,(socio.dni))
            d = cur.fetchone()
            if not d == None:
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
