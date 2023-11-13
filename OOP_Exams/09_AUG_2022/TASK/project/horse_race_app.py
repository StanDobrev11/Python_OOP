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

        if race_type in [r.race_type for r in self.horse_races]:
            raise Exception(f"Race {race_type} has been already created!")

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

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        """Adds a jockey (object) to the given horse race type (if they both exist).
        A jockey can only participate in a horse race if he has a horse."""

        try:
            race = [r for r in self.horse_races if r.race_type == race_type][0]
        except IndexError:
            raise Exception(f"Race {race_type} could not be found!")

        jockey = self.get_existing_jockey(jockey_name)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey_name in [j.name for j in race.jockeys]:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        try:
            race = [r for r in self.horse_races if r.race_type == race_type][0]
        except IndexError:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = max(race.jockeys)

        return f"The winner of the {race_type} race, with a speed of {winner.horse.speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."
