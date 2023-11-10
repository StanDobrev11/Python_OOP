from typing import List

from project.planet.planet import Planet


class PlanetRepository:
    def __init__(self):
        self.planets: List[Planet] = []

    def add(self, planet: Planet) -> str:
        """ Adds planet to list """
        if any(planet.name == pl.name for pl in self.planets):
            return f"{planet.name} is already added."

        self.planets.append(planet)
        return f"Successfully added Planet: {planet.name}."

    def remove(self, planet: Planet) -> None:
        """ Removes planet from list """
        if any(planet.name == pl.name for pl in self.planets):
            self.planets.remove(planet)

        # if planet in self.planets:
        #     self.planets.remove(planet)

    def find_by_name(self, name: str) -> Planet:
        try:
            return [planet for planet in self.planets if planet.name == name][0]
        except IndexError:
            raise Exception("Invalid planet name!")
