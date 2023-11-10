from abc import ABC, abstractmethod
from typing import List


class Astronaut(ABC):
    @abstractmethod
    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack: List = []

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if value.strip() == '':
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    @property
    def oxygen_consumption(self):
        """ Required oxygen units while breathing. Specific for each type of astronaut. """
        return 10  # default value for oxygen consumption

    @property
    def oxygen(self) -> int:
        return self.__oxygen

    @oxygen.setter
    def oxygen(self, value: int) -> None:
        self.__oxygen = value

    def breathe(self) -> None:
        """ Each time an astronaut takes a breath, their oxygen decreases. """
        self.oxygen -= self.oxygen_consumption

    def increase_oxygen(self, amount: int) -> None:
        """ Increases the oxygen with the given amount. """
        self.oxygen += amount
