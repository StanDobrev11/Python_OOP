from typing import List

from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms: List[Room] = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def remove_room(self, room: Room):
        self.rooms.remove(room)

    def get_monthly_consumptions(self):
        total_consumption = sum((room.room_cost + room.expenses) for room in self.rooms)
        return f"Monthly consumtion: {total_consumption:.2f}$."

    def pay(self):
        result = []
        for room in list(self.rooms):
            room_total_cost = room.room_cost + room.expenses
            if room.budget >= room_total_cost:
                room.budget -= room_total_cost
                text = f"{room.family_name} paid {room_total_cost:.2f}$ and have {room.budget:.2f}$ left."
            else:
                text = f"{room.family_name} does not have enough budget and must leave the hotel."
                self.remove_room(room)
            result.append(text)

        return '\n'.join(result)

    def status(self):
        total_population = sum(room.members_count for room in self.rooms)
        result_text = f"Total population: {total_population}\n"
        for room in self.rooms:
            result_text += f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n"
            if room.children:
                count = 1
                for child in room.children:
                    result_text += f"--- Child {count} monthly cost: {child.monthly_cost:.2f}$\n"
                    count += 1
            appliances_cost = room.calculate_expenses(room.appliances) * room.members_count
            result_text += f"--- Appliances monthly cost: {appliances_cost:.2f}$\n"
        return result_text.strip()

"""
Monthly consumtions: 1136.00$.
Johnsons paid 242.00$ and have 113.00$ left.
Peterson paid 894.00$ and have 226.00$ left.
Total population: 6
Johnsons with 2 members. Budget: 113.00$, Expenses: 222.00$
--- Appliances monthly cost: 222.00$
Peterson with 4 members. Budget: 226.00$, Expenses: 864.00$
--- Child 1 monthly cost: 270.00$
--- Child 2 monthly cost: 150.00$
--- Appliances monthly cost: 444.00$
"""