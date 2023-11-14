from project.toy_store import ToyStore

import unittest


class TestToyStore(unittest.TestCase):
    def setUp(self) -> None:
        self.t = ToyStore()

    def test_init(self):
        expected = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        self.assertEqual(expected, self.t.toy_shelf)

    def test_add_toy_success(self):
        expected = "Toy:Toy placed successfully!"
        actual = self.t.add_toy('B', 'Toy')
        self.assertEqual(expected, actual)
        self.assertEqual('Toy', self.t.toy_shelf['B'])

    def test_add_toy_exception_taken_shelf(self):
        self.t.add_toy('B', 'Toy')
        with self.assertRaises(Exception) as ex:
            self.t.add_toy('B', 'Toy2')
        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_exception_toy__in_shelf(self):
        self.t.add_toy('B', 'Toy')
        with self.assertRaises(Exception) as ex:
            self.t.add_toy('B', 'Toy')
        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_non_existing_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.t.add_toy('M', 'Toy')
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_success(self):
        self.t.add_toy('B', 'Toy')
        expected = "Remove toy:Toy successfully!"
        actual = self.t.remove_toy('B', 'Toy')
        self.assertIsNone(self.t.toy_shelf['B'])
        self.assertEqual(expected, actual)

    def test_remove_non_existing_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.t.remove_toy('M', 'Toy')
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_non_existing_toy(self):
        with self.assertRaises(Exception) as ex:
            self.t.remove_toy('B', 'Toy')
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))


if __name__ == '__main__':
    unittest.main()
