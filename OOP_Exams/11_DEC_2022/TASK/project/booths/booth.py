from abc import ABC, abstractmethod
from typing import List

from project.delicacies.delicacy import Delicacy


class Booth(ABC):
    def __init__(self, booth_number: int, capacity: int):
        self.booth_number = booth_number
        self.capacity = capacity
        self.delicacy_orders: List[Delicacy] = []
        self.price_for_reservation = 0  # Each time a booth is reserved, the price for a reservation should be set.
        self.is_reserved: bool = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value: int):
        if value < 0:
            raise ValueError("Capacity cannot be a negative number!")
        self.__capacity = value

    @property
    @abstractmethod
    def price_per_person(self):
        ...

    def reserve(self, number_of_people: int):
        """ Reserves the booth depending on each booth type """
        if not self.is_reserved:
            self.price_for_reservation = number_of_people * self.price_per_person
            self.is_reserved = True
