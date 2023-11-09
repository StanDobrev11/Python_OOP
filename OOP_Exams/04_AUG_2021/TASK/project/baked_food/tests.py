import unittest

from project.baked_food.baked_food import BakedFood
from project.baked_food.bread import Bread
from project.baked_food.cake import Cake


class TestFood(unittest.TestCase):
    def setUp(self) -> None:
        self.bread = Bread('diet', 10.50)
        self.cake = Cake('vanilla', 5.30)

    def test_abc_class(self):
        with self.assertRaises(TypeError):
            BakedFood('Cake', 200, 10)

    def test_class_proper_init(self):
        self.assertEqual('diet', self.bread.name)
        self.assertEqual('vanilla', self.cake.name)
        self.assertEqual('Cake', self.cake.type)
        self.assertEqual('Bread', self.bread.type)
        self.assertEqual(200, self.bread.portion)
        self.assertEqual(245, self.cake.portion)

    def test_price_valid(self):
        tests = [-1, 0]
        for x in tests:
            with self.assertRaises(ValueError) as ve:
                self.bread.price = x
                self.cake.price = x
            self.assertEqual("Price cannot be less than or equal to zero!", str(ve.exception))

    def test_name_valid_str(self):
        tests = ['', '    ']
        for x in tests:
            with self.assertRaises(ValueError) as ve:
                self.bread.name = x
                self.cake.name = x
            self.assertEqual("Name cannot be empty string or white space!", str(ve.exception))

    def test_repr_method(self):
        expected = " - diet: 200.00g - 10.50lv"
        actual = self.bread.__repr__()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

vanilla = Cake('Vanilla', 10.30)
choco = Cake('Choco', 7.25)
mixed = Cake('Mixed', 9.90)
diet = Bread('Diet', 5.45)
seeds = Bread('Seeds', 6.76)
fit = Bread('Fit', 10.20)
