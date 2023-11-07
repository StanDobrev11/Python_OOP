from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    def __init__(self, name: str, budget_one, budget_two):
        super().__init__(name, budget=budget_one + budget_two, members_count=2)
        self.room_cost = 15
        self.appliances = [TV(), Fridge(), Stove()]
        self.expenses = self.calculate_expenses(self.appliances)
        self.expenses *= self.members_count
