import unittest

from project.train.train import Train


class TestTrain(unittest.TestCase):
    def setUp(self) -> None:
        self.train = Train('Test', 10)

    def test_proper_init(self):
        self.assertEqual('Test', self.train.name)
        self.assertEqual(10, self.train.capacity)
        self.assertEqual("Train is full", self.train.TRAIN_FULL)
        self.assertEqual("Passenger {} Exists", self.train.PASSENGER_EXISTS)
        self.assertEqual("Passenger Not Found", self.train.PASSENGER_NOT_FOUND)
        self.assertEqual("Added passenger {}", self.train.PASSENGER_ADD)
        self.assertEqual("Removed {}", self.train.PASSENGER_REMOVED)
        self.assertEqual(0, self.train.ZERO_CAPACITY)

    def test_add_passenger_valid(self):
        actual = self.train.add('Ivan')
        expected = "Added passenger Ivan"
        self.assertEqual(expected, actual)
        self.assertEqual('Ivan', self.train.passengers[0])
        self.assertEqual(1, len(self.train.passengers))

    def test_add_passenger_already_in_list(self):
        self.train.add('Ivan')
        self.train.add('Dragan')
        with self.assertRaises(ValueError) as ve:
            self.train.add('Ivan')

        self.assertEqual("Passenger Ivan Exists", str(ve.exception))
        self.assertEqual(['Ivan', 'Dragan'], self.train.passengers)
        self.assertEqual(2, len(self.train.passengers))

    def test_add_passenger_not_enough_room_error(self):
        self.train.capacity = 2
        self.train.add('Ivan')
        self.train.add('Dragan')
        with self.assertRaises(ValueError) as ve:
            self.train.add('Stoyan')
        self.assertEqual("Train is full", str(ve.exception))
        self.assertEqual(['Ivan', 'Dragan'], self.train.passengers)
        self.assertEqual(2, len(self.train.passengers))

    def test_remove_passenger_valid(self):
        self.train.add('Ivan')
        self.train.add('Dragan')
        actual = self.train.remove('Dragan')
        expected = "Removed Dragan"
        self.assertEqual(expected, actual)
        self.assertEqual('Ivan', self.train.passengers[0])
        self.assertEqual(1, len(self.train.passengers))

    def test_remove_passenger_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.train.remove('Dragan')
        self.assertEqual("Passenger Not Found", str(ve.exception))


if __name__ == '__main__':
    unittest.main()
