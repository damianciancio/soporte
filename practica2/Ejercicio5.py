from .Ejercicio4 import Estudiante

def buid_dictionary(l):
    dic = {}
    for i in range(len(l)):
        if (l[i].nomCarrera in dic):
            dic[l[i].nomCarrera]+=1
        else:
            dic[l[i].nomCarrera]=1
    return dic

lista = list()
lista.append(Estudiante('Laura',25,"Mujer",89,188,'ISI',2014,50,29))
lista.append(Estudiante('Jose',21,"Hombre",51,170,'IQ',2013,50,13))
lista.append(Estudiante('Brenda',25,"Mujer",61,166,'IQ',2010,50,14))
lista.append(Estudiante('Flor',22,"Mujer",68,188,'IC',2009,50,41))
lista.append(Estudiante('Lucho',32,"Hombre",82,164,'IE',2016,50,4))
lista.append(Estudiante('Nico',20,"Hombre",98,191,'IM',2015,50,11))
lista.append(Estudiante('Marcos',24,"Hombre",93,166,'ISI',2011,50,28))

dic = buid_dictionary(lista)
print(dic)