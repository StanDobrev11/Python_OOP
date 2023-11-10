from typing import List

from project.planet.planet import Planet


class PlanetRepository:
    def __init__(self):
        self.planets: List[Planet] = []

    def add(self, planet: Planet) -> None:
        """ Adds planet to list """
        if planet not in self.planets:
            self.planets.append(planet)

    def remove(self, planet: Planet) -> None:
        """ Removes planet from list """
        if planet in self.planets:
            self.planets.remove(planet)

    def find_by_name(self, name: str) -> Planet:
        try:
            return [planet for planet in self.planets if planet.name == name][0]
        except IndexError:
            pass
