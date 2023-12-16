from abc import ABC, abstractmethod


class BaseClimber(ABC):
    MINIMUM_STRENGTH = {
        'ArcticClimber': 100,
        'SummitClimber': 75,
    }

    @abstractmethod
    def __init__(self, name: str, strength: float):
        self.name = name
        self.strength = strength
        self.conquered_peaks = []
        self.is_prepared: bool = True

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if value.strip() == '':
            raise ValueError("Climber name cannot be null or empty!")
        self.__name = value

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, value: float):
        if value < 0:
            raise ValueError("Climber cannot have negative strength!")
        self.__strength = value

    @property
    def climber_type(self):
        return self.__class__.__name__

    def can_climb(self):
        """ The method checks whether the climber has enough strength required to attempt a climb """

        return True if self.strength >= self.MINIMUM_STRENGTH[self.climber_type] else False

    @abstractmethod
    def climb(self, peak):
        pass

    def rest(self):
        self.strength += 15

    def __str__(self):
        return (f"{self.climber_type}: /// Climber name: {self.name} * Left strength: {self.strength :.1f} * "
                f"Conquered peaks: {', '.join(peak for peak in self.conquered_peaks)} ///")
