from typing import List

from project.appliances.appliance import Appliance
from project.people.child import Child


class Room:
    def __init__(self, name: str, budget: float, members_count: int):
        self.name = name
        self.budget = budget
        self.members_count = members_count
        self.children: List[Child] = []
        self.appliances: List[Appliance] = []
        self.expenses = 0
        self.room_cost = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    @staticmethod
    def calculate_expenses(*args):
        return sum(obj.monthly_cost for lst in args for obj in lst)
