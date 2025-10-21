from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    radius = 0
    def __init__(self, r):
        self.radius = r
    def calculate_perimeter(self):
        perimeter = 2*3.14*self.radius
        print(f'the perimeter of this circle is {perimeter}')

    def calculate_area(self):
        area = 3.14*self.radius**2
        print(f'The area of this circle is:{area}')

circulo_1 = Circle(5)
circulo_1.calculate_perimeter()
circulo_1.calculate_area()

class Square(Shape):
    side = 0

    def __init__(self,side):
        self.side = side

    def calculate_perimeter(self):
        perimeter = self.side*4
        print(f'the perimeter of this Square is {perimeter}')

    def calculate_area(self):
        area = self.side*self.side
        print(f'The area of this Square is:{area}')

square_1 = Square(5)
square_1.calculate_area()
square_1.calculate_perimeter()

class Rectangle(Shape):
    lenght = 0
    height = 0

    def __init__(self,l,h):
        self.lenght = l
        self.height= h

    def calculate_perimeter(self):
        perimeter = self.lenght*2+self.height*2
        print(f'the perimeter of this Rectangle is {perimeter}')

    def calculate_area(self):
        area = self.lenght*self.height
        print(f'The area of this Rectangle is:{area}')

rectangle_1 = Rectangle(5,10)
rectangle_1.calculate_area()
rectangle_1.calculate_perimeter()