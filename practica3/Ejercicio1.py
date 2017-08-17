import pymysql
import datetime

#<editor-fold desc="Clases que representan las entidades de la BDD">
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

def conectar():
    """
    Conecta a la base de datos especificada en conn.
    :return: Un cursor apuntando a la base de datos.
    """
    global conn, cur
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='test')
    #[conexion laboratorio facu] conn = pymysql.connect(host='localhost', port=3306, user='root', password='', db='personas')
    cur = conn.cursor()
    return cur

def desconectar():
    """
    Cierra la conexion a la base de datos.
    """
    conn.commit()
    cur.close()
    conn.close()

def get_persona_from_console():
    """
    Crea un objeto Persona a partir de informacion ingresada por el usuario.
    :return: El objeto Persona creado.
    """
    nom = str(input("Ingrese un nombre: "))
    fechaNac = str(input("Ingrese fecha de nacimiento(yyyy-mm-dd): "))
    dni = input("Ingrese el documento: ")
    altura = input("Ingrese altura: ")
    return Persona(nom,fechaNac,dni,altura)

def select_all():
    """
    Busca todos los elementos de la tabla personas, los mapea a objetos y los almacena en un arreglo.
    :return: El arreglo con todas las personas.
    """
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
    """
    Ejercicio 2.
    Inserta en la base de datos una persona.
    :param persona: La persona a ingresar a la base de datos.
    """
    query = "INSERT INTO persona(nombre, fechaNacimiento, dni, altura) VALUES (%s, %s, %s, %s)"
    try:
        cur = conectar()
        cur.execute(query, (persona.nombre, persona.fechaNac, persona.dni, persona.altura))
        desconectar()
    except Exception:
        pass

def delete_persona(persona):
    """
    Ejercicio 3.
    Elimina de la base de datos una persona.
    :param persona: La persona a eliminar de la base de datos.
    """
    try:
        conectar()
        query = "delete from persona where idpersona = %s"
        cur.execute(query, (persona.id))
        desconectar()
    except Exception:
        pass

def get_persona_byDNI(persona):
    """
    Ejercicio 4.
    Buscar en la base de datos una persona segun su DNI.
    :param persona: La persona a buscar segun su DNI.
    :return: La persona encontrada.
    """
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
    """
    Ejercicio 5.
    Buscar en la base de datos una persona y actualizar su informacion. Luego imprime esos datos.
    :param persona: Persona con los datos actualizados, para ingresar a la base de datos.
    :return: 
    """
    try:
        conectar()
        query = "update persona set nombre = %s, fechaNacimiento= %s, dni=%s, altura=%s where idpersona = %s"
        cur.execute(query, (persona.nombre , persona.fechaNac, persona.dni, persona.altura, persona.id))
        desconectar()
        print("Datos de la persona: %s, %s, %s, %s", persona.nombre,persona.fechaNac, persona.dni, persona.altura)
    except Exception:
        pass

def get_all_personas_to_list():
    """
    Ejercicio 6.
    Obtiene todos los registros de la tabla personas y los almacena en una lista.
    :return: La lista de personas.
    """
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
    """
    Ejercicio 8.
    Ingresa un registro en la tabla PersonaPeso, luego de ejecutar validaciones.
    :param persona: Persona de quien se va a insertar un nuevo registro.
    :param peso: Nuevo peso a registrar.
    """
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
    """
    Ejercicio 10.
    Muestra el historial de registros de pesos de una persona.
    :param persona: Persona sobre la cual se realizara la consulta.
    :return: **********REVISAR*****************
    """
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
    """
    ******************REVISAR****************
    :return: 
    """
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
    """
    Interfaz principal del programa, donde se pueden ejecutar todas las consultas
    requeridas por la practica.
    """
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
