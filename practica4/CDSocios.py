from .AccesoDatos import *
from .Socio import *
from pymysql import *

class CDSocios():

    def alta(self,socio):
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



    def modificacion(self,socio):
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

    def baja(self,socio):
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

    def primero(self,id):
        consulta = "select min(idsocio) from socios"
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

    def ultimo(self,id):
        consulta = "select max(idsocio) from socios"
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


    def contarDNI(self, dniSocio):
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
