from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    MUSICIANS = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}

    # SKILL_SET = {
    #     "Rock": {
    #         "Drummer": ["play the drums with drumsticks"],
    #         "Singer": ["sing high pitch notes"],
    #         "Guitarist": ["play rock"]
    #     },
    #
    #     'Metal': {
    #         "Drummer": ["play the drums with drumsticks"],
    #         "Singer": ["sing low pitch notes"],
    #         "Guitarist": ["play metal"]
    #     },
    #     "Jazz": {
    #         "Drummer": ["play the drums with drum brushes"],
    #         "Singer": ["sing high pitch notes", "sing low pitch notes"],
    #         "Guitarist": ["play jazz"]
    #     }
    # }
    SKILL_SET = {
        "Rock": [
            "play the drums with drumsticks",
            "sing high pitch notes",
            "play rock"
        ],
        'Metal': [
            "play the drums with drumsticks",
            "sing low pitch notes",
            "play metal"
        ],
        "Jazz": [
            "play the drums with drum brushes",
            "sing high pitch notes",
            "sing low pitch notes",
            "play jazz"
        ]
    }

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

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        """The method removes a musician from the band."""

        try:
            band = self.__get_band_by_name(band_name)
        except IndexError:
            raise Exception(f"{band_name} isn't a band!")

        try:
            musician = [m for m in band.members if m.name == musician_name][0]
        except IndexError:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def __is_band_ready(self, band: Band):
        """checks if the band has at least 1 member of each musician type"""
        for kind in self.MUSICIANS.keys():
            if kind not in [type(member).__name__ for member in band.members]:
                return False
        return True

    # def __can_band_perform_genre(self, band: Band, genre: str):
    #     required_skills = set(self.SKILL_SET[genre])
    #     band_skills = {skill for musician in band.members for skill in musician.skills}
    #
    #     return all(skill in band_skills for skill in required_skills)

    def __can_band_perform_genre(self, band: Band, genre: str):
        required_skills = set(self.SKILL_SET[genre])
        band_skills = set(skill for musician in band.members for skill in musician.skills)
        return required_skills.issubset(band_skills)

    # def __can_band_perform_genre(self, band: Band, genre: str):
    #     skills_needed = self.SKILL_SET[genre]
    #     for musician_type, skills in skills_needed.items():
    #         for member in band.members:
    #             if type(member).__name__ == musician_type:
    #                 for skill in skills:
    #                     if skill not in member.skills:
    #                         return False
    #     return True

    def start_concert(self, concert_place: str, band_name: str):
        """The method is to start a concert at the given place with the given band.
        The concert place and the band name will always be valid.
        However, there are some rules for the band to start a concert depending on the band
        members and the concert type"""

        band = self.__get_band_by_name(band_name)
        concert = self.__get_concert_by_place(concert_place)

        if not self.__is_band_ready(band):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if not self.__can_band_perform_genre(band, concert.genre):
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = concert.audience * concert.ticket_price - concert.expenses
        return f"{band_name} gained {profit :.2f}$ from the {concert.genre} concert in {concert.place}."
