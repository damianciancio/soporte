class Socio:
    id = None
    dni = None
    nombre = None
    apellido = None

    def __init__(self, dni, nombre, apellido, id = None):
        self.id = id
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
