from abc import ABC, abstractmethod


class BasePeak(ABC):
    RECOMMENDED_GEAR = {
        'ArcticPeak': ["Ice axe", "Crampons", "Insulated clothing", "Helmet"],
        'SummitPeak': ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"],
    }

    def __init__(self, name: str, elevation: int):
        self.name = name
        self.elevation = elevation
        self.difficulty_level = self.calculate_difficulty_level()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if len(value) < 2:
            raise ValueError("Peak name cannot be less than 2 symbols!")
        self.__name = value

    @property
    def summit_type(self):
        return self.__class__.__name__

    def get_recommended_gear(self):
        """ Returns a list of recommended gear.
        Keep in mind that each type of peak has specific requirements for the gear. """

        return self.RECOMMENDED_GEAR[self.summit_type]

    @abstractmethod
    def calculate_difficulty_level(self):
        """ Returns the difficulty level depending on the peak's elevation.
        Keep in mind that each type of peak can implement the method differently. """
        ...
