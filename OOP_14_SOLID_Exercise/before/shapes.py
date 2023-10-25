import math
from abc import ABC, abstractmethod


class BasicShapes(ABC):

    @property
    @abstractmethod
    def area(self):
        ...


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2


class AreaCalculator:
    def __init__(self, shapes):
        self.shapes = shapes

    @property
    def shapes(self):
        return self.__shapes

    @shapes.setter
    def shapes(self, value):
        if not isinstance(shapes, list):
            raise AssertionError("`shapes` should be of type `list`.")
        self.__shapes = value

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.area

        return total


shapes = [Rectangle(2, 3), Rectangle(1, 6), Circle(5)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)
