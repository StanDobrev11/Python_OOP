from project.plantation import Plantation

import unittest


class TestPlantation(unittest.TestCase):
    def setUp(self) -> None:
        self.p = Plantation(10)

    def test_proper_init(self):
        self.assertEqual(10, self.p.size)
        self.assertEqual({}, self.p.plants)
        self.assertEqual([], self.p.workers)

    def test_size_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.p.size = -1
        self.assertEqual("Size must be positive number!", str(ve.exception))


    def test_hire_worker_success(self):
        expected = "Ivan successfully hired."
        actual = self.p.hire_worker('Ivan')
        self.assertEqual(expected, actual)
        self.assertEqual(['Ivan'], self.p.workers)

    def test_planting_first_plant_success(self):
        self.p.hire_worker('Ivan')
        self.assertEqual({}, self.p.plants)
        expected = "Ivan planted it's first Tree."
        actual = self.p.planting('Ivan', 'Tree')
        self.assertEqual(expected, actual)
        self.assertEqual({'Ivan': ['Tree']}, self.p.plants)

    def test_planting_tree_success(self):
        self.p.hire_worker('Ivan')
        self.p.hire_worker('Dragan')
        self.p.planting('Ivan', 'Tree')
        self.p.planting('Dragan', 'Tree')
        actual = self.p.planting('Dragan', 'Pine Tree')
        expected = "Dragan planted Pine Tree."
        self.assertEqual(expected, actual)
        self.assertEqual({'Ivan': ['Tree'], 'Dragan': ['Tree', 'Pine Tree']}, self.p.plants)

    def test_plantation_full_error(self):
        self.p.size = 3
        self.p.hire_worker('Ivan')
        self.p.hire_worker('Dragan')
        self.p.planting('Ivan', 'Tree')
        self.p.planting('Dragan', 'Tree')
        self.p.planting('Dragan', 'Pine Tree')

        with self.assertRaises(ValueError) as ve:
            self.p.planting('Ivan', 'Pine')
        self.assertEqual("The plantation is full!", str(ve.exception))
        self.assertEqual(2, len(self.p.workers))

    def test_plantation_worker_not_hired(self):
        with self.assertRaises(ValueError) as ve:
            self.p.planting('Ivan', 'Tree')
        self.assertEqual("Worker with name Ivan is not hired!", str(ve.exception))

    def test_len_method_with_zero(self):
        self.assertEqual(0, len(self.p))

    def test_len_method_more(self):
        self.p.hire_worker('Ivan')
        self.p.hire_worker('Dragan')
        self.p.planting('Ivan', 'Tree')
        self.p.planting('Dragan', 'Tree')
        self.p.planting('Dragan', 'Pine Tree')
        self.assertEqual(3, len(self.p))

    def test_str_method_all_missing(self):
        self.assertEqual('Plantation size: 10\n', self.p.__str__())

    def test_str(self):
        self.p.hire_worker('Ivan')
        self.p.hire_worker('Dragan')
        self.p.planting('Ivan', 'Tree')
        self.p.planting('Dragan', 'Tree')
        self.p.planting('Dragan', 'Pine Tree')
        expected = "Plantation size: 10\nIvan, Dragan\nIvan planted: Tree\nDragan planted: Tree, Pine Tree"
        self.assertEqual(expected, str(self.p))

    def test_repr(self):
        self.p.hire_worker('Ivan')
        self.p.hire_worker('Dragan')
        self.p.planting('Ivan', 'Tree')
        self.p.planting('Dragan', 'Tree')
        self.p.planting('Dragan', 'Pine Tree')
        expected = "Size: 10\nWorkers: Ivan, Dragan"
        self.assertEqual(expected, self.p.__repr__())

    def test_repr_nothing(self):
        expected = "Size: 10\nWorkers: "
        self.assertEqual(expected, self.p.__repr__())


if __name__ == '__main__':
    unittest.main()
