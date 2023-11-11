from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken: bool = False  # One car can be driven by ONLY one driver.

    @property
    @abstractmethod
    def min_speed(self):
        """ defines min speed range of a car """
        ...

    @property
    @abstractmethod
    def max_speed(self):
        """ defines max speed range of a car """
        ...

    @property
    def type(self):
        return self.__class__.__name__

    @property
    def model(self) -> str:
        return self.__model

    @model.setter
    def model(self, value):
        if len(value) < 4:  # model less than 4 symbols
            raise ValueError(f"Model {value} is less than 4 symbols!")
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value: int):
        if value not in range(self.min_speed, self.max_speed + 1):
            raise ValueError(f"Invalid speed limit! Must be between {self.min_speed} and {self.max_speed}!")
        self.__speed_limit = value

    def assign_driver(self):
        self.is_taken = True

    def remove_driver(self):
        self.is_taken = False
