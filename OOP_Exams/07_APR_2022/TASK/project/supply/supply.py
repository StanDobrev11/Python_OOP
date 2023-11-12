from abc import ABC, abstractmethod


class Supply(ABC):
    @abstractmethod
    def __init__(self, name: str, energy: int):
        self.name = name
        self.energy = energy

    @property
    def type(self):
        return self.__class__.__name__

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if value.strip() == '':
            raise ValueError("Name cannot be an empty string.")
        self.__name = value

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value: int):
        if value < 0:
            raise ValueError("Energy cannot be less than zero.")
        self.__energy = value

    def details(self) -> str:
        return f"{self.type}: {self.name}, {self.energy}"
