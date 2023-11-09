from typing import List

from project.aquarium.base_aquarium import BaseAquarium
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    base_aquariums = {"FreshwaterAquarium": FreshwaterAquarium, "SaltwaterAquarium": SaltwaterAquarium, }
    base_decorations = {'Ornament': Ornament, 'Plant': Plant}
    base_fish = {'FreshwaterFish': FreshwaterFish, 'SaltwaterFish': SaltwaterFish}

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

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium = self.get_aquarium_by_name(aquarium_name)
        if aquarium:
            try:
                decor = [decor for decor in self.decorations_repository.decorations if decor.type == decoration_type][0]
            except IndexError:
                return
            aquarium.add_decoration(decor)  # add decoration to given aquarium
            self.decorations_repository.decorations.remove(decor)  # remove decoration from repository
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        aquarium = self.get_aquarium_by_name(aquarium_name)
        if aquarium:
            if fish_type in self.base_fish:
                fish = self.base_fish[fish_type](fish_name, fish_species, price)
                return aquarium.add_fish(fish)
            else:
                return f"There isn't a fish of type {fish_type}."

    def feed_fish(self, aquarium_name: str):
        aquarium = self.get_aquarium_by_name(aquarium_name)
        if aquarium:
            aquarium.feed()
            return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        """Calculates the value of the aquarium with the given name.
        It is calculated by the sum of all fish’s and decorations’ prices in the aquarium."""
        aquarium = self.get_aquarium_by_name(aquarium_name)
        if aquarium:
            fish_value = sum(fish.price for fish in aquarium.fish)
            decor_value = sum(decor.price for decor in aquarium.decorations)
            return f"The value of Aquarium {aquarium_name} is {fish_value + decor_value :.2f}."

    def report(self):
        result_string = ''
        for aquarium in self.aquariums:
            result_string += aquarium.__str__() + '\n'

        return result_string.strip()

    def get_aquarium_by_name(self, aquarium_name: str):
        try:
            return [aquarium for aquarium in self.aquariums if aquarium.name == aquarium_name][0]
        except IndexError:
            return
