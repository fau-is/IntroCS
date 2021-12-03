import math


def area(a, b):
    """
    Calculates the area of a rectangle.
    :param a: height
    :param b: width
    :return: area of a rectangle
    """
    return a * b


def perimeter(a, b):
    """
    Calculates the perimeter of a rectangle
    :param a: height
    :param b: width
    :return: Perimeter of a rectangle
    """
    return 2 * a + 2 * b


def area_triangle(side1, side2, side3):
    """
    Calculates the area of an triangle
    :param side1: 1st side of a triangle
    :param side2: 2nd side of a triangle
    :param side3: 3rd side of a triangle
    :return: Area of a triangle
    """
    s = (side1 + side2 + side3) / 2
    return math.sqrt(s * ((s - side1) * (s - side2) * (s - side3)))


def perimeter_triangle(side1, side2, side3):
    """
    Returns the perimeter of a triangle
    :param side1: 1st side of a triangle
    :param side2: 2nd side of a triangle
    :param side3: 3rd side of a triangle
    :return: Perimeter of a triangle
    """
    return side1 + side2 + side3


def area_circle(radius):
    """
    Returns the area of a circle
    :param radius: Radius of the circle
    :return: Area of a circle
    """
    return math.pi * (radius ** 2)


def perimeter_circle(radius):
    """
    Returns the perimeter of a circle
    :param radius: Radius of the circle
    :return: Perimeter of a circle
    """
    return 2 * math.pi * radius
