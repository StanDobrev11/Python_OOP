from OOP_19_Testing_Lab.OOP_03_List.extended_list import IntegerList

import unittest


class ListTest(unittest.TestCase):

    def test_constructor_private_data_attr(self):
        il = IntegerList()
        self.assertEqual(il._IntegerList__data, [])

    def test_constructor_public_data_attr(self):
        il = IntegerList()
        with self.assertRaises(AttributeError) as context:
            il.data
        self.assertEqual(type(context.exception), AttributeError)
        self.assertEqual(str(context.exception), "'IntegerList' object has no attribute 'data'")

    def test_constructor_stores_integers_only(self):
        il = IntegerList(0, '1', '2', 3, -1, 2.5, 'pi')
        self.assertEqual(il.get_data(), [0, 3, -1])

    def test_get_data_method(self):
        il = IntegerList(1, 2, 3)
        self.assertEqual(il.get_data(), [1, 2, 3])

    def test_add_integer_element(self):
        il = IntegerList(1, 2, 3)
        self.assertEqual(il.add(4), [1, 2, 3, 4])

    def test_add_non_integer_element(self):
        il = IntegerList(1, 2, 3)
        with self.assertRaises(ValueError) as context:
            il.add('string')
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), "Element is not Integer")

    def test_remove_correct_index(self):
        il = IntegerList(1, 2, 3)
        self.assertEqual(il.remove_index(0), 1)
        self.assertEqual(il.get_data(), [2, 3])

    def test_remove_incorrect_index(self):
        il = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as context:
            il.remove_index(3)
        self.assertEqual(type(context.exception), IndexError)
        self.assertEqual(str(context.exception), "Index is out of range")

    def test_get_with_proper_index(self):
        il = IntegerList(1, 2, 3)
        self.assertEqual(il.get(0), 1)
        self.assertEqual(il.get_data(), [1, 2, 3])

    def test_get_with_incorrect_index(self):
        il = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as context:
            il.get(3)
        self.assertEqual(type(context.exception), IndexError)
        self.assertEqual(str(context.exception), "Index is out of range")

    def test_insert_with_proper_index(self):
        il = IntegerList(1, 2, 3)
        il.insert(0, 0)
        self.assertEqual(il.get_data(), [0, 1, 2, 3])

    def test_insert_with_incorrect_index(self):
        il = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as context:
            il.insert(4, 4)
        self.assertEqual(type(context.exception), IndexError)
        self.assertEqual(str(context.exception), "Index is out of range")

    def test_insert_with_non_integer_element(self):
        il = IntegerList(1, 2, 3)
        with self.assertRaises(ValueError) as context:
            il.insert(0, 'string')
        self.assertEqual(type(context.exception), ValueError)
        self.assertEqual(str(context.exception), "Element is not Integer")

    def test_get_biggest(self):
        il = IntegerList(1, 2, 3)
        self.assertEqual(il.get_biggest(), 3)

    def test_get_index(self):
        il = IntegerList(1, 2, 3)
        self.assertEqual(il.get_index(3), 2)

if __name__ == '__main__':
    unittest.main()
