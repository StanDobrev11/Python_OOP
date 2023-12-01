import unittest

from OOP_Workshop_HashTable.hash_table import HashTable


class TestHashTable(unittest.TestCase):

    def setUp(self) -> None:
        self.table = HashTable()

    def test_proper_init(self):
        self.assertEqual(4, self.table._HashTable__capacity)
        self.assertEqual([None] * 4, self.table._HashTable__key_array)
        self.assertEqual([None] * 4, self.table._HashTable__value_array)
        self.assertEqual(0, self.table._HashTable__length)

    def test_add_item(self):
        self.assertEqual(0, len(self.table))

        self.table.add('name', 'Peter')
        expected = 'Peter'
        actual = self.table['name']
        self.assertEqual(expected, actual)

    def test_add_again_same_key(self):
        self.table.add('name', 'Peter')
        expected = 'Peter'
        actual = self.table['name']
        self.assertEqual(expected, actual)

        self.table['name'] = 'Ivan'

        self.assertEqual('Ivan', self.table['name'])

    def test_add_key_increase_capacity(self):
        self.table.add('name', 'Peter')
        self.table.add('name1', 'Peter1')
        self.table.add('name2', 'Peter2')
        self.table.add('name3', 'Peter3')

        self.assertEqual(4, len(self.table))

        self.table.add('name4', 'Peter4')

        self.assertEqual(5, len(self.table))

    def test_getitem_method_returns_item(self):
        self.table.add('name', 'Peter')
        actual = self.table['name']
        expected = 'Peter'
        self.assertEqual(expected, actual)

    def test_getitem_method_raises_error(self):
        self.table.add('name', 'Peter')
        with self.assertRaises(KeyError) as ke:
            self.table['no valid key']
        expected = "'no valid key is not a valid HashTable key'"
        self.assertEqual(expected, str(ke.exception))

    def test_get_method_returns_value(self):
        self.table.add('name', 'Peter')
        actual = self.table.get('name')
        expected = 'Peter'
        self.assertEqual(expected, actual)

    def test_get_returns_msg(self):
        self.table.add('name', 'Peter')
        actual = self.table.get('name1', 'no such key')
        expected = 'no such key'
        self.assertEqual(actual, expected)

    def test_del_method_reduces_len_attr(self):
        self.table.add('name', 'Peter')
        self.table.add('name1', 'Peter1')
        self.table.add('name2', 'Peter2')

        self.assertEqual(3, len(self.table))

        del self.table['name']

        self.assertEqual(2, len(self.table))


if __name__ == '__main__':
    unittest.main()
