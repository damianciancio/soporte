from practica4.CDSocios import CDSocios

class CNSocios():

    max_cantidad_socios = 200

    def alta(self, socio):
        if(not self.existe_socio(self, socio)):
            CDSocios().alta(socio)

    def validar_alta(self,socio):
        return ((not self.existe_socio(socio.dni)) & (not self.llego_al_maximo_de_socios())) ##falta validar nombre y apellido

    def existe_socio(self, socio):
        return (CDSocios().contarDNI(socio.dni) > 0)

    def llego_al_maximo_de_socios(self):
        return CDSocios().buscar_todos().count() < self.max_cantidad_socios

    def eliminar(self,socio):
        CDSocios().baja(socio)

    def modificar(self,socio):
        CDSocios().modificacion(socio)##falta validar


    def todos(self):
        return CDSocios().buscar_todos()


