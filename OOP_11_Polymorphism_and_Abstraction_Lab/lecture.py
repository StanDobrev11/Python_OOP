# class Triangle:
#     def get_triangle_perimeter(self):
#         return "Calculating triangle perimeter"
#
#
# class Square:
#     def get_square_perimeter(self):
#         return "Calculating square perimeter"
#
#
# class Rhombus:
#     def get_rhombus_perimeter(self):
#         return "Calculating rhombus perimeter"
#
#
# shapes = [Triangle(), Square(), Rhombus()]
#
# for shape in shapes:
#     if isinstance(shape, Triangle):
#         print(shape.get_triangle_perimeter())
#     elif isinstance(shape, Square):
#         print(shape.get_square_perimeter())
#     elif isinstance(shape, Rhombus):
#         print(shape.get_rhombus_perimeter())
#     else:
#         print("Unknown shape")

# All of the above are figures. All have perimeter.
# In order to calc for each their perimeter we have to do as per above.

class Shape:
    def get_perimeter(self):
        return "Shape perimeter"


class Triangle(Shape):
    def get_perimeter(self):
        return "Calculating triangle perimeter"


class Square(Shape):
    def get_perimeter(self):
        return "Calculating square perimeter"


class Rhombus(Shape):
    def get_perimeter(self):
        return "Calculating rhombus perimeter"


shapes = [Triangle(), Square(), Rhombus()]
for shape in shapes:
    print(shape.get_perimeter())
