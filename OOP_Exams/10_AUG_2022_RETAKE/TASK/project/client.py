import re
from typing import List

from project.meals.meal import Meal


class Client:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart: List[Meal] = []  # contain all meals (objects) added by the client
        self.bill: float = 0.0  # the total amount of money for all meals that the client has added to his shopping cart
        self.meal_order = {}

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value: str):
        """ start with "0", 10 characters long, contain only numbers """
        pattern = r"0\d{9}\b"
        if re.fullmatch(pattern, value):
            self.__phone_number = value
        else:
            raise ValueError("Invalid phone number!")

    # def __repr__(self):
    #     return self.phone_number
