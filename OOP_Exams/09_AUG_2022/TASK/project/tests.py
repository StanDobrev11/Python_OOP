import unittest

from project.horse_race_app import HorseRaceApp


class TestHorseApp(unittest.TestCase):
    def setUp(self) -> None:
        self.test = HorseRaceApp()

    def test_add_horse_success(self):
        expected = "Appaloosa horse HorseA is added."
        expected2 = "Thoroughbred horse HorseT is added."
        actual = self.test.add_horse('Appaloosa', 'HorseA', 117)
        actual2 = self.test.add_horse('Thoroughbred', 'HorseT', 125)

        self.assertEqual(expected, actual)
        self.assertEqual(expected2, actual2)
        self.assertEqual(2, len(self.test.horses))
        self.assertEqual(117, self.test.horses[0].speed)

    def test_add_horse_already_existing(self):
        self.test.add_horse('Appaloosa', 'HorseA', 117)
        with self.assertRaises(Exception) as ex:
            self.test.add_horse('Appaloosa', 'HorseA', 117)

        self.assertEqual("Horse HorseA has been already added!", str(ex.exception))

    def test_add_wrong_breed_does_nothing(self):
        self.assertIsNone(self.test.add_horse('Test', 'Ivan', 117))

    def test_add_jockey_success(self):
        expected = "Jockey Ivan is added."
        actual = self.test.add_jockey('Ivan', 22)
        self.assertEqual(expected, actual)

    def test_add_jockey_raises_age_error(self):
        with self.assertRaises(ValueError) as ve:
            self.test.add_jockey('Ivan', 17)
        expected = "Jockeys must be at least 18 to participate in the race!"
        self.assertEqual(expected, str(ve.exception))

    def test_add_jockey_raises_name_error(self):
        with self.assertRaises(ValueError) as ve:
            self.test.add_jockey('', 17)
        expected = "Name should contain at least one character!"
        self.assertEqual(expected, str(ve.exception))

    def test_add_jockey_already_added(self):
        self.test.add_jockey('Ivan', 22)
        with self.assertRaises(Exception) as ex:
            self.test.add_jockey('Ivan', 22)
        expected = "Jockey Ivan has been already added!"
        self.assertEqual(expected, str(ex.exception))

    def test_add_jockeys(self):
        self.test.add_jockey('Ivan', 22)
        self.test.add_jockey('Stoyan', 21)
        self.test.add_jockey('Dragan', 23)
        self.assertEqual(3, len(self.test.jockeys))

    def test_create_race_success(self):
        self.test.create_horse_race('Winter')
        self.test.create_horse_race('Autumn')
        self.test.create_horse_race('Spring')
        actual = self.test.create_horse_race('Summer')
        expected = "Race Summer is created."
        self.assertEqual(expected, actual)
        self.assertEqual(4, len(self.test.horse_races))

    def test_create_raises_ex_already_created(self):
        self.test.create_horse_race('Summer')
        self.test.create_horse_race('Winter')
        with self.assertRaises(Exception) as ex:
            self.test.create_horse_race('Winter')
        expected = "Race Winter has been already created!"
        self.assertEqual(expected, str(ex.exception))

    def test_create_race_wrong_type_raises_exception(self):
        expected = "Race type does not exist!"
        with self.assertRaises(ValueError) as ve:
            self.test.create_horse_race('Test')
        self.assertEqual(expected, str(ve.exception))
