def es_vocal(a, vocales):
    return (a in vocales)

if (es_vocal(a=input("Ingrese caracter: "), vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])):
    print("Es vocal")
else:
    print("Es consonante")