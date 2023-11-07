from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, name: str, budget_one, budget_two, *children):
        super().__init__(name, budget=budget_one + budget_two, members_count=2 + len(children))
        self.room_cost = 30
        self.appliances = [TV(), Fridge(), Laptop()]
        self.children = [child for child in children]
        self.expenses = self.calculate_expenses(self.appliances)
        self.expenses *= self.members_count
        self.expenses += self.calculate_expenses(self.children)
