from typing import List

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    BREEDS = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}

    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def get_last_added_free_horse(self, breed: str):
        try:
            return [h for h in self.horses if h.breed == breed and not h.is_taken][-1]
        except IndexError:
            return False

    def get_existing_horse(self, name: str):
        try:
            return [h for h in self.horses if h.name == name][0]
        except IndexError:
            return False

    def get_existing_jockey(self, name: str):
        try:
            return [j for j in self.jockeys if j.name == name][0]
        except IndexError:
            return False

    def add_horse(self, breed: str, name: str, speed: int):
        """ The method creates a horse and adds it to the horses' list. """
        if breed not in HorseRaceApp.BREEDS:
            return

        if self.get_existing_horse(name):
            raise Exception(f"Horse {name} has been already added!")

        self.horses.append(HorseRaceApp.BREEDS[breed](name, speed))
        return f"{breed} horse {name} is added."

    def add_jockey(self, name: str, age: int):
        """ The method creates a jockey and adds it to the jockeys' list. """

        if self.get_existing_jockey(name):
            raise Exception(f"Jockey {name} has been already added!")

        self.jockeys.append(Jockey(name, age))
        return f"Jockey {name} is added."

    def create_horse_race(self, race_type: str):
        """ The method creates a race and adds it to the horse races' list. """

        try:
            if [r for r in self.horse_races if r.race_type == race_type][0]:
                raise Exception(f"Race {race_type} has been already created!")
        except IndexError:
            self.horse_races.append(HorseRace(race_type))
            return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, breed: str):
        """ Sets the last horse added from the given horse type to the jockey with the given name if they both exist."""

        if not self.get_existing_jockey(jockey_name):
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not self.get_last_added_free_horse(breed):
            raise Exception(f"Horse breed {breed} could not be found!")

        jockey = self.get_existing_jockey(jockey_name)
        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        horse = self.get_last_added_free_horse(breed)
        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."


if __name__ == '__main__':
    h = HorseRaceApp()
    print(h.create_horse_race('Winter'))
    print(h.create_horse_race('Winter'))
    print(h.add_horse('Appaloosa', 'konche', 120))
    print(h.add_horse('Thoghbred', 'konche', 101))
