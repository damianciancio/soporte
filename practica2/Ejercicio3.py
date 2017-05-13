from random import randint

class Persona:
    def generar_dni(self):
        rand = randint(10000000, 99999999)
        return rand

    def __init__(self, nom, edad, sexo, peso, alt):
        self.nombre = nom
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.altura = alt
        self.dni = self.generar_dni()

    def es_mayor_de_edad(self):
        return self.edad > 18

    def print_data(self):
        print('Nombre:', self.nombre)
        print('Edad:', self.edad)
        print('Sexo:', self.sexo)
        print('Peso:', self.peso)
        print('Altura:', self.altura)
        print('DNI (aleatorio):', self.dni)


if __name__ == '__main__':
    print('Repositorio de informacon de una persona.')

    nom = input('Ingrese nombre ')
    edad = input('Ingrese edad ')
    while True:
        sexo = input("Ingrese sexo (H/M): ")
        if (sexo.lower() == "h"):
            sexo = "Hombre"
            break
        elif (sexo.lower() == "m"):
            sexo = "Mujer"
            break
    peso = input('Ingrese peso ')
    alt = input('Ingrese altura ')

    persona = Persona(nom,edad,sexo,peso,alt)
    persona.print_data()


""" def ingresar_sexo(self):
        print('Ingrese su sexo H/M: ')
        inp = input()
        if (inp == 'H' or inp == 'h'):
            self.sexo = 'Hombre'
        elif (inp == 'M' or inp == 'm'):
            self.sexo = 'Mujer'
        else:
            print('Opcion no valida, ingrese H o M:', self.ingresar_sexo())"""

