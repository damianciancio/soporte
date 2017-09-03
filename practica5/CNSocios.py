from practica5.CDSocios import CDSocios
from practica5.Socio import Socio

class CNSocios():

    max_cantidad_socios = 200

    def alta(self, socio):
        if(self.validar_alta(socio)):
            try:
                CDSocios().alta_socio(socio)
            except Exception as e:
                raise e

    def validar_alta(self,socio):
        condicion = ((not self.existe_socio(socio)) & (not self.llego_al_maximo_de_socios()) & self.validar_nombre_y_apellido(socio)) ##falta validar nombre y apellido
        return condicion

    def validar_modificacion(self, socio):
        return self.validar_nombre_y_apellido(socio)

    def buscar_por_id(self,socio):
        try:
            return CDSocios().buscar_por_id(socio.id)
        except Exception as e:
            raise e

    def buscar_por_dni(self,socio):
        try:
            return CDSocios().buscar_por_dni(socio)
        except Exception as e:
            raise e

    def existe_socio(self, socio):
        encontrado = self.buscar_por_dni(socio)
        condicion =  not encontrado == None
        return condicion

    def llego_al_maximo_de_socios(self):
        condicion = len(CDSocios().buscar_todos()) >= self.max_cantidad_socios
        return condicion

    def validar_nombre_y_apellido(self, socio):
        longitud = len(socio.nombre)
        condicion = ((len(socio.nombre) >= 3) & (len(socio.nombre) <= 25)) & ((len(socio.apellido) >= 3) & (len(socio.apellido) <= 25))
        return condicion

    def eliminar(self,socio):
        try:
            CDSocios().baja_socio(socio)
        except Exception as e:
            raise e

    def modificar(self,socio):
        if self.validar_modificacion(socio):
            CDSocios().modificar_socio(socio)


    def todos(self):
        try:
            return CDSocios().buscar_todos()
        except Exception as e:
            raise e
