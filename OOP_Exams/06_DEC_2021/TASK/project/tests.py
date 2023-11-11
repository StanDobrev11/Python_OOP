import unittest

from project.controller import Controller


class TestController(unittest.TestCase):
    def setUp(self) -> None:
        self.c = Controller()

    def test_init(self):
        self.assertEqual([], self.c.cars)
        self.assertEqual([], self.c.races)
        self.assertEqual([], self.c.drivers)

    def test_create_car_success(self):
        actual = self.c.create_car('MuscleCar', '440p', 250)
        expected = f"MuscleCar 440p is created."
        self.assertEqual(expected, actual)

    def test_create_car_no_valid_model(self):
        with self.assertRaises(ValueError) as ve:
            self.c.create_car('MuscleCar', '440', 250)
        self.assertEqual("Model 440 is less than 4 symbols!", str(ve.exception))

