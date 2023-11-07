import unittest

from project.people.child import Child
from project.rooms.alone_old import AloneOld
from project.rooms.alone_young import AloneYoung
from project.rooms.old_couple import OldCouple
from project.rooms.room import Room
from project.rooms.young_couple import YoungCouple
from project.rooms.young_couple_with_children import YoungCoupleWithChildren


class TestRoom(unittest.TestCase):
    def setUp(self) -> None:
        self.room = Room('test', 100, 2)

    def test_proper_init(self):
        self.assertEqual('test', self.room.name)
        self.assertEqual(100, self.room.budget)
        self.assertEqual(2, self.room.members_count)
        self.assertEqual([], self.room.children)
        self.assertEqual([], self.room.appliances)
        self.assertEqual(0, self.room.expenses)
        self.assertEqual(0, self.room.room_cost)

    def test_expenses_negative_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.room.expenses = -5
        self.assertEqual("Expenses cannot be negative", str(ve.exception))

    def test_calculate_expenses_returns_zero(self):
        actual = self.room.calculate_expenses()
        self.assertEqual(0, actual)


class TestAloneOld(unittest.TestCase):
    def setUp(self) -> None:
        self.room = AloneOld('TestOld', 100)

    def test_proper_init(self):
        self.assertEqual(1, self.room.members_count)
        self.assertEqual(10, self.room.room_cost)
        self.assertEqual(0, self.room.expenses)

    def test_calculate_expenses_returns_zero(self):
        actual = self.room.calculate_expenses()
        self.assertEqual(0, actual)


class TestAloneYoung(unittest.TestCase):
    def setUp(self) -> None:
        self.room = AloneYoung('TestYoung', 100)

    def test_proper_init(self):
        self.assertEqual(1, self.room.members_count)
        self.assertEqual(10, self.room.room_cost)
        self.assertEqual(1, len(self.room.appliances))
        self.assertEqual(45, self.room.expenses)


class TestOldCouple(unittest.TestCase):
    def setUp(self) -> None:
        self.room = OldCouple('Test', 100, 150)

    def test_proper_init(self):
        self.assertEqual('Test', self.room.name)
        self.assertEqual(15, self.room.room_cost)
        self.assertEqual(250, self.room.budget)
        self.assertEqual(2, self.room.members_count)
        self.assertEqual(3, len(self.room.appliances))
        self.assertEqual(204, self.room.expenses)


class TestYoungCouple(unittest.TestCase):
    def setUp(self) -> None:
        self.room = YoungCouple('Test', 100, 150)

    def test_proper_init(self):
        self.assertEqual('Test', self.room.name)
        self.assertEqual(20, self.room.room_cost)
        self.assertEqual(250, self.room.budget)
        self.assertEqual(2, self.room.members_count)
        self.assertEqual(3, len(self.room.appliances))
        self.assertEqual(222, self.room.expenses)


class TestYoungCoupleWithChildren(unittest.TestCase):
    def setUp(self) -> None:
        child1 = Child(5, 1, 2, 1)
        child2 = Child(3, 2)
        child3 = Child(0, 0)
        self.room = YoungCoupleWithChildren('Test', 100, 150, child1, child2, child3)

    def test_proper_init(self):
        self.assertEqual('Test', self.room.name)
        self.assertEqual(30, self.room.room_cost)
        self.assertEqual(250, self.room.budget)
        self.assertEqual(5, self.room.members_count)
        self.assertEqual(3, len(self.room.children))
        self.assertEqual(3, len(self.room.appliances))

    def test_proper_expenses_for_appliances_for_one_person(self):
        actual = self.room.calculate_expenses(self.room.appliances)
        self.assertEqual(111, actual)

    def test_proper_children_monthly_cost(self):
        actual = self.room.calculate_expenses(self.room.children)
        self.assertEqual(420, actual)

    def test_proper_expenses_attribute_appliances_for_all_members_and_child_care(self):
        self.assertEqual(975, self.room.expenses)

    def test_no_children(self):
        room = YoungCoupleWithChildren('Test', 100, 150)
        self.assertEqual(2, room.members_count)
        self.assertEqual([], room.children)
        self.assertEqual(0, room.calculate_expenses(room.children))
        self.assertEqual(222, room.expenses)


if __name__ == '__main__':
    unittest.main()
