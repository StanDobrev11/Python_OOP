from typing import List
from project.room import Room


class Hotel:
    def __init__(self, name: str) -> None:
        self.name = name
        self.rooms: List[Room] = []

    @property
    def guests(self):
        return sum(r.guests for r in self.rooms)

    @classmethod
    def from_stars(cls, stars_count: int) -> "Hotel":
        """ Creates a new instance with name '{stars_count} stars Hotel' """
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room) -> None:
        """ Adds the room to the list of rooms """
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int) -> None:
        # the method should have return in order to re-return the original msg composed in the room.take_room method
        room = [r for r in self.rooms if r.number == room_number][0]
        return room.take_room(people)

    def free_room(self, room_number: int) -> None:
        # the method should have return in order to re-return the original msg composed in the room.free_room method
        room = [r for r in self.rooms if r.number == room_number][0]
        return room.free_room()

    def status(self) -> str:
        result = f"Hotel {self.name} has {self.guests} total guests\n"
        result += f"Free rooms: {', '.join(str(r.number) for r in self.rooms if not r.is_taken)}\n"
        result += f"Taken rooms: {', '.join(str(r.number) for r in filter(lambda room: room.is_taken, self.rooms))}"
        return result
