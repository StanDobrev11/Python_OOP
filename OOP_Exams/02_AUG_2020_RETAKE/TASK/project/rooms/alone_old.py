from project.rooms.room import Room


class AloneOld(Room):
    def __init__(self, name: str, budget):
        super().__init__(name, budget, members_count=1)
        self.room_cost = 10
