from .AccesoDatos import *
from .Socio import *
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
                   "WHERE socios.id = %s"
        try:
            datos = AccesoDatos()
            cur = datos.conectar()
            cur.execute(consulta,(socio.dni, socio.nombre, socio.apellido, socio.id))
            datos.desconectar()
        except OperationalError as e:
            raise Exception("ERROR FATAL")
        except Exception as a:
            raise Exception("Error al conectar a la base de datos")

    def baja_socio(self,socio):
        """
        Elimina un socio en la base de datos.
        :param socio: Objeto Socio a eliminar.
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

    def buscar_por_id(self,socio):
        """
        Busca un socio en la base de datos.
        :param socio: Objeto Socio a buscar.
        :return: El socio si es encontrado, None si no lo encuentra.
        """
        consulta = "SELECT * FROM socios WHERE idsocio = %s"
        encontrado = None
        try:
            datos = AccesoDatos()
            cur = datos.conectar()
            cur.execute(consulta,(socio.id))
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

    def siguiente(self,id):
        """
        Dada una id de socio, obtiene el socio con la siguiente id.
        :param id: La id a buscar.
        :return: El siguiente socio segun su id.
        """
        consulta = "select * from socios m " \
                   "where m.idsocio = (select min(idsocio) from socios s " \
                   "where s.idsocio > %s);"
        encontrado = None
        try:
            datos = AccesoDatos()
            cur = datos.conectar()
            cur.execute(consulta,(id))
            d = cur.fetchone()
            encontrado = Socio(d[1],d[2],d[3],d[0])
            datos.desconectar()
        except OperationalError as e:
            raise Exception("ERROR FATAL")
        except Exception as a:
            raise Exception("Error al conectar a la base de datos")
        return encontrado

    def anterior(self,id):
        """
        Dada una id de socio, obtiene el socio con la id anterior.
        :param id: La id a buscar.
        :return: El socio anterior segun su id.
        """
        consulta = "select * from socios m " \
                   "where m.idsocio = (select min(idsocio) from socios s " \
                   "where s.idsocio < %s);"
        encontrado = None
        try:
            datos = AccesoDatos()
            cur = datos.conectar()
            cur.execute(consulta,(id))
            d = cur.fetchone()
            encontrado = Socio(d[1],d[2],d[3],d[0])
            datos.desconectar()
        except OperationalError as e:
            raise Exception("ERROR FATAL")
        except Exception as a:
            raise Exception("Error al conectar a la base de datos")
        return encontrado

    def primero(self):
        """
        Encuentra el socio con la menor id.
        :return: El socio encontrado.
        """
        consulta = "select min(idsocio) from socios"
        try:
            datos = AccesoDatos()
            cur = datos.conectar()
            cur.execute(consulta)
            d = cur.fetchone()
            encontrado = Socio(d[1],d[2],d[3],d[0])
            datos.desconectar()
        except OperationalError as e:
            raise Exception("ERROR FATAL")
        except Exception as a:
            raise Exception("Error al conectar a la base de datos")
        return encontrado

    def ultimo(self):
        """
        Encuentra el socio con la mayor id.
        :return: El socio encontrado.
        """
        consulta = "select max(idsocio) from socios"
        try:
            datos = AccesoDatos()
            cur = datos.conectar()
            cur.execute(consulta)
            d = cur.fetchone()
            encontrado = Socio(d[1],d[2],d[3],d[0])
            datos.desconectar()
        except OperationalError as e:
            raise Exception("ERROR FATAL")
        except Exception as a:
            raise Exception("Error al conectar a la base de datos")
        return encontrado

    def contarDNI(self, dniSocio):
        """
        Busca la cantidad de socios con el numero de DNI dado.
        :param dniSocio: Numero de DNI a usar como parametro de busqueda.
        :return: El dni encontrado y la cantidad de repeticiones de su valor.
        """
        consulta = "select count(*)from socios where dni=%s"
        encontrado = None
        try:
            datos = AccesoDatos()
            cur = datos.conectar()
            cur.execute(consulta,(dniSocio))
            encontrado = cur.fetchall()
            datos.desconectar()
        except OperationalError as e:
            raise Exception("ERROR FATAL")
        except Exception as a:
            raise Exception("Error al conectar a la base de datos")
        return encontrado
