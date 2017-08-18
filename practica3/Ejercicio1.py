import pymysql
import datetime

#<editor-fold desc="Definicion de las clases Persona y Peso.">
class Persona():
    nombre = ""
    fechaNac = datetime.date(2000,1,1)
    dni = 0
    altura = 0
    id = None
    pesos = []
    def __init__(self, nombre, fechaNac, dni, altura,id = None, pesos = []):
        self.nombre = nombre
        self.fechaNac = fechaNac
        self.dni = dni
        self.altura = altura
        self.id = id
        self.pesos = pesos

class Peso():
    idPersona = 0
    peso = 0
    fecha = 0
    def __init__(self,idPersona, peso, fecha):
        self.idPersona = idPersona
        self.peso = peso
        self.fecha = fecha
#</editor-fold>

class Practica3():

    conn = None
    cur = None

    def conectar(self):
        """
        Conecta a la base de datos especificada en conn.
        :return: Un cursor apuntando a la base de datos.
        """
        global conn, cur
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', password='', db='personas')
        self.cur = self.conn.cursor()
        return self.cur

    def desconectar(self):
        """
        Cierra la conexion a la base de datos.
        """
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    def get_persona_from_console(self):
        """
        Crea un objeto Persona a partir de informacion ingresada por el usuario.
        :return: El objeto Persona creado.
        """
        nom = str(input("Ingrese un nombre: "))
        fechaNac = str(input("Ingrese fecha de nacimiento(yyyy-mm-dd): "))
        dni = input("Ingrese el documento: ")
        altura = input("Ingrese altura: ")
        return Persona(nom,fechaNac,dni,altura)

    def select_all(self):
        """
        Ejercicio 1.
        Busca todos los elementos de la tabla personas, los mapea a objetos y los almacena en un arreglo.
        Luego imprime el contenido de dicho arreglo.
        :return: Un arreglo con todas las personas.
        """
        query = "select * from persona"
        try:
            self.cur = self.conectar()
            self.cur.execute(query)
            data = self.cur.fetchall()
            array = []
            for d in data:
                array.append(Persona(d[1],d[2],d[3],d[4],d[0]))
            self.desconectar()
        except Exception:
            pass
        for p in array:
            print("Nombre: ", p.nombre)
            print("Fecha de Nacimiento: ", p.fechaNac)
            print("DNI: ", p.dni)
            print("Altura: ", p.altura)
            print("=======================================================================================")

    def insert_row(self, persona):
        """
        Ejercicio 2.
        Inserta en la base de datos una persona.
        :param persona: La persona a ingresar a la base de datos.
        """
        query = "INSERT INTO persona(nombre, fechaNacimiento, dni, altura) VALUES (%s, %s, %s, %s)"
        try:
            self.cur = self.conectar()
            print("INSIDE: ", persona.nombre, persona.fechaNac, persona.altura, persona.dni)
            self.cur.execute(query, (persona.nombre, persona.fechaNac, persona.dni, persona.altura))
            self.desconectar()
        except Exception:
            pass

    def delete_persona(self, persona):
        """
        Ejercicio 3.
        Elimina de la base de datos una persona.
        :param persona: La persona a eliminar de la base de datos.
        """
        try:
            self.conectar()
            query = "DELETE FROM persona WHERE idpersona = %s"
            self.cur.execute(query, (persona.id))
            self.desconectar()
        except Exception:
            pass

    def get_persona_byDNI(self,persona):
        """
        Ejercicio 4.
        Buscar en la base de datos una persona segun su DNI.
        :param persona: La persona a buscar segun su DNI.
        :return: La persona encontrada.
        """
        try:
           self.conectar()
           query = "select * from persona where dni=%s"
           self.cur.execute(query, (persona.dni))
           d = self.cur.fetchone()
           found = Persona(d[1],d[2],d[3],d[4],d[0])
           self.desconectar()
           return found
        except Exception as exc:
            print(exc)
            pass

    def update_persona(self,persona):
        """
        Ejercicio 5.
        Busca en la base de datos una persona y actualiza su informacion.
        :param persona: Persona con los datos actualizados para ingresar a la base de datos.
        :return:
        """
        try:
            self.conectar()
            query = "update persona set nombre = %s, fechaNacimiento= %s, dni=%s, altura=%s where idpersona = %s"
            self.cur.execute(query, (persona.nombre , persona.fechaNac, persona.dni, persona.altura, persona.id))
            self.desconectar()
        except Exception:
            pass

    def get_all_personas_to_list(self):
        """
        Ejercicio 6.
        Obtiene todos los registros de la tabla personas y los almacena en una lista.
        :return: La lista de personas.
        """
        lista = []
        try:
            self.conectar()
            query = "select * from persona"
            self.cur.execute(query)
            lista = list(cur.fetchall())
            self.desconectar()
        except Exception:
            pass
        return lista

    def add_peso(self,persona, peso):
        """
        Ejercicio 8.
        Ingresa un registro en la tabla PersonaPeso, luego de ejecutar validaciones.
        :param persona: Persona de quien se va a insertar un nuevo registro.
        :param peso: Nuevo peso a registrar.
        """
        try:
            persona = self.get_persona_byDNI(persona)
            date = peso.fecha
            #date = datetime.datetime.strptime(fechaIngresada, "%Y-%m-%d")
            if (persona != None):
                self.conectar()
                query = "select * from personapeso where idPersona = %s"
                self.cur.execute(query,(persona.id))
                for row in self.cur.fetchall():
                    if date.Ticks<row[1].Ticks:
                        raise Exception("La persona tiene cargado un peso de una fecha posterior")
                query = "insert into personapeso (idpersona,fecha,peso) values (%s,%s,%s)"
                self.cur.execute(query,(persona.id, peso.fecha, peso.peso))
                self.desconectar()
            else:
                raise Exception("La persona no existe en la base de datos")
        except Exception:
            pass

    def pesos_por_persona(self,persona):
        """
        Ejercicio 10.
        Muestra el historial de registros de pesos de una persona.
        :param persona: Persona sobre la cual se realizara la consulta.
        :return: **********REVISAR*****************
        """
        try:
            persona = self.get_persona_byDNI(persona)
            query = "select * from personapeso where idpersona = %s"
            self.cur = self.conectar()
            self.cur.execute(query,(persona.id))
            historialPesos = list(self.cur.fetchall())
            for row in historialPesos:
                persona.pesos.append(Peso(row[0],row[2],row[1]))
            self.desconectar()
        except Exception:
            pass
        return persona

    def list_persona_pesos(self):
        """
        Lista la informacion de todos los pacientes y sus registros de pesos.
        *** NO FUNCIONA BIEN - REVISAR LA LOGICA ***
        :return:
        """
        personas= []
        try:
            query = "select * from persona left join personapeso on persona.idpersona = personapeso.idpersona"
            self.cur = self.conectar()
            self.cur.execute(query)
            list = self.cur.fetchall()
            self.desconectar()
        except Exception as e:
            print(e)
            pass
        for row in list:
            # Lista con todos los objetos Persona de la base de datos.
            personas.append(Persona(row[1],row[2],row[3],row[4],row[0]))
        for row in list:
            for persona in personas:
                if row[5] == persona.id:
                    persona.pesos.append(Peso(row[6],row[7],row[8]))
        return personas

    def menu(self):
        """
        Interfaz principal del programa, donde se pueden ejecutar todas las consultas
        requeridas en la practica.
        """
        print("**************************MENU*****************************")
        print("1 . Listar personas.")
        print("2 . Insertar persona.")
        print("3 . Eliminar persona.")
        print("4 . Buscar por DNI.")
        print("5 . Actualizar persona.")
        print("6 . Devolver en listas.")
        print("7 . Insertar PersonaPeso y validar.")
        print("8 . Buscar por DNI y mostrar pesos.")
        print("9 . Mostrar todos los registros, por paciente.")
        print()
        opt = int(input("Ingrese una opcion: "))

        if (opt==1):
           self.select_all()
        elif (opt == 2):
            self.insert_row(self.get_persona_from_console())
        elif (opt == 3):
            dni = int(input("Ingrese el dni de la persona a eliminar: "))
            persona = self.get_persona_byDNI(Persona("","",dni,0))
            self.delete_persona(persona)
        elif (opt == 4):
            dni = int(input("Ingrese el dni de la persona a mostrar: "))
            persona = self.get_persona_byDNI(Persona("","",dni,0))
            print("ID Nombre  FechaNac      DNI   Altura")
            print(persona.id, persona.nombre, persona.fechaNac, persona.dni, persona.altura)
        elif (opt == 5):
            dni = int(input("Ingrese el dni de la persona a modificar: "))
            persona_new_data = self.get_persona_from_console()
            persona_new_data.id = self.get_persona_byDNI(Persona("","",dni,0)).id
            self.update_persona(persona_new_data)
        elif (opt == 6):
            self.get_all_personas_to_list()
        elif (opt == 7):
            dni = int(input("Ingrese el numero de documento: "))
            fecha = datetime.datetime.strptime(str(input("Ingrese la fecha del nuevo peso (yyyy-mm-dd): ")), "%Y-%m-%d")
            peso = float(input("Ingrese el peso: "))
            self.add_peso(Persona("","",dni,0),Peso(0,peso, fecha))
        elif (opt == 8):
            dni = int(input("\nIngrese el dni de la persona a listar: "))
            persona = self.pesos_por_persona(Persona("",None,dni,0))
            print("\nID: ", persona.id, "Nombre: ", persona.nombre, "Fecha de Nacimiento: ", persona.fechaNac, "DNI: ", persona.dni, "Altura: ", persona.altura, "\n")
            for i in persona.pesos:
                print("Fecha del registro: ", i.fecha, "Peso registrado: ",i.peso)
        elif (opt == 9):
            personas = self.list_persona_pesos()
            for persona in personas:
                print("ID: ",persona.id, "Nombre: ",persona.nombre, "Fecha de Nac: ",persona.fechaNac, "DNI: ", persona.dni, "Altura: ",persona.altura)
                for peso in persona.pesos:
                    print("Fecha: ",peso.fecha, "Peso: ",peso.peso)
        else:
            self.menu()

practica3 = Practica3()
practica3.menu()
