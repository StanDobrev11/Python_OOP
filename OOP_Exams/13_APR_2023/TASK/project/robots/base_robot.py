from abc import ABC, abstractmethod


class BaseRobot(ABC):
    def __init__(self, name: str, kind: str, price: float, weight: int):
        self.name = name
        self.kind = kind
        self.price = price
        self.weight = weight  # the weight in kilograms of the robot

    @property
    @abstractmethod
    def service(self):
        ...

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if value.strip() == '':
            raise ValueError("Robot name cannot be empty!")
        self.__name = value

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, value: str):
        if value.strip() == '':
            raise ValueError("Robot kind cannot be empty!")
        self.__kind = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            raise ValueError("Robot price cannot be less than or equal to 0.0!")
        self.__price = value

    @property
    @abstractmethod
    def weight_gain(self):
        """indicates increase of weight when eating bss type of robot"""
        ...

    def eating(self):
        self.weight += self.weight_gain

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.name}, {self.weight}"
