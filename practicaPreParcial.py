##prueba de parcial de castagnino


def es_primo(numero):
    prueba = range(numero-1,2, -1)
    for n in prueba:
        if(numero % n == 0):
            return False
    return True


print(es_primo(7))


class ordenador():

    def ordenar(self, lista):
        lista.sort()
        return lista

print(ordenador().ordenar([1,9,3,6,4,3]))
