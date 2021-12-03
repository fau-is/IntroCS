import math


class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width

    def area(self):
        """
        Calculates the area of a rectangle.
        :return: area of a rectangle
        """
        return self.height * self.width

    def perimeter(self):
        """
        Calculates the perimeter of a rectangle
        :return: Perimeter of a rectangle
        """
        return 2 * self.height + 2 * self.width

    def show(self):
        print(f'A rectangle with height: {self.height} '
              f'and width: {self.width} has '
              f'the area {self.area()} and perimeter {self.perimeter()}')

    def __str__(self):
        return f'A rectangle with height: {self.height} ' + \
              f'and width: {self.width} has ' + \
              f'the area {self.area()} and perimeter {self.perimeter()}'


class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        """
        Calculates the area of an triangle
        :return: Area of a triangle
        """
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * ((s - self.side1)
                              * (s - self.side2)
                              * (s - self.side3))
                         )

    def perimeter(self):
        """
        Calculates the perimeter of a triangle
        :return: Perimeter of a triangle
        """
        return self.side1 + self.side2 + self.side3

    def show(self):
        print(f'A triangle with the three sides {self.side1}, '
              f'{self.side2}, and {self.side3} has '
              f'the area {self.area():.2f} and perimeter {self.perimeter()}')


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Calculates the area of a circle
        :return: Area of the circle
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Calculates the perimeter of a circle
        :return: perimeter of a circle
        """
        return 2 * math.pi * self.radius

    def show(self):
        print(f'A circle with radius: {self.radius} has '
              f'the area {self.area():.2f} and perimeter {self.perimeter():.2f}')
