import unittest

from project.everland import Everland
from project.people.child import Child
from project.rooms.alone_old import AloneOld
from project.rooms.alone_young import AloneYoung
from project.rooms.old_couple import OldCouple
from project.rooms.young_couple import YoungCouple
from project.rooms.young_couple_with_children import YoungCoupleWithChildren


class TestEverland(unittest.TestCase):
    def setUp(self) -> None:
        self.everland = Everland()
        self.young_single = AloneYoung('Johny', 10)
        self.old_single = AloneOld('James', 10)
        self.old_couple = OldCouple("Oldees", 200, 120)
        self.young_couple = YoungCouple("Johnsons", 200, 205)
        child1 = Child(5, 1, 2, 1)
        child2 = Child(3, 2)
        self.young_couple_with_children = YoungCoupleWithChildren("Peterson", 700, 520, child1, child2)

    def test_proper_init(self):
        self.assertEqual([], self.everland.rooms)

    def test_add_room_adds_room(self):
        self.everland.add_room(self.young_single)
        self.assertEqual(1, len(self.everland.rooms))

    def test_remove_room_removes_room(self):
        self.everland.add_room(self.young_single)
        self.everland.add_room(self.old_single)

        self.assertEqual(2, len(self.everland.rooms))

        self.everland.remove_room(self.young_single)

        self.assertEqual(1, len(self.everland.rooms))
        self.assertEqual(self.old_single, self.everland.rooms[0])

    def test_get_monthly_consumption_proper_value(self):
        self.everland.add_room(self.young_single)  # room cost 10, appliances expenses 45
        self.everland.add_room(self.old_couple)  # room cost 15, appliances expenses 204
        self.assertEqual("Monthly consumption: 274.00$.", self.everland.get_monthly_consumptions())

    def test_get_monthly_consumption_no_rooms(self):
        self.assertEqual("Monthly consumption: 0.00$.", self.everland.get_monthly_consumptions())

    def test_pay_two_rooms_budget_is_enough(self):
        self.everland.add_room(AloneYoung('room_1', 60))  # room cost 10, appliances expenses 45
        self.everland.add_room(OldCouple('room_2', 120, 120))  # room cost 15, appliances expenses 204
        expected = "room_1 paid 55.00$ and have 5.00$ left.\nroom_2 paid 219.00$ and have 21.00$ left."
        actual = self.everland.pay()
        self.assertEqual(expected, actual)

    def test_pay_two_rooms_budget_not_enough(self):
        test_1 = AloneYoung('room_1', 55)
        self.everland.add_room(test_1)  # room cost 10, appliances expenses 45
        self.everland.add_room(OldCouple('room_2', 100, 100))  # room cost 15, appliances expenses 204
        expected = "room_1 paid 55.00$ and have 0.00$ left.\nroom_2 does not have enough budget and must leave the hotel."
        actual = self.everland.pay()
        self.assertEqual(expected, actual)
        self.assertEqual(test_1, self.everland.rooms[0])

    def test_pay_no_rooms(self):
        self.assertEqual('', self.everland.pay())

    def test_status_no_rooms(self):
        self.assertEqual("Total population: 0\n", self.everland.status())


if __name__ == '__main__':
    unittest.main()
