import datetime

from Practica2.persona import Persona


class Estudiante(Persona):
    nombre_carrera = ''
    año_ingreso = 0
    cantidad_materias_carrera = 0
    cantidad_materias_aprobadas = 0

    def __init__(self,name,age,sex,weight,height,nombre_carrera = "Sistemas", año_ingreso = 2014, cantidad_materias_carrera = 50, cantidad_materias_aprobadas = 20):
        Persona.__init__(self, name,age,sex,weight,height)
        self.nombre_carrera = nombre_carrera
        self.año_ingreso = año_ingreso
        self.cantidad_materias_carrera = cantidad_materias_carrera
        self.cantidad_materias_aprobadas = cantidad_materias_aprobadas

    def avance(self):
        return self.cantidad_materias_aprobadas * 100 / self.cantidad_materias_carrera

    def edad_ingreso(self):
        x = datetime.datetime.now()
        return self.age - (int(x.year) - self.año_ingreso)
