import unittest

from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.space_station import SpaceStation


class TestSpaceStation(unittest.TestCase):

    def setUp(self) -> None:
        self.ss = SpaceStation()
        self.b = Biologist('b')
        self.g = Geodesist('g')
        self.m = Meteorologist('m')

    def test_init_planet_repo(self):
        expected = "PlanetRepository"
        actual = self.ss.planet_repository.__class__.__name__
        self.assertEqual(expected, actual)

    def test_init_astro_repo(self):
        expected = "AstronautRepository"
        actual = self.ss.astronaut_repository.__class__.__name__
        self.assertEqual(expected, actual)

    def test_adds_astro_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.ss.add_astronaut('Test', 'test')
        self.assertEqual("Astronaut type is not valid!", str(ex.exception))

    def test_add_astro_return_success(self):
        actual = self.ss.add_astronaut("Biologist", 'Test')
        expected = "Successfully added Biologist: Test."
        self.assertEqual(expected, actual)

    def test_add_planet(self):
        actual = self.ss.add_planet('p', '1, 2, 3')
        self.assertEqual("Successfully added Planet: p.", actual)

    def test_retire_astro_valid(self):
        self.ss.add_astronaut('Biologist', 'b')
        self.ss.add_astronaut('Geodesist', 'g')
        actual = self.ss.retire_astronaut('g')
        expected = "Astronaut g was retired!"
        self.assertEqual(expected, actual)

    def test_retire_not_exist_exception(self):
        self.ss.add_astronaut('Biologist', 'b')
        self.ss.add_astronaut('Geodesist', 'g')
        with self.assertRaises(Exception) as ex:
            self.ss.retire_astronaut('m')
        self.assertEqual("Astronaut m doesn't exist!", str(ex.exception))

    def test_recharge_by_10(self):
        self.ss.add_astronaut('Biologist', 'b')
        self.ss.add_astronaut('Geodesist', 'g')
        self.ss.recharge_oxygen()
        actual = self.ss.astronaut_repository.astronauts[0].oxygen
        expected = 80
        self.assertEqual(expected, actual)
        actual = self.ss.astronaut_repository.astronauts[1].oxygen
        expected = 60
        self.assertEqual(expected, actual)

    def test_send_on_mission_invalid_planet(self):
        with self.assertRaises(Exception) as ex:
            self.ss.send_on_mission('test')
        self.assertEqual("Invalid planet name!", str(ex.exception))

    def test_send_on_mission_no_astronauts_exception(self):
        self.ss.add_planet("test", "1, 2, 3, 4, 5")
        with self.assertRaises(Exception) as ex:
            self.ss.send_on_mission('test')
        self.assertEqual("You need at least one astronaut to explore the planet!", str(ex.exception))

    def test_send_on_mission_explore_planet(self):
        self.ss.add_planet('Earth', '1, 2, 3, 4, 5')
        self.ss.add_astronaut('Biologist', 'BioName')
        self.ss.add_astronaut('Geodesist', 'GeoName')

        actual = self.ss.send_on_mission('Earth')
        expected = "Planet: Earth was explored. 1 astronauts participated in collecting items."

        self.assertEqual(expected, actual)

    def test_send_on_mission_not_explored(self):
        self.ss.add_planet('Earth', '1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11')
        self.ss.add_astronaut('Geodesist', 'GeoName')

        actual = self.ss.send_on_mission('Earth')
        expected = "Mission is not completed."

        self.assertEqual(expected, actual)

    def test_report(self):
        self.ss.add_planet('Earth', '1, 2, 3, 4, 5')
        self.ss.add_astronaut('Biologist', 'BioName')
        self.ss.add_astronaut('Geodesist', 'GeoName')
        self.ss.send_on_mission('Earth')
        expected = f"1 successful missions!\n0 missions were not completed!\nAstronauts' info:\nName: BioName\nOxygen: 45\nBackpack items: 5, 4, 3, 2, 1\nName: GeoName\nOxygen: 50\nBackpack items: none"
        actual = self.ss.report()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
