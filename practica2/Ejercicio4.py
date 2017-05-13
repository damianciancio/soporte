from .Ejercicio3 import Persona

import datetime

class Estudiante(Persona):
    def __init__(self, nom, edad, sexo, peso, alt, nomCar, anIng, cantMat, cantMatApr):
        super(Estudiante,self).__init__(nom, edad, sexo, peso, alt)
        self.nomCarrera = nomCar
        self.añoIngreso = anIng
        self.cantMaterias = cantMat
        self.cantMateriasAprobadas = cantMatApr

    def avance(self):
        print("Has avanzado un ", (100 * self.cantMateriasAprobadas / self.cantMaterias), "% de la carrera.")

    def edad_ingreso(self):
        print("Cuando ingresaste tenias %s años" % (self.edad - (datetime.datetime.now().year - self.añoIngreso)))


if __name__ == '__main__':
    print('Repositorio de informacon de un estudiante.')

    nom = input('Ingrese nombre ')
    edad = (int(input('Ingrese edad ')))
    while True:
        sexo = input("Ingrese sexo (H/M): ")
        if (sexo.lower() == "h"):
            sexo = "Hombre"
            break
        elif (sexo.lower() == "m"):
            sexo = "Mujer"
            break
    peso = (int(input('Ingrese peso ')))
    alt = (int(input('Ingrese altura ')))
    nomCar = input('Ingrese Nombre de la Carrera ')
    anIng = (int(input('Ingrese Año de ingreso ')))
    cantMat = (int(input('Ingrese Cantidad de materias ')))
    cantMatAp = (int(input('Ingrese Cantidad de materias aprobadas ')))
    estudiante = Estudiante(nom, edad, sexo, peso, alt, nomCar, anIng, cantMat, cantMatAp)

    estudiante.avance()
    estudiante.edad_ingreso()
