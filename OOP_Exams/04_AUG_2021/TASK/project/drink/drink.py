from abc import ABC, abstractmethod


class Drink(ABC):
    def __init__(self, name: str, portion: float, price: float, brand: str):
        self.name = name
        self.portion = portion  # size of the drink in milliliters.
        self.price = price
        self.brand = brand

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
    def portion(self) -> float:
        return self.__portion

    @portion.setter
    def portion(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Portion cannot be less than or equal to zero!")
        self.__portion = value

    @property
    def brand(self) -> str:
        return self.__brand

    @brand.setter
    def brand(self, value: str) -> None:
        if value.strip() == "":
            raise ValueError("Name cannot be empty string or white space!")
        self.__brand = value

    def __repr__(self) -> str:
        return f"- {self.name} {self.brand} - {self.portion :.2f}ml - {self.price :.2f}lv"
