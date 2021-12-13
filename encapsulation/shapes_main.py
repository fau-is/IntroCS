from shapes import Rectangle, Triangle, Circle
import shapes_functions

# Rectangle
rect = Rectangle(10, 5)
rect_area = shapes_functions.area_rectangle(rect.height, rect.width)
rect_peri = shapes_functions.perimeter_rectangle(rect.height, rect.width)
print(f'A rectangle with height: {rect.height} '
      f'and width: {rect.width} has '
      f'the area {rect_area} and perimeter {rect_peri}')


# Triangle
tri = Triangle(10, 10, 10)
tri_area = shapes_functions.area_triangle(tri.side1, tri.side2, tri.side3)
tri_peri = shapes_functions.perimeter_triangle(tri.side1, tri.side2, tri.side3)

print(f'A triangle with the three sides {tri.side1}, '
      f'{tri.side2}, and {tri.side3} has '
      f'the area {tri_area:.2f} and perimeter {tri_peri}')

# Circle
circ = Circle(5)
circ_area = shapes_functions.area_circle(circ.radius)
circ_peri = shapes_functions.perimeter_circle(circ.radius)
print(f'A circle with radius: {circ.radius} has '
      f'the area {circ_area} and perimeter {circ_peri}')



