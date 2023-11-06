from typing import List

from project.appliances.appliance import Appliance
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.people.child import Child


class Room:
    def __init__(self, name: str, budget: float, members_count: int):
        self.name = name
        self.budget = budget
        self.members_count = members_count
        self.children: List[Child] = []
        self.expenses = 0
        self.room_cost = 0
        self.appliances = []

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        result = 0
        for element in args:
            for el in element:
                result += el.get_monthly_expense()
        return result
