from abc import ABC, abstractmethod


class Meal(ABC):

    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price  # price per one piece of a meal
        self.quantity = quantity  # quantity to be ordered for that meal

    @property
    def type(self):
        return self.__class__.__name__

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if value == '':
            raise ValueError("Name cannot be an empty string!")
        self.__name = value

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            raise ValueError("Invalid price!")
        self.__price = value

    @abstractmethod
    def details(self):
        ...


class Meall(Meal):

    def details(self):
        pass
