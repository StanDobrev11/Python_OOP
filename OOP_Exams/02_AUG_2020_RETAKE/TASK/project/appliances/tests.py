import unittest

from project.appliances.appliance import Appliance
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.stove import Stove
from project.appliances.tv import TV


class TestAppliance(unittest.TestCase):
    def setUp(self) -> None:
        self.appliance = Appliance(5)

    def test_proper_init_method(self):
        self.assertEqual(5, self.appliance.cost)

    def test_proper_monthly_cost_calculation(self):
        self.assertEqual(150, self.appliance.monthly_cost)

    def test_tv_monthly_cost(self):
        test = TV()
        self.assertEqual(45, test.monthly_cost)

    def test_fridge_monthly_cost(self):
        test = Fridge()
        self.assertEqual(36, test.monthly_cost)

    def test_stove_monthly_cost(self):
        test = Stove()
        self.assertEqual(21, test.monthly_cost)

    def test_laptop_monthly_cost(self):
        test = Laptop()
        self.assertEqual(30, test.monthly_cost)


if __name__ == '__main__':
    unittest.main()
