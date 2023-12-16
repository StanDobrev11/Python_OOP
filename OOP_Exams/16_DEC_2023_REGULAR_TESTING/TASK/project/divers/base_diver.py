from abc import ABC, abstractmethod
from typing import List

from project.fish.base_fish import BaseFish


class BaseDiver(ABC):
    TANK_LVL = {
        'FreeDiver': 120,
        'ScubaDiver': 540
    }

    MISS_RATE = {
        'FreeDiver': 0.6,
        'ScubaDiver': 0.3
    }

    @abstractmethod
    def __init__(self, name: str, oxygen_level: float):
        self.name = name
        self.oxygen_level = oxygen_level
        self.catch: List[BaseFish] = []
        self.competition_points: float = 0
        self.has_health_issue = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if value.strip() == '':
            raise ValueError("Diver name cannot be null or empty!")
        self.__name = value

    @property
    def oxygen_level(self):
        return self.__oxygen_level

    @oxygen_level.setter
    def oxygen_level(self, value: float):
        if value < 0:
            raise ValueError("Cannot create diver with negative oxygen level!")
        self.__oxygen_level = value

    @property
    def competition_points(self):
        return float(f"{self.__competition_points :.1f}")

    @competition_points.setter
    def competition_points(self, value: float):
        self.__competition_points = value

    @property
    def kind(self):
        return self.__class__.__name__

    def miss(self, time_to_catch: int):
        """ Decreases the diver's oxygen_level property. When the method is invoked the diver's oxygen_level is
        decreased by a certain value, that will depend on the fish that is chased. """

        if self.oxygen_level - time_to_catch < 0:
            self.oxygen_level = 0
            self.has_health_issue = True
            return

        self.oxygen_level -= round(time_to_catch * BaseDiver.MISS_RATE[self.kind])

    def renew_oxy(self):
        """	The diver's oxygen_level should be fully replenished to its original value. This would mean
        setting the oxygen_level back to its starting value depending on the diver’s type."""

        self.oxygen_level = BaseDiver.TANK_LVL[self.kind]

    def hit(self, fish: BaseFish):
        """ The method takes a fish parameter. This fish represents the target
        fish that the diver is trying to catch. """

        # check if time required matches oxygen level
        if self.oxygen_level - fish.time_to_catch < 0:
            self.oxygen_level = 0
            return

        # catch fish
        self.oxygen_level -= fish.time_to_catch
        self.competition_points += fish.points
        self.catch.append(fish)

    def update_health_status(self):
        """ Changes the health status of the diver to True, if it is False or reciprocally. """

        self.has_health_issue = not self.has_health_issue

    def __str__(self):

        return (f"{self.kind}: "
                f"[Name: {self.name}, "
                f"Oxygen level left: {self.oxygen_level}, "
                f"Fish caught: {len(self.catch)}, "
                f"Points earned: {self.competition_points}]")
