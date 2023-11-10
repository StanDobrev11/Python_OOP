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
        actual = self.pr.add(self.p)
        expected = "Successfully added Planet: p."
        self.assertEqual([self.p], self.pr.planets)
        self.assertEqual(expected, actual)

    def test_add_same_planet(self):
        self.pr.add(self.p)
        actual = self.pr.add(self.p)
        expected = "p is already added."
        self.assertEqual([self.p], self.pr.planets)
        self.assertEqual(expected, actual)

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

    def test_find_non_listed_planet_raises_exception(self):
        self.pr.add(self.p)
        self.pr.add(self.p2)
        with self.assertRaises(Exception) as ex:
            self.pr.find_by_name('p3')
        self.assertEqual("Invalid planet name!", str(ex.exception))

    def test_add_items(self):
        items = 'knife, coca-cola, RANDOM_ITEM, different object, some.simple items'
        self.p.add_items(items)
        actual = self.p.items
        expected = ['knife', 'coca-cola', 'RANDOM_ITEM', 'different object', 'some.simple items']
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
