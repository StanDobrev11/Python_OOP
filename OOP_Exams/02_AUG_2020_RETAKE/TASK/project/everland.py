from typing import List

from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms: List[Room] = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = sum((room.room_cost + room.expenses) for room in self.rooms)
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        result = []
        for room in self.rooms:
            room_total_cost = room.room_cost + room.expenses
            if room.budget >= room_total_cost:
                room.budget -= room_total_cost
                text = f"{room.name} paid {room_total_cost:.2f}$ and have {room.budget:.2f}$ left."
            else:
                text = f"{room.name} does not have enough budget and must leave the hotel."
                self.rooms.remove(room)
            result.append(text)

        return '\n'.join(result)

    def status(self):
        total_population = sum(room.members_count for room in self.rooms)
        result_text = f"Total population: {total_population}\n"
        for room in self.rooms:
            result_text += f"{room.name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses + room.room_cost:.2f}$)\n"
            if room.children:
                count = 1
                for child in room.children:
                    result_text += f"--- Child {count} monthly cost: {child.monthly_cost:.2f}$\n"
                    count += 1
            if room.appliances:
                result_text += f"‐‐‐ Appliances monthly cost: {room.expenses:.2f}\n"
        return result_text
