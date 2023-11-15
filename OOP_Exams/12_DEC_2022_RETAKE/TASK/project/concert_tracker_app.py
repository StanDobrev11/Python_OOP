from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    MUSICIANS = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def __get_musician_by_name(self, name):
        pass

    def __is_musician_name_taken(self, name: str) -> bool:
        """checks if the name is taken"""
        if name in [m.name for m in self.musicians]:
            return True
        return False

    def create_musician(self, musician_type: str, name: str, age: int):
        """The method creates a new musician."""

        if musician_type not in self.MUSICIANS:
            raise ValueError("Invalid musician type!")

        if self.__is_musician_name_taken(name):
            raise Exception(f"{name} is already a musician!")

        musician = self.MUSICIANS[musician_type](name, age)
        self.musicians.append(musician)
        return f"{name} is now a {musician_type}."

    def __is_band_name_taken(self, name: str) -> bool:
        if name in [b.name for b in self.bands]:
            return True
        return False

    def create_band(self, name: str):
        """The method creates a new band."""

        if self.__is_band_name_taken(name):
            raise Exception(f"{name} band is already created!")

        band = Band(name)
        self.bands.append(band)
        return f"{name} was created."
   