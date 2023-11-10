from abc import ABC, abstractmethod
from typing import List

from project.planet.planet import Planet


class Astronaut(ABC):
    @abstractmethod
    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack: List = []

    @property
    def type(self):
        return self.__class__.__name__

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

    def __repr__(self):
        return f"Name: {self.name}\nOxygen: {self.oxygen}\nBackpack items: {', '.join(self.backpack) if self.backpack else 'none'}"

    def __gt__(self, other):
        return self.oxygen > other.oxygen

    def breathe(self) -> None:
        """ Each time an astronaut takes a breath, their oxygen decreases. """
        self.oxygen -= self.oxygen_consumption

    def explore(self, planet: Planet):
        while self.oxygen > 0:
            try:
                item = planet.items.pop()  # takes item found on planet
                self.backpack.append(item)  # places item in backpack
                self.breathe()  # takes a breath when finds item and reduces oxygen
            except IndexError:
                break

            if not planet.items:
                planet.is_explored = True

    def increase_oxygen(self, amount: int) -> None:
        """ Increases the oxygen with the given amount. """
        self.oxygen += amount
