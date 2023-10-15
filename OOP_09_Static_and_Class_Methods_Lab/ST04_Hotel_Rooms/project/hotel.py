from typing import List
from project.room import Room


class Hotel:
    def __init__(self, name: str) -> None:
        self.name = name
        self.rooms: List[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int) -> "Hotel":
        """ Creates a new instance with name '{stars_count} stars Hotel' """
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room) -> None:
        """ Adds the room to the list of rooms """
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int) -> None:
        room = [r for r in self.rooms if r.number == room_number][0]
        room.take_room(people)
        self.add_guests(room)

    def free_room(self, room_number: int) -> None:
        room = [r for r in self.rooms if r.number == room_number][0]
        self.remove_guests(room)
        room.free_room()

    def add_guests(self, room: Room) -> None:
        self.guests += room.guests

    def remove_guests(self, room: Room) -> None:
        self.guests -= room.guests

    def status(self) -> str:
        result = f"Hotel {self.name} has {self.guests} total guests\n"
        result += f"Free rooms: {', '.join(str(r.number) for r in self.rooms if not r.is_taken)}\n"
        result += f"Taken rooms: {', '.join(str(r.number) for r in self.rooms if r.is_taken)}"
        return result
