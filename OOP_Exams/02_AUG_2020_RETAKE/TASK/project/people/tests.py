import unittest

from project.people.child import Child


class TestChild(unittest.TestCase):
    def setUp(self) -> None:
        self.child = Child(10, 1, 2, 3)
        self.child_2 = Child(10)

    def test_proper_init(self):
        self.assertEqual(16, self.child.cost)

    def test_cost_without_toys(self):
        self.assertEqual(10, self.child_2.cost)

    def test_monthly_cost_with_toys(self):
        self.assertEqual(480, self.child.monthly_cost)

    def test_monthly_cost_without_toys(self):
        self.assertEqual(300, self.child_2.monthly_cost)


if __name__ == '__main__':
    unittest.main()
