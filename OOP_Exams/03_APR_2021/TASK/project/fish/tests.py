import unittest

from project.fish.base_fish import BaseFish
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class TestFish(unittest.TestCase):

    def test_fish_abc(self):
        with self.assertRaises(TypeError) as te:
            f = BaseFish('test', 'species', 5, 5)
        expected = "Can't instantiate abstract class BaseFish with abstract methods aquarium_type, eat, type"
        self.assertEqual(expected, str(te.exception))

    def test_freshwater_fish_init(self):
        fish = FreshwaterFish('test', 'fresh', 10)
        self.assertEqual('test', fish.name)
        self.assertEqual('fresh', fish.species)
        self.assertEqual(10, fish.price)
        self.assertEqual(3, fish.size)
        self.assertEqual('FreshwaterAquarium', fish.aquarium_type)

    def test_name_empty_raises_value_error(self):
        fish = FreshwaterFish('test', 'fresh', 10)
        with self.assertRaises(ValueError) as ve:
            fish.name = ''
        self.assertEqual("Fish name cannot be an empty string.", str(ve.exception))

    def test_species_empty_raises_value_error(self):
        fish = FreshwaterFish('test', 'fresh', 10)
        with self.assertRaises(ValueError) as ve:
            fish.species = ''
        self.assertEqual("Fish species cannot be an empty string.", str(ve.exception))

    def test_price_below_equals_zero(self):
        fish = FreshwaterFish('test', 'fresh', 10)
        test_range = [-1, 0]
        for x in test_range:
            with self.assertRaises(ValueError) as ve:
                fish.price = x
            self.assertEqual("Price cannot be equal to or below zero.", str(ve.exception))

    def test_freshwater_fish_eat_increase_size(self):
        fish = FreshwaterFish('test', 'fresh', 10)
        fish.eat()
        self.assertEqual(6, fish.size)

    def test_saltwater_fish_init(self):
        fish = SaltwaterFish('test', 'salt', 10)
        self.assertEqual('test', fish.name)
        self.assertEqual('salt', fish.species)
        self.assertEqual(10, fish.price)
        self.assertEqual(5, fish.size)
        self.assertEqual('SaltwaterAquarium', fish.aquarium_type)

    def test_saltwater_fish_eat_increase_size(self):
        fish = SaltwaterFish('test', 'salt', 10)
        fish.eat()
        self.assertEqual(7, fish.size)

if __name__ == '__main__':
    unittest.main()