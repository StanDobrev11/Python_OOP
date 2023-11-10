import unittest

from project.astronaut.astronaut import Astronaut
from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet


class TestAstronaut(unittest.TestCase):
    def setUp(self) -> None:
        self.b = Biologist('b')
        self.b1 = Biologist('b1')
        self.g = Geodesist('g')
        self.g1 = Geodesist('g1')
        self.m = Meteorologist('m')
        self.m1 = Meteorologist('m1')
        self.ar = AstronautRepository()

    def test_base_class_abc(self):
        with self.assertRaises(TypeError):
            Astronaut('test', 10)

    def test_proper_init(self):
        self.assertEqual('b', self.b.name)
        self.assertEqual(70, self.b.oxygen)
        self.assertEqual(5, self.b.oxygen_consumption)
        self.assertEqual([], self.b.backpack)

    def test_type_prop_returns_class_name(self):
        self.assertEqual("Biologist", self.b.type)
        self.assertEqual("Geodesist", self.g.type)
        self.assertEqual("Meteorologist", self.m.type)

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

    def test_add_astro_in_list(self):
        self.assertEqual([], self.ar.astronauts)
        self.ar.add(self.g)
        actual = self.ar.add(self.b)
        expected = "Successfully added Biologist: b."
        self.assertEqual([self.g, self.b], self.ar.astronauts)
        self.assertEqual(expected, actual)

    def test_add_same_astro(self):
        self.assertEqual([], self.ar.astronauts)
        self.ar.add(self.b)
        self.ar.add(self.g)
        actual = self.ar.add(self.g)
        expected = "g is already added."
        self.assertEqual([self.b, self.g], self.ar.astronauts)
        self.assertEqual(expected, actual)

    def test_remove_existing_astro(self):
        self.ar.add(self.b)
        self.ar.add(self.g)
        actual = self.ar.remove(self.b)
        expected = "Astronaut b was retired!"
        self.assertEqual(expected, actual)
        self.assertEqual([self.g], self.ar.astronauts)

    def test_remove_astro_not_in_list(self):
        self.ar.add(self.b)
        self.ar.add(self.g)
        self.ar.remove(self.m)
        self.assertEqual([self.b, self.g], self.ar.astronauts)

    def test_find_by_name_success(self):
        self.ar.add(self.b)
        self.ar.add(self.g)
        actual = self.ar.find_by_name('g')
        expected = self.g
        self.assertEqual(expected, actual)

    def test_find_by_name_raises_exception(self):
        self.ar.add(self.b)
        self.ar.add(self.g)
        with self.assertRaises(Exception) as ex:
            self.ar.find_by_name('m')
        self.assertEqual("Astronaut m doesn't exist!", str(ex.exception))

    def test_repr_method(self):
        self.ar.add(self.b)
        self.b.backpack = ['1', '2', '3']
        expected = "Name: b\nOxygen: 70\nBackpack items: 1, 2, 3"
        actual = self.b.__repr__()
        self.assertEqual(expected, actual)

    def test_repr_method_no_items(self):
        self.ar.add(self.b)
        expected = "Name: b\nOxygen: 70\nBackpack items: none"
        actual = self.b.__repr__()
        self.assertEqual(expected, actual)

    def test_select_for_mission(self):
        self.ar.add(self.b)
        self.ar.add(self.b1)
        self.ar.add(self.g)
        self.ar.add(self.g1)
        self.ar.add(self.m)
        self.ar.add(self.m1)
        actual = self.ar.select_for_mission()
        expected = [self.m, self.m1, self.b, self.b1, self.g]
        self.assertEqual(expected, actual)

    def test_select_for_mission_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.ar.select_for_mission()
        self.assertEqual("You need at least one astronaut to explore the planet!", str(ex.exception))

    def test_compare_oxygen(self):
        self.assertTrue(self.b > self.g)

    def test_explore(self):
        planet = Planet('test')
        planet.items = ['1', '2', '3', '4']
        self.assertEqual(50, self.g.oxygen)
        self.assertFalse(planet.is_explored)

        self.g.explore(planet)

        self.assertEqual(10, self.g.oxygen)
        self.assertTrue(planet.is_explored)
        self.assertEqual(['4', '3', '2', '1'], self.g.backpack)

    def test_explore_same_items_as_oxygen(self):
        planet = Planet('test')
        planet.items = ['1', '2', '3', '4', '5']
        self.assertEqual(50, self.g.oxygen)
        self.assertFalse(planet.is_explored)

        self.g.explore(planet)

        self.assertEqual(0, self.g.oxygen)
        self.assertTrue(planet.is_explored)
        self.assertEqual(['5', '4', '3', '2', '1'], self.g.backpack)

    def test_explore_planet_not_explored(self):
        planet = Planet('test')
        planet.items = ['-1', '0', '1', '2', '3', '4', '5']
        self.assertEqual(50, self.g.oxygen)
        self.assertFalse(planet.is_explored)

        self.g.explore(planet)

        self.assertEqual(0, self.g.oxygen)
        self.assertFalse(planet.is_explored)
        self.assertEqual(['5', '4', '3', '2', '1'], self.g.backpack)
        self.assertEqual(['-1', '0'], planet.items)

    def test_explore_planet_no_items(self):
        planet = Planet('test')
        self.assertEqual([], planet.items)

        self.g.explore(planet)

        self.assertEqual(50, self.g.oxygen)
        self.assertTrue(planet.is_explored)


if __name__ == '__main__':
    unittest.main()
