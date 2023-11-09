from abc import ABC, abstractmethod


class BakedFood(ABC):
    def __init__(self, name: str, portion: float, price: float):
        self.name = name
        self.portion = portion  # size of the baked food in grams
        self.price = price

    @property
    @abstractmethod
    def type(self):
        ...

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if value.strip() == "":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price cannot be less than or equal to zero!")
        self.__price = value

    def __repr__(self) -> str:
        return f" - {self.name}: {self.portion :.2f}g - {self.price :.2f}lv"
