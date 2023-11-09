import unittest

from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish


class TestAquarium(unittest.TestCase):
    def setUp(self) -> None:
        self.test = FreshwaterAquarium('fresh')

    def test_add_decoration(self):
        for _ in range(3):
            self.test.add_decoration(Ornament())
        self.assertEqual(3, len(self.test.decorations))

    def test_calculate_comfort(self):
        for _ in range(3):
            self.test.add_decoration(Ornament())
        self.assertEqual(3, self.test.calculate_comfort())

    def test_add_fish_valid_fish_enough_capacity(self):
        self.test.capacity = 1
        self.assertEqual([], self.test.fish)
        fish = FreshwaterFish('fish', 'freshwater', 10)
        expected = "Successfully added FreshwaterFish to fresh."
        actual = self.test.add_fish(fish)
        self.assertEqual(fish, self.test.fish[0])
        self.assertEqual(expected, actual)

    def test_valid_fish_not_enough_capacity(self):
        self.test.capacity = 1
        self.assertEqual([], self.test.fish)
        fish = FreshwaterFish('fish', 'freshwater', 10)
        fish2 = FreshwaterFish('fish', 'freshwater', 10)
        self.test.add_fish(fish)
        expected = "Not enough capacity."
        actual = self.test.add_fish(fish2)
        self.assertEqual(expected, actual)

    def test_str_method_with_fish(self):
        fish = FreshwaterFish('fish', 'freshwater', 10)
        fish2 = FreshwaterFish('fish2', 'freshwater', 10)
        self.test.add_decoration(Ornament())
        self.test.add_decoration(Plant())
        self.test.add_decoration(Plant())
        self.test.add_fish(fish)
        self.test.add_fish(fish2)
        expected = "fresh:\nFish: fish fish2\nDecorations: 3\nComfort: 11"
        actual = self.test.__str__()
        self.assertEqual(expected, actual)

    def test_str_method_no_fish(self):
        self.test.add_decoration(Ornament())
        self.test.add_decoration(Plant())
        self.test.add_decoration(Plant())
        expected = "fresh:\nFish: none\nDecorations: 3\nComfort: 11"
        actual = self.test.__str__()
        self.assertEqual(expected, actual)
