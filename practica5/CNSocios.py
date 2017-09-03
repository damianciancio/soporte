from practica5.CDSocios import CDSocios
from practica5.Socio import Socio

class CNSocios():

    max_cantidad_socios = 200

    def alta(self, socio):
        if(self.validar_alta(socio)):
            CDSocios().alta_socio(socio)

    def validar_alta(self,socio):
        condicion = ((not self.existe_socio(socio)) & (not self.llego_al_maximo_de_socios()) & self.validar_nombre_y_apellido(socio)) ##falta validar nombre y apellido
        return condicion

    def validar_modificacion(self, socio):
        return self.validar_nombre_y_apellido(socio)

    def buscar_por_id(self,socio):
        return CDSocios().buscar_por_id(socio.id)

    def buscar_por_dni(self,socio):
        return CDSocios().buscar_por_dni(socio)

    def existe_socio(self, socio):
        encontrado = self.buscar_por_dni(socio)
        condicion =  not encontrado == None
        return condicion

    def llego_al_maximo_de_socios(self):
        condicion = len(CDSocios().buscar_todos()) >= self.max_cantidad_socios
        return condicion

    def validar_nombre_y_apellido(self, socio):
        condicion = not (len(socio.nombre) <= 3 | len(socio.apellido) <= 3 | len(socio.apellido) >= 25 | len(socio.apellido) >= 25)
        return condicion

    def eliminar(self,socio):
        CDSocios().baja_socio(socio)

    def modificar(self,socio):
        if self.validar_modificacion(socio):
            CDSocios().modificar_socio(socio)


    def todos(self):
        return CDSocios().buscar_todos()

socio = Socio(40000005,'Luis', 'Pereyra')
cn = CNSocios()

cn.alta(socio)
