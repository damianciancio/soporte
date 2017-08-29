from numpy import matrix
from numpy import linalg
import numpy as np

a = matrix([[1,3,-5],[3,4,2],[-5,2,0]])
b = matrix([[1],[5],[3]])


print("Multiplicacion de a * b")
print(a*b) ##multiplicacion de matrices


print("Traspuesta de  b")
print(b.T) ##transpuesta de b

print("Hermitica de b")
print(b.H) ## hermitica de b

print("Inversa de b")
print(a.I) ## inversa de a


print("Resolver ecuaciones lineales")
solucion = linalg.solve(a,b)
print(solucion)


numero_complejo = (1 + 1j) # Defino el número complejo.
print(numero_complejo)     # Lo presento en pantalla.
print(type(numero_complejo))



datos = np.loadtxt('/home/damian/seminario/datos.txt',delimiter=',')
for d in datos:
    print(d)

array1 = np.array([1,5,9])
array2 = np.array([1,2,10])

result = array1 + array2 * 2
result = result * array1
print(result)
