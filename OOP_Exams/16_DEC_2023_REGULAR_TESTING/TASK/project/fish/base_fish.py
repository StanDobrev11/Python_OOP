from abc import ABC, abstractmethod


class BaseFish(ABC):
    @abstractmethod
    def __init__(self, name: str, points: float, time_to_catch: int):
        self.name = name
        self.points = points
        self.time_to_catch = time_to_catch

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if value.strip() == '':
            raise ValueError("Fish name should be determined!")
        self.__name = value

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, value: float):
        if not 1 <= value <= 10:
            raise ValueError("Points should be a value ranging from 1 to 10!")
        self.__points = value

    @property
    def kind(self):
        return self.__class__.__name__

    def fish_details(self):
        return f"{self.kind}: {self.name} [Points: {self.points}, Time to Catch: {self.time_to_catch} seconds]"
