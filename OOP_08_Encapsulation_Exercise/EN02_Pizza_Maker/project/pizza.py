from typing import Dict
from project.dough import Dough
from project.topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int):
        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings: Dict[Topping.topping_type: Topping.weight] = {}

    def __repr__(self):
        return f"Name: {self.name}, Dough: {self.dough}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if not value:
            raise ValueError("The name cannot be an empty string")
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value: Dough) -> None:
        if not value:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value

    @property
    def max_number_of_toppings(self) -> float:
        return self.__max_number_of_toppings

    @max_number_of_toppings.setter
    def max_number_of_toppings(self, value: float) -> None:
        if value <= 0:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")
        self.__max_number_of_toppings = value

    def add_topping(self, topping: Topping) -> None:
        """Add a new topping to the dictionary if conditions are met"""
        if len(self.toppings) < self.max_number_of_toppings:
            if topping.topping_type in self.toppings:
                self.toppings[topping.topping_type] += topping.weight
            else:
                self.toppings[topping.topping_type] = topping.weight
        else:
            raise ValueError("Not enough space for another topping")

    def calculate_total_weight(self) -> float or int:
        """Returns the total weight of the pizza (dough's weight and toppings' weight)"""
        toppings_weight = sum(weight for weight in self.toppings.values())
        dough_weight = self.dough.weight
        return toppings_weight + dough_weight
