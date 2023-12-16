class Rectangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return self.a * 2 + self.b * 2


rectangle = Rectangle(5, 5)
print(rectangle.area())
print(rectangle.perimeter())
