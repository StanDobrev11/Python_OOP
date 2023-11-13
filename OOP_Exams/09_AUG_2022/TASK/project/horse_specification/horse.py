from abc import ABC, abstractmethod


class Horse(ABC):
    MAX_SPEED = {'Appaloosa': 120, 'Thoroughbred': 140}

    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @property
    @abstractmethod
    def training_gain(self):
        ...

    @property
    def breed(self):
        return self.__class__.name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if len(value) < 4:
            raise ValueError(f"Horse name {value} is less than 4 symbols!")
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > Horse.MAX_SPEED[self.breed]:
            raise ValueError("Horse speed is too high!")
        self.__speed = value

    def train(self):
        if self.speed + self.training_gain > Horse.MAX_SPEED[self.breed]:
            self.speed = Horse.MAX_SPEED[self.breed]
        else:
            self.speed += self.training_gain
