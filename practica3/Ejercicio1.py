import pymysql
import datetime

def conectar():
   global conn, cur
   conn = pymysql.connect(host='localhost', port=3306, user='root', password='', db='personas')
   cur = conn.cursor()
   return cur

def desconectar():
   conn.commit()
   cur.close()
   conn.close()

def selectAll():
   query = "select * from persona"
   cur = conectar()
   cur.execute(query)

   data = cur.fetchall()
   print("Nombre   FechaNac   DNI   Altura")
   for d in data:
       print(d[1],d[2], d[3], d[4])
   desconectar()

def insertRow():
   nom = str(input("Ingrese un nombre: "))
   fechaNac = str(input("Ingrese fecha de nacimiento(yyyy-mm-dd): "))
   dni = input("Ingrese el documento: ")
   altura = input("Ingrese altura: ")
   query = "INSERT INTO persona(nombre, fechaNacimiento, dni, altura) VALUES (%s, %s, %s, %s)"
   cur = conectar()
   cur.execute(query, (nom, fechaNac, dni, altura))
   desconectar()

def delete_persona(persona):
   conectar()
   query = "delete from persona where idpersona = %s"
   cur.execute(query, (persona[0]))
   desconectar()

def getPersonaByDNIstring(dni):
   conectar()
   query = "select * from persona where dni=%s"
   cur.execute(query, (dni))
   persona = cur.fetchone()
   desconectar()
   return persona

def update_persona(persona):
   conectar()
   query = "update persona set nombre = %s, fechaNacimiento= %s, dni=%s, altura=%s where idpersona = %s"
   cur.execute(query, (persona[1] + 'asd', persona[2], persona[3], persona[4], persona[0]))
   desconectar()
   getPersonaByDNIstring(persona[3])

def get_all_personas_to_list():
   conectar()
   query = "select * from persona"
   cur.execute(query)
   lista = list(cur.fetchall())
   for row in lista:
       print(row)
   desconectar()

def add_peso(dni, fechaIngresada, peso):
   persona = getPersonaByDNIstring(dni)
   date = datetime.datetime.strptime(fechaIngresada, "%Y-%m-%d")
   if (persona != None):
       print("Persona existe")
       conectar()
       query = "select * from personapeso where idPersona = %s"
       cur.execute(query,(persona[0]))
       for row in cur.fetchall():
           if date.Ticks<row[1].Ticks:
               print("Fecha atrasada")
               return
       query = "insert into personapeso (idpersona,fecha,peso) values (%s,%s,%s)"
       cur.execute(query,(persona[0], fechaIngresada, peso))
       desconectar()
   else:
       print("No existe la persona")

def pesosPorPersona(dni):
   persona = getPersonaByDNIstring(dni)
   query = "select * from personapeso where idpersona = %s"
   cur = conectar()
   cur.execute(query,(persona[0]))
   historialPesos = list(cur.fetchall())
   print("ID Nombre  FechaNac      DNI   Altura")
   print(persona[0], persona[1], persona[2], persona[3], persona[4])
   print()
   print("Fecha       Peso")
   for row in historialPesos:
       print(row[1],row[2])
   desconectar()

def listPersonasPesos():
   query = "select * from persona left join personapeso on persona.idpersona = personapeso.idpersona"
   cur = conectar()
   cur.execute(query)
   personas= []
   for per in cur.fetchall():
       personas.append(per)
   desconectar()
   return personas


###    data = cur.fetchall()
###    print("Nombre   FechaNac   DNI   Peso")
###    for d in data:
###        print(d[1],d[2], d[3], d[4], d[5], d[6], d[7])



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
       selectAll()
       menu()
   elif (opt == 2):
       insertRow()
   elif (opt == 3):
       dni = int(input("Ingrese el dni de la persona a eliminar: "))
       persona = getPersonaByDNIstring(dni)
       print("Se elimino la siguiente persona: ")
       print(persona)
       delete_persona(persona)
   elif (opt == 4):
       dni = int(input("Ingrese el dni de la persona a mostrar: "))
       persona = getPersonaByDNIstring(dni)
       print("ID Nombre  FechaNac      DNI   Altura")
       print(persona[0], persona[1], persona[2], persona[3], persona[4])
   elif (opt == 5):
       dni = int(input("Ingrese el dni de la persona a modificar: "))
       persona = getPersonaByDNIstring(dni)
       update_persona(persona)
   elif (opt == 6):
       get_all_personas_to_list()
   elif (opt == 7):
       dni = int(input("Ingrese el numero de documento: "))
       fecha = str(input("Ingrese la fecha del nuevo peso (yyyy/mm/dd): "))
       peso = float(input("Ingrese el peso: "))
       add_peso(dni,fecha, peso)
   elif (opt == 8):
       dni = int(input("Ingrese el dni de la persona a listar: "))
       pesosPorPersona(dni)
   elif (opt == 9):
       personas = listPersonasPesos()
       for row in personas:
           print(row)
   else:
       menu()

menu()

