from abc import ABC, abstractmethod
from typing import List

from project.decoration.base_decoration import BaseDecoration
from project.fish.base_fish import BaseFish


class BaseAquarium(ABC):

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity  # It represents the number of fish an aquarium can have.
        self.decorations: List[BaseDecoration] = []
        self.fish: List[BaseFish] = []

    @property
    @abstractmethod
    def type(self):
        ...

    def calculate_comfort(self):
        """ Returns the sum of each decoration’s comfort in the Aquarium. """
        return sum(decor.comfort for decor in self.decorations)

    def add_fish(self, fish: BaseFish):
        if fish.type not in fish.base_types:
            return f"There isn't a fish of type {fish.type}."

        if fish.aquarium_type != self.type:
            return "Water not suitable."

        current_fish_quantity = len(self.fish)
        if current_fish_quantity < self.capacity:
            self.fish.append(fish)
            return f"Successfully added {fish.type} to {self.name}."

        return "Not enough capacity."

    def remove_fish(self, fish: BaseFish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        text = (f"{self.name}:\n"
                f"Fish: {' '.join(fish.name for fish in self.fish) if self.fish else 'none'}\n"
                f"Decorations: {len(self.decorations)}\n"
                f"Comfort: {self.calculate_comfort()}")
        return text
