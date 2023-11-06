import unittest

from project.factory.factory import Factory
from project.factory.paint_factory import PaintFactory


class TestPaintFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.pf = PaintFactory('Candy', 10)

    def test_if_base_class_is_abstract(self):
        with self.assertRaises(TypeError):
            Factory('Candy', 10)

    def test_proper_init_method(self):
        self.assertEqual('Candy', self.pf.name)
        self.assertEqual(10, self.pf.capacity)
        self.assertEqual({}, self.pf.ingredients)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.pf.valid_ingredients)

    def test_product_property_returns_ingredients(self):
        self.assertEqual(self.pf.ingredients, self.pf.products)

    def test_add_ingredient_valid_ingredient_not_yet_added(self):
        self.pf.add_ingredient('white', 10)
        expected = {'white': 10}
        actual = self.pf.ingredients
        self.assertEqual(expected, actual)

    def test_add_ingredient_valid_ingredient_already_added(self):
        self.pf.ingredients = {'white': 5}
        self.pf.add_ingredient('white', 5)
        expected = {'white': 10}
        actual = self.pf.ingredients
        self.assertEqual(expected, actual)

    def test_add_ingredient_valid_ingredient_already_added_raises_no_capacity_value_error(self):
        self.pf.ingredients = {'white': 5}
        with self.assertRaises(ValueError) as ve:
            self.pf.add_ingredient('white', 10)
        self.assertEqual("Not enough space in factory", str(ve.exception))

    def test_add_ingredient_with_invalid_ingredient(self):
        with self.assertRaises(TypeError) as te:
            self.pf.add_ingredient('Milk', 5)
        expected = "Ingredient of type Milk not allowed in PaintFactory"
        self.assertEqual(expected, str(te.exception))


    def test_remove_ingredient_method_raises_value_error(self):
        self.pf.ingredients['Milk'] = 10
        with self.assertRaises(ValueError) as ve:
            self.pf.remove_ingredient('Milk', 15)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ve.exception))

    def test_remove_ingredient_method_raises_no_such_item_error(self):
        with self.assertRaises(KeyError) as ke:
            self.pf.remove_ingredient('Milk', 10)
        self.assertEqual("'No such ingredient in the factory'", str(ke.exception))

    def test_remove_ingredient_method_valid_ingredient_zero_quantity_left(self):
        self.pf.ingredients['Milk'] = 10
        self.pf.remove_ingredient('Milk', 10)
        self.assertEqual(0, self.pf.ingredients['Milk'])

    def test_remove_ingredient_method_valid_ingredient_positive_quantity_left(self):
        self.pf.ingredients['Milk'] = 10
        self.pf.remove_ingredient('Milk', 8)
        self.assertEqual(2, self.pf.ingredients['Milk'])

    def test_can_add_method_returns_true(self):
        self.assertTrue(self.pf.can_add(10))
        self.assertTrue(self.pf.can_add(5))

    def test_can_add_method_returns_false(self):
        self.assertFalse(self.pf.can_add(11))

    def test_repr_method_no_ingredients(self):
        actual = self.pf.__repr__()
        expected = "Factory name: Candy with capacity 10.\n"
        self.assertEqual(expected, actual)

    def test_repr_method_one_ingredients(self):
        self.pf.ingredients['Milk'] = 10
        actual = self.pf.__repr__()
        expected = "Factory name: Candy with capacity 10.\nMilk: 10\n"
        self.assertEqual(expected, actual)

    def test_repr_method_two_ingredients(self):
        self.pf.ingredients['Milk'] = 10
        self.pf.ingredients['Coco'] = 5
        actual = self.pf.__repr__()
        expected = "Factory name: Candy with capacity 10.\nMilk: 10\nCoco: 5\n"
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()