from abc import ABC, abstractmethod


class Computer(ABC):
    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.__processor = None
        self.__ram = None
        self.price = None

    @property
    def manufacturer(self) -> str:
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value: str):
        if not value or all(x == ' ' for x in value):
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @property
    def model(self) -> str:
        return self.__model

    @model.setter
    def model(self, value: str):
        if not value or all(x == ' ' for x in value):
            raise ValueError("Model name cannot be empty.")
        self.__model = value

    @abstractmethod
    def configure_computer(self, processor: str, ram: int) -> None:
        ...

    def __repr__(self) -> str:
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
