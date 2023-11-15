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
        return [m for m in self.musicians if m.name == name][0]

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

    def __get_band_by_name(self, name):
        return [b for b in self.bands if b.name == name][0]

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

    def __is_concert_place_taken(self, place: str) -> bool:
        if place in [c.place for c in self.concerts]:
            return True
        return False

    def __get_concert_by_place(self, place: str):
        return [c for c in self.concerts if c.place == place][0]

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        """Creates concert"""

        if self.__is_concert_place_taken(place):
            concert = self.__get_concert_by_place(place)
            raise Exception(f"{place} is already registered for {concert.genre} concert!")

        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        """The method adds a musician to the band."""
        try:
            musician = self.__get_musician_by_name(musician_name)
        except IndexError:
            raise Exception(f"{musician_name} isn't a musician!")

        try:
            band = self.__get_band_by_name(band_name)
        except IndexError:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."
