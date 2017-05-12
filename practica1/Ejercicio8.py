def superposicion(lista1, lista2):
    for i in range(0,len(lista1)):
        for j in range(0, len(lista2)):
            if lista1[i] == lista2[j]:
                return True
    return False

lista1=[1,2,3]
lista2=[4,5,6]
print(superposicion(lista1, lista2))
