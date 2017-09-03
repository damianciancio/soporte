class Socio:
    def __init__(self, dni, nombre, apellido, id = None):
        self.id = id
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido



    def tienen_mismo_nombre_apellido(self,otroSocio):
        return self.nombre == otroSocio.nombre & self.apellido == otroSocio.apellido
