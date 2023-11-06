from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    def __init__(self, family_name: str, pension_one, pension_two):
        super().__init__(name=family_name, budget=pension_one + pension_two, members_count=2)
        self.room_cost = 15
        self.appliances = [TV(), Fridge(), Stove()]
        self.expenses = (self.calculate_expenses(self.appliances))
        self.expenses *= self.members_count
