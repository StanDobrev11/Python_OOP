from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):
    def __init__(self, name: str, budget_one, budget_two):
        super().__init__(name, budget=budget_one + budget_two, members_count=2)
        self.room_cost = 20
        self.appliances = [TV(), Fridge(), Laptop()]
        self.expenses = self.calculate_expenses(self.appliances)
        self.expenses *= self.members_count
