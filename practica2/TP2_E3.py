from .persona import Persona

p = Persona(input('Ingrese nombre: '), int(input('Ingrese edad: ')), input('Ingrese sexo: '), float(input('Ingrese peso: ')), float(input('Ingrese altura: ')))
if p.es_mayor_edad() :
    print('Es mayor de edad')
else :
    print('Es menor de edad')
p.print_data()
