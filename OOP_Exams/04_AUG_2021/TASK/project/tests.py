import unittest

from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.bakery import Bakery
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class TestBakery(unittest.TestCase):

    def setUp(self) -> None:
        self.test = Bakery("Bakery")
        vanilla = Cake('Vanilla', 10.30)
        choco = Cake('Choco', 7.25)
        mixed = Cake('Mixed', 9.90)
        diet = Bread('Diet', 5.45)
        seeds = Bread('Seeds', 6.76)
        fit = Bread('Fit', 10.20)
        herbs = Tea('Herbs', 330, 'Twins Tea')
        menthol = Tea('Menthol', 340, 'Menthol Tea')
        black = Tea('Black', 320, 'Black Tea')
        mineral = Water('Mineral', 500, 'Mountain')
        spring = Water('Spring', 450, 'Velingrad')
        table_1 = InsideTable(1, 4)
        table_2 = InsideTable(2, 8)
        table_6 = InsideTable(6, 5)
        table_3 = InsideTable(3, 10)
        table_51 = OutsideTable(51, 14)
        table_55 = OutsideTable(55, 6)
        table_100 = OutsideTable(100, 10)

        self.test_tables = [table_1, table_2, table_3, table_6, table_51, table_55, table_100]
        self.drink_tests = [herbs, menthol, black, mineral, spring]
        self.foods_tests = [vanilla, choco, mixed, diet, seeds, fit]

    def test_proper_init(self):
        self.assertEqual('Bakery', self.test.name)
        self.assertEqual([], self.test.food_menu)
        self.assertEqual([], self.test.drinks_menu)
        self.assertEqual([], self.test.tables_repository)
        self.assertEqual(0, self.test.total_income)

    def test_name_validator_raises_value_error(self):
        tests = ['', '    ']
        with self.assertRaises(ValueError) as ve:
            for x in tests:
                self.test.name = x
            self.assertEqual("Name cannot be empty string or white space!", str(ve.exception))

    def test_add_food_to_menu_food_not_present(self):
        for food in self.foods_tests:
            actual = self.test.add_food(food.type, food.name, food.price)
            expected = f"Added {food.name} ({food.type}) to the food menu"
            self.assertEqual(expected, actual)

    def test_add_food_already_in_menu(self):
        for food in self.foods_tests:
            self.test.add_food(food.type, food.name, food.price)
        test_food = Bread('Seeds', 6.76)
        with self.assertRaises(Exception) as ex:
            self.test.add_food(test_food.type, test_food.name, test_food.price)
        self.assertEqual("Bread Seeds is already in the menu!", str(ex.exception))

    def test_add_drink_to_menu(self):
        for drink in self.drink_tests:
            actual = self.test.add_drink(drink.type, drink.name, drink.portion, drink.brand)
            expected = f"Added {drink.name} ({drink.brand}) to the drink menu"
            self.assertEqual(expected, actual)

    def test_add_drink_already_in_menu(self):
        for drink in self.drink_tests:
            self.test.add_drink(drink.type, drink.name, drink.portion, drink.brand)
        test_drink = Tea('Black', 320, 'Black Tea')
        with self.assertRaises(Exception) as ex:
            self.test.add_drink(test_drink.type, test_drink.name, test_drink.portion, test_drink.brand)
        self.assertEqual("Tea Black is already in the menu!", str(ex.exception))

    def test_add_table_to_list(self):
        for table in self.test_tables:
            actual = self.test.add_table(table.type, table.table_number, table.capacity)
            expected = f"Added table number {table.table_number} in the bakery"
            self.assertEqual(expected, actual)

    def test_add_table_raises_exception(self):
        for table in self.test_tables:
            self.test.add_table(table.type, table.table_number, table.capacity)
        test_table = OutsideTable(100, 10)
        with self.assertRaises(Exception) as ex:
            self.test.add_table(test_table.type, test_table.table_number, test_table.capacity)
        self.assertEqual("Table 100 is already in the bakery!", str(ex.exception))

    def test_reserve_table_reserves_table(self):
        for table in self.test_tables:
            self.test.add_table(table.type, table.table_number, table.capacity)
        actual = self.test.reserve_table(13)
        expected = "Table 51 has been reserved for 13 people"
        self.assertEqual(expected, actual)
        test_table = [table for table in self.test.tables_repository if table.is_reserved][0]
        self.assertEqual(13, test_table.number_of_people)

    def test_table_returns_no_available_table(self):
        for table in self.test_tables:
            self.test.add_table(table.type, table.table_number, table.capacity)
        actual = self.test.reserve_table(41)
        expected = "No available table for 41 people"
        self.assertEqual(expected, actual)
        self.assertFalse(not any(self.test.tables_repository))

    def test_order_food_no_such_table(self):
        for table in self.test_tables:
            self.test.add_table(table.type, table.table_number, table.capacity)
        for food in self.foods_tests:
            self.test.add_food(food.type, food.name, food.price)

        actual = self.test.order_food(111, 'Choco', 'Kimchi', 'Bananas', 'Fit')
        expected = "Could not find table 111"

        self.assertEqual(expected, actual)

    def test_order_food_have_menu_food_and_non_menu(self):
        for table in self.test_tables:
            self.test.add_table(table.type, table.table_number, table.capacity)
        for food in self.foods_tests:
            self.test.add_food(food.type, food.name, food.price)

        actual = self.test.order_food(3, 'Seeds', 'Choco', 'Kimchi', 'Bananas', 'Fit')
        expected = "Table 3 ordered:\n - Seeds: 200.00g - 6.76lv\n - Choco: 245.00g - 7.25lv\n - Fit: 200.00g - 10.20lv\nBakery does not have in the menu:\nKimchi\nBananas"
        self.assertEqual(expected, actual)
        test_table = [table for table in self.test.tables_repository if table.is_reserved][0]
        self.assertEqual(3, test_table.table_number)
        self.assertEqual(3, len(test_table.food_orders))

    def test_order_drink_no_such_table(self):
        for table in self.test_tables:
            self.test.add_table(table.type, table.table_number, table.capacity)
        for drink in self.drink_tests:
            self.test.add_drink(drink.type, drink.name, drink.portion, drink.brand)

        actual = self.test.order_drink(111, 'Choco', 'Kimchi', 'Bananas', 'Fit')
        expected = "Could not find table 111"

        self.assertEqual(expected, actual)

    def test_order_drink_have_menu_food_and_non_menu(self):
        for table in self.test_tables:
            self.test.add_table(table.type, table.table_number, table.capacity)
        for drink in self.drink_tests:
            self.test.add_drink(drink.type, drink.name, drink.portion, drink.brand)

        actual = self.test.order_drink(3, 'Spring', 'Mineral', 'Kimchi', 'Bananas', 'Black')
        expected = "Table 3 ordered:\n - Spring Velingrad - 450.00ml - 1.50lv\n - Mineral Mountain - 500.00ml - 1.50lv\n - Black Black Tea - 320.00ml - 2.50lv\nBakery does not have in the menu:\nKimchi\nBananas"
        self.assertEqual(expected, actual)
        test_table = [table for table in self.test.tables_repository if table.is_reserved][0]
        self.assertEqual(3, test_table.table_number)
        self.assertEqual(3, len(test_table.drink_orders))

    def test_leave_table(self):
        for table in self.test_tables:
            self.test.add_table(table.type, table.table_number, table.capacity)
        for drink in self.drink_tests:
            self.test.add_drink(drink.type, drink.name, drink.portion, drink.brand)
        for food in self.foods_tests:
            self.test.add_food(food.type, food.name, food.price)

        self.test.order_drink(3, 'Spring', 'Mineral', 'Kimchi', 'Bananas', 'Black')
        self.test.order_food(3, 'Seeds', 'Choco', 'Kimchi', 'Bananas', 'Fit')
        test_table = [table for table in self.test.tables_repository if table.is_reserved][0]

        actual = self.test.leave_table(3)
        expected = "Table: 3\nBill: 29.71"
        self.assertEqual(expected, actual)
        self.assertFalse(test_table.is_reserved)
        self.assertEqual(29.71, self.test.total_income)



    def test_get_total_income(self):
        for table in self.test_tables:
            self.test.add_table(table.type, table.table_number, table.capacity)
        for drink in self.drink_tests:
            self.test.add_drink(drink.type, drink.name, drink.portion, drink.brand)
        for food in self.foods_tests:
            self.test.add_food(food.type, food.name, food.price)

        self.test.order_drink(51, 'Spring', 'Mineral', 'Kimchi', 'Bananas', 'Black')
        self.test.order_drink(51, 'Spring', 'Mineral', 'Kimchi', 'Bananas', 'Black')
        self.test.order_food(3, 'Seeds', 'Choco', 'Kimchi', 'Bananas', 'Fit')
        self.test.order_food(3, 'Seeds', 'Choco', 'Kimchi', 'Bananas', 'Fit')

        self.test.leave_table(3)
        self.test.leave_table(51)

        expected = "Total income: 59.42lv"
        actual = self.test.get_total_income()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
