from scipy import integrate
import scipy as sp
import math
import matplotlib.pyplot as plt
from scipy import interpolate

#calculo de integrales

limite_inferior = 0
limite_superior = math.inf
exponencial_decreciente = lambda x: sp.exp(-x)

print ('La integral entre %2.2f y  %2.2f es '% (limite_inferior, limite_superior))
print(integrate.quad(exponencial_decreciente,limite_inferior,limite_superior))


## Interpolación

x = sp.linspace(0,3,30)

y = sp.exp(-x/3.0)

interpolacion = interpolate.interp1d(x,y)

x2 = sp.linspace(0,3,100)

y2 = interpolacion(x2)


plt.figure

plt.plot(x, y, 'o',x2,y2,'-')

plt.legend(('Datos conocidos', 'Datos experimentales'))

plt.xlabel('Eje x')
plt.ylabel('Eje y')

plt.show()


