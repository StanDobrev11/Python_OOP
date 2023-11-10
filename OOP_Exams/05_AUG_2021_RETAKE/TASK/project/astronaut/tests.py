import unittest

from project.astronaut.astronaut import Astronaut
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist


class TestAstronaut(unittest.TestCase):
    def setUp(self) -> None:
        self.b = Biologist('b')
        self.g = Geodesist('g')
        self.m = Meteorologist('m')

    def test_base_class_abc(self):
        with self.assertRaises(TypeError):
            Astronaut('test', 10)

    def test_proper_init(self):
        self.assertEqual('b', self.b.name)
        self.assertEqual(70, self.b.oxygen)
        self.assertEqual(5, self.b.oxygen_consumption)
        self.assertEqual([], self.b.backpack)

    def test_name_raises_value_error(self):
        tests = ['', '     ']
        for x in tests:
            with self.assertRaises(ValueError) as ve:
                self.b.name = x
            self.assertEqual("Astronaut name cannot be empty string or whitespace!", str(ve.exception))

    def test_breathe_reduces_oxygen_biologist(self):
        self.assertEqual(70, self.b.oxygen)
        self.b.breathe()
        self.assertEqual(65, self.b.oxygen)

    def test_breathe_reduces_oxygen_geodesist(self):
        self.assertEqual(50, self.g.oxygen)
        self.g.breathe()
        self.assertEqual(40, self.g.oxygen)

    def test_breathe_reduces_oxygen_meteorologist(self):
        self.assertEqual(90, self.m.oxygen)
        self.m.breathe()
        self.assertEqual(75, self.m.oxygen)

    def test_add_oxygen(self):
        self.assertEqual(70, self.b.oxygen)
        self.b.increase_oxygen(10)
        self.assertEqual(80, self.b.oxygen)


if __name__ == '__main__':
    unittest.main()
