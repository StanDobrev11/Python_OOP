from typing import List

from project.astronaut.astronaut import Astronaut


class AstronautRepository:
    def __init__(self):
        self.astronauts: List[Astronaut] = []

    def add(self, astronaut: Astronaut) -> str:
        """ Adds astronaut to the list """
        if astronaut not in self.astronauts:
            self.astronauts.append(astronaut)
            return f"Successfully added {astronaut.type}: {astronaut.name}."
        else:
            return f"{astronaut.name} is already added."

    def remove(self, astronaut: Astronaut):
        """ Removes astronaut from the list """
        if astronaut in self.astronauts:
            self.astronauts.remove(astronaut)
            return f"Astronaut {astronaut.name} was retired!"

    def find_by_name(self, name: str) -> Astronaut:
        try:
            return [astro for astro in self.astronauts if astro.name == name][0]
        except IndexError:
            raise Exception(f"Astronaut {name} doesn't exist!")

    def select_for_mission(self):
        filtered_astro = [astro for astro in self.astronauts if astro.oxygen > 30]
        if filtered_astro:
            return sorted(filtered_astro, reverse=True)[:5]
        else:
            raise Exception("You need at least one astronaut to explore the planet!")
