import scipy as sp                  # Importamos scipy como el alias sp
import matplotlib.pyplot as plt     # Importamos matplotlib.pyplot como el alias plt

# Creamos un polinomio
polinomio = [1.3,4,.6,-1]   # polinomio = 1.3 x^3 + 4 x^2 + 0.6 x - 1

# Creamos un array dimensional
x = sp.arange(-4,1,.05)

#  Evaluamos el polinomio en x mediante polyval.
y = sp.polyval(polinomio,x)

# Calculamos las raices del polinomio
raices = sp.roots(polinomio)

# Evaluamos el polinomio en las raices
s = sp.polyval(polinomio,raices)

# Las presentamos en pantalla
print ("Las raices son %2.2f, %2.2f, %2.2f. " % (raices[0], raices[1], raices[2]))

# Creamos la figura
plt.figure

# Dibujamos
plt.plot(x,y,'-', label = 'y(x)')

# Dibujamos en la figura anterior
plt.hold('on')

# Dibujamos
plt.plot(raices.real,s.real,'ro', label = 'Raices del polinomio')

# Etiquetas
plt.xlabel('x')
plt.ylabel('y')
plt.title(u'Cálculo de las raices de un polinomio')

# Leyenda
plt.legend()

# Mostramos la figura en pantalla
plt.show()
