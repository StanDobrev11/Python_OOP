from abc import ABC, abstractmethod
from typing import List

from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink


class Table(ABC):
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders: List[BakedFood] = []
        self.drink_order: List[Drink] = []
        self.number_of_people: int = 0
        self.is_reserved: bool = False

    @property
    @abstractmethod
    def type(self) -> str:
        ...

    @property
    def capacity(self) -> int:
        return self.__capacity

    @capacity.setter
    def capacity(self, value: int) -> None:
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0!")
        self.__capacity = value

    def reserve(self, number_of_people: int) -> None:
        """Reserves the table with the count of people given."""
        self.number_of_people = number_of_people
        self.is_reserved = True

    def order_food(self, baked_food: BakedFood) -> None:
        """Orders the provided food."""
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink) -> None:
        """Orders the provided drink."""
        self.drink_order.append(drink)

    def get_bill(self):
        """Returns the bill for all the ordered drinks and food."""
        food_bill = sum(food.price for food in self.food_orders)
        drink_bill = sum(drink.price for drink in self.drink_order)
        return food_bill + drink_bill

    def clear(self) -> None:
        """Removes all the ordered drinks and food and finally frees the seats at the table."""
        self.food_orders = []
        self.drink_order = []
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self) -> str:
        """If the table is free, returns a string"""
        if not self.is_reserved:
            return f"Table: {self.table_number}\nType: {self.type}\nCapacity: {self.capacity}"
