
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def get_area(self):
        return (self.radius)**2 * math.pi

    def get_perimeter(self):
        return self.radius *2 * math.pi


x = Circle(int(input('Ingrese area del circulo: ')))
print(x.get_area())
print(x.get_perimeter())
