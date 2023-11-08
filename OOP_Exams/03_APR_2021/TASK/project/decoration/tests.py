import unittest

from project.decoration.base_decoration import BaseDecoration
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant


class TestDecoration(unittest.TestCase):

    def test_base_decoration_abc(self):
        with self.assertRaises(TypeError) as te:
            b = BaseDecoration(5, 3)
        expected = "Can't instantiate abstract class BaseDecoration with abstract method __repr__"
        self.assertEqual(expected, str(te.exception))

    def test_decoration_types_implemented(self):
        self.assertEqual({'Ornament', 'Plant'}, Plant().base_types)

    def test_ornament_price_comfort(self):
        comfort = 1
        price = 5
        o = Ornament()
        self.assertEqual(comfort, o.comfort)
        self.assertEqual(price, o.price)

    def test_plant_price_comfort(self):
        comfort = 5
        price = 10
        p = Plant()
        self.assertEqual(comfort, p.comfort)
        self.assertEqual(price, p.price)

    def test_decoration_repository_init(self):
        dr = DecorationRepository()
        self.assertEqual([], dr.decorations)

    def test_add_decorations(self):
        dr = DecorationRepository()
        o = Ornament()
        p = Plant()
        dr.add(o)
        self.assertEqual([o], dr.decorations)
        dr.add(p)
        self.assertEqual([o, p], dr.decorations)

    # •	Removes the decoration object from the list if it exists and returns True, otherwise returns False.
    def test_remove_decoration_if_exists_and_returns_true(self):
        dr = DecorationRepository()
        o = Ornament()
        p = Plant()
        dr.add(o)
        dr.add(p)
        result = dr.remove(o)
        self.assertEqual([p], dr.decorations)
        self.assertTrue(result)

    def test_remove_non_existing_return_false(self):
        dr = DecorationRepository()
        o = Ornament()
        result = dr.remove(o)
        self.assertEqual([], dr.decorations)
        self.assertFalse(result)

    # •	Returns the first decoration of the given type if there is. Otherwise, returns a message "None".
    def test_find_decoration_by_type_return_first_decoration(self):
        dr = DecorationRepository()
        o = Ornament()
        p = Plant()
        p1 = Plant()
        p2 = Plant()
        o1 = Ornament()
        dr.add(o)
        dr.add(p1)
        dr.add(p)
        dr.add(o1)
        dr.add(p2)
        self.assertEqual(p1, dr.find_by_type('Plant'))
        self.assertEqual(o, dr.find_by_type('Ornament'))

    def test_find_decoration_return_none_if_none(self):
        dr = DecorationRepository()
        self.assertIsNone(dr.find_by_type('Ornament'))


if __name__ == '__main__':
    unittest.main()
