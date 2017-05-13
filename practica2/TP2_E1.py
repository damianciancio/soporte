class Rectangle:
    def __init__(self, alto, ancho):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return (self.alto*self.ancho)

r = Rectangle(int(input('Ingrese ancho: ')), int(input('Ingrese alto: ')))
print(r.area())
