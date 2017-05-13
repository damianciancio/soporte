import random

class Persona:
    def __init__(self, name, age, sex, weight, height):
        self.name = name
        self.age = age
        self.sex = sex
        self.weight = weight
        self.height = height
        self.dni = self.generar_dni()

    def es_mayor_edad(self):
        return (self.age) >= 18

    def print_data(self):
        print(self.name, self.age, self.sex, self.weight, self.height, self.dni)

    def generar_dni(self):
        return random.randint(10000000, 99999999)
