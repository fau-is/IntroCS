from oop_shapes import Triangle, Circle, Rectangle


def main():
    circle = Circle(5)
    print(circle.perimeter())

    triangle = Triangle(10, 10, 10)
    print(triangle.area())

    rectangle = Rectangle(10, 10)
    print(rectangle)


if __name__ == "__main__":
    main()
