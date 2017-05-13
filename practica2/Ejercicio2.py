import math

class Circulo:

    def __init__(self,r):
        self.radio = r

    def area(self):
        return (math.pi * math.pow(self.radio,2))

    def perim(self):
        return (2 * math.pi * self.radio)

circ = Circulo(5)

#Dos formas diferentes de mostrar los resultados.
print("El area del circulo es %.2f" % (circ.area()))
print("El perimetro del circulo es {}".format(round(circ.perim(),2)))
