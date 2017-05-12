def es_polindromo():
    cadena = input("Ingrese texto: ")
    i = len(cadena) - 1
    cad = ''
    for letra in cadena :
        cad = cad + cadena[i]
        i=i-1
    return cadena == cad

if (es_polindromo()) :
    print("Es polindromo")
else :
    print("No es polindromo")