class Rectangulo:

    def __init__(self,b,a):
        self.base = b
        self.altura = a

    def area(self):
        return (self.base * self.altura)


rect = Rectangulo(3,2)
print (rect.area())