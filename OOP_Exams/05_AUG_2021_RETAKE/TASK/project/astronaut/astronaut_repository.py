from typing import List

from project.astronaut.astronaut import Astronaut


class AstronautRepository:
    def __init__(self):
        self.astronauts: List[Astronaut] = []

    def add(self, astronaut: Astronaut) -> None:
        """ Adds astronaut to the list """
        if astronaut not in self.astronauts:
            self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        """ Removes astronaut from the list """
        if astronaut in self.astronauts:
            self.astronauts.remove(astronaut)

    def find_by_name(self, name: str) -> Astronaut:
        try:
            return [astro for astro in self.astronauts if astro.name == name][0]
        except IndexError:
            pass
