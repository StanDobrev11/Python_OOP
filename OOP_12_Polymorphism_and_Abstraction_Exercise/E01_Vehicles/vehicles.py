from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: int, fuel_consumption: int) -> None:
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: int) -> None:
        """ drive a given distance and reduce fuel as per fuel_consumption * distance driven"""

    @abstractmethod
    def refuel(self, fuel: int) -> None:
        """refuel with a given amount of fuel"""


class Car(Vehicle):
    SUMMER_CONSUMPTION = 0.9

    def drive(self, distance: int) -> None:
        ttl_consumption = (self.fuel_consumption + self.SUMMER_CONSUMPTION) * distance
        if self.fuel_quantity >= ttl_consumption:
            self.fuel_quantity -= ttl_consumption

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    SUMMER_CONSUMPTION = 1.6
    FUEL_LOST_DUE_TO_PUNCTURE = 0.05

    def drive(self, distance: int) -> None:
        ttl_consumption = (self.fuel_consumption + self.SUMMER_CONSUMPTION) * distance
        if self.fuel_quantity >= ttl_consumption:
            self.fuel_quantity -= ttl_consumption

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel - fuel * self.FUEL_LOST_DUE_TO_PUNCTURE
