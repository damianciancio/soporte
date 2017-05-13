# conn = pymysql.connect(host='localhost', port=3306, user='root', password='', db='personas') conecccion laboratorio facu

import pymysql
import datetime

def get_persona_from_console():
    nom = str(input("Ingrese un nombre: "))
    fechaNac = str(input("Ingrese fecha de nacimiento(yyyy-mm-dd): "))
    dni = input("Ingrese el documento: ")
    altura = input("Ingrese altura: ")
    return Persona(nom,fechaNac,dni,altura)

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


def conectar():
   global conn, cur
   conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='test')
   cur = conn.cursor()
   return cur

def desconectar():
   conn.commit()
   cur.close()
   conn.close()

def select_all():
    query = "select * from persona"
    try:
        cur = conectar()
        cur.execute(query)
        data = cur.fetchall()
        array = []
        for d in data:
            array.append(Persona(d[1],d[2],d[3],d[4],d[0]))
    except Exception:
        pass
    desconectar()
    return d

def insert_row(persona):
   query = "INSERT INTO persona(nombre, fechaNacimiento, dni, altura) VALUES (%s, %s, %s, %s)"
   try:
        cur = conectar()
        cur.execute(query, (persona.nombre, persona.fechaNac, persona.dni, persona.altura))
        desconectar()
   except Exception:
       pass

def delete_persona(persona):
    try:
        conectar()
        query = "delete from persona where idpersona = %s"
        cur.execute(query, (persona.id))
        desconectar()
    except Exception:
        pass

def get_persona_byDNI(persona):
    found = None
    try:
       conectar()
       query = "select * from persona where dni=%s"
       cur.execute(query, (persona.dni))
       d = cur.fetchone()
       found = Persona(d[1],d[2],d[3],d[4],d[0])
       desconectar()
       return found
    except Exception as exc:
        print(exc)
        pass

def update_persona(persona):
    try:
        conectar()
        query = "update persona set nombre = %s, fechaNacimiento= %s, dni=%s, altura=%s where idpersona = %s"
        cur.execute(query, (persona.nombre , persona.fechaNac, persona.dni, persona.altura, persona.id))
        desconectar()
    except Exception:
        pass

def get_all_personas_to_list():
    lista = []
    try:
        conectar()
        query = "select * from persona"
        cur.execute(query)
        lista = list(cur.fetchall())
        desconectar()
    except Exception:
        pass
    return lista

def add_peso(persona, peso):
    try:
        persona = get_persona_byDNI(persona)
        date = peso.fecha
        #date = datetime.datetime.strptime(fechaIngresada, "%Y-%m-%d")
        if (persona != None):
            conectar()
            query = "select * from personapeso where idPersona = %s"
            cur.execute(query,(persona.id))
            for row in cur.fetchall():
                if date.Ticks<row[1].Ticks:
                    raise Exception("La persona tiene cargado un peso de una fecha posterior")
            query = "insert into personapeso (idpersona,fecha,peso) values (%s,%s,%s)"
            cur.execute(query,(persona.id, peso.fecha, peso.peso))
            desconectar()
        else:
            raise Exception("La persona no existe en la base de datos")
    except Exception:
        pass


def pesos_por_persona(persona):
    try:
        persona = get_persona_byDNI(persona)
        query = "select * from personapeso where idpersona = %s"
        cur = conectar()
        cur.execute(query,(persona.id))
        historialPesos = list(cur.fetchall())
        for row in historialPesos:
            persona.pesos.append(Peso(row[0],row[2],row[1]))
        desconectar()
    except Exception:
        pass
    return persona

def list_persona_pesos():
    personas= []
    try:
        query = "select * from persona left join personapeso on persona.idpersona = personapeso.idpersona"
        cur = conectar()
        cur.execute(query)
        list = []
        list = cur.fetchall()
        for row in list:
            personas.append(Persona(row[1],row[2],row[3],row[4],row[0]))
        for row in list:
            for persona in personas:
                if row[5] == persona.id:
                    persona.pesos.append(Peso(row[5],row[6],row[7]))
    except Exception as e:
        print(e)
        pass
    desconectar()
    return personas

def menu():
   print("***MENU***")
   print("1 . Listar personas.")
   print("2 . Insertar persona.")
   print("3 . Eliminar persona.")
   print("4 . Buscar por DNI.")
   print("5 . Actualizar persona.")
   print("6 . Devolver en listas.")
   print("7 . Insertar PersonaPeso y validar.")
   print("8 . Buscar por DNI y mostrar pesos.")
   print("9 . Devolver todo de todo.")
   print()
   opt = int(input("Ingrese una opcion: "))

   if (opt==1):
       print(select_all())
   elif (opt == 2):
       insert_row(get_persona_from_console())
   elif (opt == 3):
       dni = int(input("Ingrese el dni de la persona a eliminar: "))
       persona = get_persona_byDNI(Persona("","",dni,0))
       delete_persona(persona)
   elif (opt == 4):
       dni = int(input("Ingrese el dni de la persona a mostrar: "))
       persona = get_persona_byDNI(Persona("","",dni,0))
       print("ID Nombre  FechaNac      DNI   Altura")
       print(persona.id, persona.nombre, persona.fechaNac, persona.dni, persona.altura)
   elif (opt == 5):
       dni = int(input("Ingrese el dni de la persona a modificar: "))
       persona_new_data = get_persona_from_console()
       persona_new_data.id = get_persona_byDNI(Persona("","",dni,0)).id
       update_persona(persona_new_data)
   elif (opt == 6):
       print(get_all_personas_to_list())
   elif (opt == 7):
       dni = int(input("Ingrese el numero de documento: "))
       fecha = datetime.datetime.strptime(str(input("Ingrese la fecha del nuevo peso (yyyy-mm-dd): ")), "%Y-%m-%d")
       peso = float(input("Ingrese el peso: "))
       add_peso(Persona("","",dni,0),Peso(0,peso, fecha))
   elif (opt == 8):
       dni = int(input("Ingrese el dni de la persona a listar: "))
       persona = pesos_por_persona(Persona("",None,dni,0))
       print(persona.id, persona.nombre, persona.fechaNac, persona.dni, persona.altura)
       for i in persona.pesos:
           print(i.fecha, i.peso)
   elif (opt == 9):
       personas = list_persona_pesos()
       for persona in personas:
           print(persona.id, persona.nombre, persona.fechaNac, persona.dni, persona.altura)
           for peso in persona.pesos:
               print(peso.fecha, peso.peso)
   else:
       menu()

menu()
