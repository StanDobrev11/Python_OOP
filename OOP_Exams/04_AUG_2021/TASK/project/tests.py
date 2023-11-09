import unittest

from project.bakery import Bakery
from project.table.inside_table import InsideTable


class TestBakery(unittest.TestCase):

    def setUp(self) -> None:
        self.test = Bakery('test')

    def test_add_valid_food_not_in_menu(self):
        self.test.add_food('Cake', 'coco cake', 10.30)
        self.test.add_food('Cake', 'milk cake', 8.20)
        self.test.add_food('Bread', 'regular', 5.50)
        actual = self.test.add_food('Bread', 'diet', 6.75)
        expected = "Added diet (Bread) to the food menu"
        self.assertEqual(expected, actual)
        self.assertEqual(4, len(self.test.food_menu))

    def test_add_valid_food_already_in_menu_same_name_same_type_diff_price_raises_exception(self):
        self.test.add_food('Cake', 'coco cake', 10.30)
        self.test.add_food('Cake', 'milk cake', 8.20)
        self.test.add_food('Bread', 'regular', 5.50)
        self.test.add_food('Bread', 'diet', 6.75)
        with self.assertRaises(Exception) as ex:
            self.test.add_food('Bread', 'diet', 5.75)
        self.assertEqual("Bread diet is already in the menu!", str(ex.exception))

    def test_add_valid_food_already_in_meny_same_name_diff_type_adds_food(self):
        self.test.add_food('Cake', 'coco cake', 10.30)
        self.test.add_food('Cake', 'milk cake', 8.20)
        self.test.add_food('Bread', 'regular', 5.50)
        self.test.add_food('Bread', 'diet', 6.75)
        actual = self.test.add_food('Cake', 'diet', 5.75)
        expected = "Added diet (Cake) to the food menu"
        self.assertEqual(expected, actual)
        self.assertEqual(5, len(self.test.food_menu))

    def test_add_valid_drink_not_in_menu(self):
        self.test.add_drink('Tea', 'ice tea', 220, 'nice')
        self.test.add_drink('Tea', 'hot tea', 200, 'more')
        self.test.add_drink('Tea', 'herbs tea', 205, 'happy')
        self.test.add_drink('Water', 'mineral', 330, 'spring')
        actual = self.test.add_drink('Water', 'tap', 320, 'sparkling')
        expected = "Added tap (sparkling) to the drink menu"
        self.assertEqual(expected, actual)
        self.assertEqual(5, len(self.test.drinks_menu))

    def test_add_valid_drink_dif_type_same_name_added_ok(self):
        self.test.add_drink('Tea', 'ice tea', 220, 'nice')
        self.test.add_drink('Tea', 'hot tea', 200, 'more')
        self.test.add_drink('Tea', 'herbs tea', 205, 'happy')
        self.test.add_drink('Water', 'mineral', 330, 'spring')
        self.test.add_drink('Tea', 'tap', 320, 'sparkling')
        actual = self.test.add_drink('Water', 'tap', 320, 'sparkling')
        expected = "Added tap (sparkling) to the drink menu"
        self.assertEqual(expected, actual)

    def test_add_valid_drink_already_in_menu_raises_exception(self):
        self.test.add_drink('Tea', 'ice tea', 220, 'nice')
        self.test.add_drink('Tea', 'hot tea', 200, 'more')
        self.test.add_drink('Tea', 'herbs tea', 205, 'happy')
        with self.assertRaises(Exception) as ex:
            self.test.add_drink('Tea', 'herbs tea', 205, 'happy')
        self.assertEqual("Tea herbs tea is already in the menu!", str(ex.exception))

    def test_add_table_valid_output(self):
        self.test.add_table('InsideTable', 15, 4)
        self.assertEqual(1, len(self.test.tables_repository))
        self.assertEqual('InsideTable', self.test.tables_repository[0].type)

    def test_add_table_wrong_table_number_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.test.add_table('InsideTable', 75, 4)
        self.assertEqual("Inside table's number must be between 1 and 50 inclusive!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.test.add_table('OutsideTable', 15, 4)
        self.assertEqual("Outside table's number must be between 51 and 100 inclusive!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.test.add_table('OutsideTable', 52, 0)
        self.assertEqual("Capacity has to be greater than 0!", str(ex.exception))

    def test_add_table_raises_exception(self):
        self.test.add_table('InsideTable', 15, 4)
        with self.assertRaises(Exception) as ex:
            self.test.add_table('InsideTable', 15, 4)
        self.assertEqual("Table 15 is already in the bakery!", str(ex.exception))

    def test_reserve_table_success(self):
        self.test.add_table('InsideTable', 15, 4)
        self.test.add_table('InsideTable', 12, 8)
        self.test.add_table('InsideTable', 18, 1)
        self.test.add_table('OutsideTable', 55, 1)
        self.test.add_table('InsideTable', 19, 4)
        self.assertFalse(self.test.tables_repository[0].is_reserved)
        actual = self.test.reserve_table(4)
        expected = "Table 15 has been reserved for 4 people"
        self.assertEqual(actual, expected)
        self.assertTrue(self.test.tables_repository[0].is_reserved)

        self.assertFalse(self.test.tables_repository[1].is_reserved)
        actual_1 = self.test.reserve_table(5)
        expected_1 = "Table 12 has been reserved for 5 people"
        self.assertEqual(actual_1, expected_1)
        self.assertTrue(self.test.tables_repository[1].is_reserved)

    def test_reserve_table_not_success(self):
        self.test.add_table('InsideTable', 15, 4)
        self.test.add_table('InsideTable', 12, 8)
        self.test.add_table('InsideTable', 18, 1)
        self.test.add_table('OutsideTable', 55, 1)
        self.test.add_table('InsideTable', 19, 4)
        actual = self.test.reserve_table(9)
        expected = "No available table for 9 people"
        self.assertEqual(expected, actual)

    def test_order_food_raises_exception_table_not_found(self):
        self.assertEqual(0, len(self.test.tables_repository))
        actual = self.test.order_food(12, 'coco cake', 'regular')
        expected = "Could not find table 12"
        self.assertEqual(expected, actual)

    def test_order_return_proper_food_description(self):
        self.test.add_food('Cake', 'coco cake', 10.30)
        self.test.add_food('Cake', 'milk cake', 8.20)
        self.test.add_food('Bread', 'regular', 5.50)
        self.test.add_food('Bread', 'diet', 8.50)
        self.test.add_food('Bread', 'seeds', 7.50)
        self.test.add_table('InsideTable', 15, 4)
        actual = self.test.order_food(15, 'coco cake', 'banana', 'seeds', 'apples', 'regular')
        expected = "Table 15 ordered:\n- coco cake: 245.00g - 10.30lv\n- seeds: 200.00g - 7.50lv\n- regular: 200.00g - 5.50lv\ntest does not have in the menu:\nbanana\napples"
        self.assertEqual(expected, actual)

    def test_leave_table(self):
        table = InsideTable(15, 4)
        self.test.add_table(table.type, table.table_number, table.capacity)
        self.test.add_food('Cake', 'coco cake', 10.30)
        self.test.add_food('Cake', 'milk cake', 8.20)
        self.test.add_food('Bread', 'regular', 5.50)
        self.test.add_food('Bread', 'diet', 8.50)
        self.test.add_food('Bread', 'seeds', 7.50)
        self.test.order_food(15, 'coco cake', 'banana', 'seeds', 'apples', 'regular')
        actual = self.test.leave_table(15)
        expected = "Table: 15\nBill: 23.30"
        self.assertEqual(expected, actual)
        self.assertEqual([], table.food_orders)


if __name__ == '__main__':
    unittest.main()
