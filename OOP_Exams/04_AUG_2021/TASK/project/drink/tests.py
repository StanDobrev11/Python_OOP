import unittest

from project.drink.drink import Drink
from project.drink.tea import Tea
from project.drink.water import Water


class TestDrink(unittest.TestCase):
    def setUp(self) -> None:
        self.herbs = Tea('Herbs', 330, 'Twins Tea')
        self.spring = Water('Spring', 450, 'Velingrad')

    def test_base_class_abc(self):
        with self.assertRaises(TypeError):
            Drink('test', 200, 200, 'some_brand')

    def test_proper_init(self):
        self.assertEqual('Herbs', self.herbs.name)
        self.assertEqual(330, self.herbs.portion)
        self.assertEqual('Twins Tea', self.herbs.brand)
        self.assertEqual(2.50, self.herbs.price)
        self.assertEqual(1.50, self.spring.price)

    def test_name_proper_validation(self):
        tests = ['', '    ']
        for x in tests:
            with self.assertRaises(ValueError) as ve:
                self.herbs.name = x
                self.spring.name = x
            self.assertEqual("Name cannot be empty string or white space!", str(ve.exception))

    def test_brand_proper_validation(self):
        tests = ['', '    ']
        for x in tests:
            with self.assertRaises(ValueError) as ve:
                self.herbs.brand = x
                self.spring.brand = x
            self.assertEqual("Brand cannot be empty string or white space!", str(ve.exception))

    def test_repr_method(self):
        expected = " - Herbs Twins Tea - 330.00ml - 2.50lv"
        actual = self.herbs.__repr__()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()


herbs = Tea('Herbs', 330, 'Twins Tea')
menthol = Tea('Menthol', 340, 'Menthol Tea')
black = Tea('Black', 320, 'Black Tea')
mineral = Water('Mineral', 500, 'Mountain')
spring = Water('Spring', 450, 'Velingrad')
