from __future__ import division

#----------------------------------------------------------------------
# Nombre:       ejemplo_matplotlib_grafica_superficie3d.py
# PropÃ³sito:    Aprender como leer una image y representar una grafica en 3D.
#
# Origen:        Propio .
# Autor:         JosÃ© MarÃ­a Herrera-Fernandez
#
# CreaciÃ³n:        18 de Septiembre de 2013
# Historia:
#
# Dependencias:    scipy, mpl_toolkits, matplotlib, numpy
# Licencia:        GPL
#----------------------------------------------------------------------


"""
DescripciÃ³n: Ejemplo de cÃ³mo usar la funciÃ³n integrate para realizar integrales
numÃ©ricas en python.
"""



from mpl_toolkits.mplot3d import Axes3D         # Cargo Axes3D de mpl_toolkits.mplot3d
from scipy.misc import imread                   # Cargo imread de scipy.misc
import numpy as np                              # Cargo numpy como el aliaas np
import matplotlib.pyplot as plt                 # Cargo matplotlib.pyplot  en el alias sp

# Leo una imagen y la almaceno en imagen_superficial
imagen_superficial = imread('/home/damian/seminario/fondo.jpg')

# Creo una figura
plt.figure()

# Muestro la imagen en pantalla
plt.imshow(imagen_superficial)

# AÃ±ado etiquetas
plt.title('Imagen que usaremos de superficie')
plt.xlabel(u'# de pÃ­xeles')
plt.ylabel(u'# de pÃ­xeles')

# Creo otra figura y la almaceno en figura_3d
figura_3d = plt.figure()

# Indicamos que vamos a representar en 3D
ax = figura_3d.gca(projection = '3d')

# Creamos los arrays dimensionales de la misma dimensiÃ³n que imagen_superficial
X = np.linspace(-5, 5, imagen_superficial.shape[0])
Y = np.linspace(-5, 5, imagen_superficial.shape[1])

# Obtenemos las coordenadas a partir de los arrays creados
X, Y = np.meshgrid(X, Y)

# Defino la funciÃ³n que deseo representar
R = np.sqrt(X ** 2 + Y ** 2)
Z = np.sin(R)

# Reescalamos de RGB a [0-1]
imagen_superficial = imagen_superficial.swapaxes(0, 1) / 255.

# meshgrid orienta los ejes al revÃ©s luego hay que voltear
ax.plot_surface(X, Y, Z, facecolors = np.flipud(imagen_superficial))

# Fijamos la posiciÃ³n inicial de la grafica
ax.view_init(45, -35)

# AÃ±adimos etiquetas
plt.title(u'Imagen sobre una grafica 3D')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
# Mostramos en pantalla
plt.show()
