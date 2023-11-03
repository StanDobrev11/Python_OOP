from abc import ABC, abstractmethod


class Computer(ABC):
    _processors_prices = {}
    _ram_prices = {}

    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    @abstractmethod
    def type(self):
        ...

    @property
    def processor(self):
        return self.__processor

    @processor.setter
    def processor(self, value):
        if value not in self.__class__._processors_prices and value is not None:
            raise ValueError(f"{value} is not compatible with {self.type} {self.manufacturer} {self.model}!")
        self.__processor = value

    @property
    def ram(self):
        return self.__ram

    @ram.setter
    def ram(self, value):
        if value not in self.__class__._ram_prices and value is not None:
            raise ValueError(f"{value}GB RAM is not compatible with {self.type} {self.manufacturer} {self.model}!")
        self.__ram = value

    @property
    def manufacturer(self) -> str:
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value: str):
        # if value.strip() == "" -> better solution
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

    def update_price(self):
        self.price = self.__class__._processors_prices[self.processor] + self.__class__._ram_prices[self.ram]

    def configure_computer(self, processor: str, ram: int):
        self.processor = processor
        self.ram = ram
        self.update_price()
        return f"Created {self} for {self.price}$."

    def __repr__(self) -> str:
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
