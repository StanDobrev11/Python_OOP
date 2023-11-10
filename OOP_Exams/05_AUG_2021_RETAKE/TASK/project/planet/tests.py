import unittest

from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class TestPlanet(unittest.TestCase):

    def setUp(self) -> None:
        self.p = Planet('p')
        self.p2 = Planet('p2')
        self.pr = PlanetRepository()

    def test_proper_init(self):
        self.assertEqual('p', self.p.name)
        self.assertEqual([], self.p.items)
        self.assertEqual([], self.pr.planets)

    def test_name_raises_value_error(self):
        tests = ['', '     ']
        for x in tests:
            with self.assertRaises(ValueError) as ve:
                self.p.name = x
            self.assertEqual("Planet name cannot be empty string or whitespace!", str(ve.exception))

    def test_add_planet_to_repo(self):
        self.pr.add(self.p)
        self.assertEqual([self.p], self.pr.planets)

    def test_add_same_planet(self):
        self.pr.add(self.p)
        self.pr.add(self.p)
        self.assertEqual([self.p], self.pr.planets)

    def test_remove_planet(self):
        self.pr.add(self.p)
        self.pr.add(self.p2)
        self.assertEqual([self.p, self.p2], self.pr.planets)
        self.pr.remove(self.p2)
        self.assertEqual([self.p], self.pr.planets)

    def test_remove_non_listed_planet(self):
        self.pr.add(self.p)
        self.assertEqual([self.p], self.pr.planets)
        self.pr.remove(self.p2)
        self.assertEqual([self.p], self.pr.planets)

    def test_find_planet_by_name(self):
        self.pr.add(self.p)
        self.pr.add(self.p2)
        self.assertEqual([self.p, self.p2], self.pr.planets)
        actual = self.pr.find_by_name('p2')
        expected = self.p2
        self.assertEqual(expected, actual)

    def test_find_non_listed_planet_returns_none(self):
        self.pr.add(self.p)
        self.pr.add(self.p2)
        self.assertEqual([self.p, self.p2], self.pr.planets)
        self.assertIsNone(self.pr.find_by_name('p3'))


if __name__ == '__main__':
    unittest.main()
