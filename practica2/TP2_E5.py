from .estudiante import Estudiante
lista = []
for estudiante in range(3):
    a = Estudiante('asd', 12, 'm', 123, 34, input('Carrera',))
    lista.append(a)

def diccionario(lista):
    dic = {}
    for l in lista:
        if l.nombre_carrera in dic :
            dic[l.nombre_carrera]=dic[l.nombre_carrera]+1
        else :
            dic[l.nombre_carrera] = 1
    return dic

print(diccionario(lista))
