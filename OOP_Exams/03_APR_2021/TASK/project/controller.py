from typing import List

from project.aquarium.base_aquarium import BaseAquarium
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant


class Controller:
    base_aquariums = {"FreshwaterAquarium": FreshwaterAquarium, "SaltwaterAquarium": SaltwaterAquarium, }
    base_decorations = {'Ornament': Ornament, 'Plant': Plant}

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums: List[BaseAquarium] = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in self.base_aquariums:
            return "Invalid aquarium type."

        self.aquariums.append(self.base_aquariums[aquarium_type](aquarium_name))
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in self.base_decorations:
            return "Invalid decoration type."

        self.decorations_repository.add(self.base_decorations[decoration_type]())
        return f"Successfully added {decoration_type}."
