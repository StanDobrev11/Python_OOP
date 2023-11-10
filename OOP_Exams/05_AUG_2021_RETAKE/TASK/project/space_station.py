from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    ASTRONAUTS = {"Biologist": Biologist, "Geodesist": Geodesist, "Meteorologist": Meteorologist}

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.mission_success = 0
        self.mission_failed = 0
    def add_astronaut(self, astronaut_type: str, name: str) -> str:
        if astronaut_type in self.ASTRONAUTS:
            astro = self.ASTRONAUTS[astronaut_type](name)
            return self.astronaut_repository.add(astro)
        else:
            raise Exception("Astronaut type is not valid!")

    def add_planet(self, name: str, items: str) -> str:  # "item 1, item 2, ... "
        planet = Planet(name)
        planet.add_items(items)
        return self.planet_repository.add(planet)

    def retire_astronaut(self, name: str):
        astro = self.astronaut_repository.find_by_name(name)
        return self.astronaut_repository.remove(astro)

    def recharge_oxygen(self):
        for astro in self.astronaut_repository.astronauts:
            astro.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        astronauts = self.astronaut_repository.select_for_mission()

        for astronaut in astronauts:
            astronaut.explore(planet)

            if planet.is_explored:
                self.mission_success += 1
                return f"Planet: {planet_name} was explored. {len(astronauts)} astronauts participated in collecting items."
        else:
            self.mission_failed += 1
            return "Mission is not completed."

    def report(self):
        text = (f"{self.mission_success} successful missions!\n"
                f"{self.mission_failed} missions were not completed!\n"
                f"Astronauts' info:\n")

        for astro in self.astronaut_repository.astronauts:
            text += astro.__repr__()
            text += '\n'

        return text.strip()

