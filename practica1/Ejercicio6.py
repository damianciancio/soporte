def inversa():
    cadena = input("Ingrese texto: ")
    i = len(cadena) - 1
    cad = ''
    for letra in cadena :
        cad = cad + cadena[i]
        i=i-1
    return cad

print(inversa())