import unittest

from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table


class TestTable(unittest.TestCase):
    def setUp(self) -> None:
        self.table_3 = InsideTable(3, 10)
        self.table_51 = OutsideTable(51, 14)

    def test_base_table_abc(self):
        with self.assertRaises(TypeError):
            Table(15, 10)

    def test_proper_init(self):
        self.assertEqual(3, self.table_3.table_number)
        self.assertEqual(14, self.table_51.capacity)
        self.assertEqual('InsideTable', self.table_3.type)
        self.assertEqual('OutsideTable', self.table_51.type)
        self.assertEqual([], self.table_3.food_orders)
        self.assertEqual([], self.table_51.drink_orders)
        self.assertEqual(0, self.table_51.number_of_people)
        self.assertFalse(self.table_3.is_reserved)

    def test_capacity_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.table_3.capacity = -1
            self.table_51.capacity = 0
        self.assertEqual("Capacity has to be greater than 0!", str(ve.exception))

    def test_reserve_method_reserves_table_and_counts_people_sat_less_or_equal_to_capacity(self):
        people = [5, 10]
        self.assertFalse(self.table_3.is_reserved)
        for x in people:
            self.table_3.reserve(x)
            self.assertTrue(self.table_3.is_reserved)
            self.assertEqual(x, self.table_3.number_of_people)
            self.table_3.is_reserved = False

    def test_reserve_method_people_more_than_capacity_zero_negative_value(self):
        self.assertFalse(self.table_3.is_reserved)
        self.assertEqual(0, self.table_3.number_of_people)
        people = [-1, 0, 11]
        for x in people:
            self.table_3.reserve(x)
            self.assertFalse(self.table_3.is_reserved)
            self.assertEqual(0, self.table_3.number_of_people)

    def test_order_food(self):
        mixed = Cake('Mixed', 9.90)
        diet = Bread('Diet', 5.45)
        self.table_3.order_food(mixed)
        self.table_3.order_food(diet)

        self.assertEqual(mixed, self.table_3.food_orders[0])
        self.assertEqual(diet, self.table_3.food_orders[1])
        self.assertEqual(2, len(self.table_3.food_orders))

    def test_order_drink(self):
        black = Tea('Black', 320, 'Black Tea')
        mineral = Water('Mineral', 500, 'Mountain')
        spring = Water('Spring', 450, 'Velingrad')
        self.table_51.order_drink(mineral)
        self.table_51.order_drink(black)
        self.table_51.order_drink(spring)

        self.assertEqual(black, self.table_51.drink_orders[1])
        self.assertEqual(mineral, self.table_51.drink_orders[0])
        self.assertEqual(3, len(self.table_51.drink_orders))

    def test_get_bill(self):
        black = Tea('Black', 320, 'Black Tea')
        mineral = Water('Mineral', 500, 'Mountain')
        spring = Water('Spring', 450, 'Velingrad')
        mixed = Cake('Mixed', 9.90)
        diet = Bread('Diet', 5.45)
        self.table_51.order_food(mixed)
        self.table_51.order_food(diet)
        self.table_51.order_drink(mineral)
        self.table_51.order_drink(black)
        self.table_51.order_drink(spring)

        food_bill = 15.35
        drink_bill = 5.50
        expected = food_bill + drink_bill
        actual = self.table_51.get_bill()
        self.assertEqual(expected, actual)

    def test_clear_method(self):
        self.assertFalse(self.table_51.is_reserved)
        self.assertEqual(0, self.table_51.number_of_people)
        self.assertEqual([], self.table_51.drink_orders)
        self.assertEqual([], self.table_51.food_orders)

        self.table_51.reserve(8)
        black = Tea('Black', 320, 'Black Tea')
        mineral = Water('Mineral', 500, 'Mountain')
        spring = Water('Spring', 450, 'Velingrad')
        mixed = Cake('Mixed', 9.90)
        diet = Bread('Diet', 5.45)
        self.table_51.order_food(mixed)
        self.table_51.order_food(diet)
        self.table_51.order_drink(mineral)
        self.table_51.order_drink(black)
        self.table_51.order_drink(spring)

        self.assertTrue(self.table_51.is_reserved)
        self.assertEqual(8, self.table_51.number_of_people)
        self.assertEqual(spring, self.table_51.drink_orders[2])
        self.assertEqual(2, len(self.table_51.food_orders))

        self.table_51.clear()

        self.assertFalse(self.table_51.is_reserved)
        self.assertEqual(0, self.table_51.number_of_people)
        self.assertEqual([], self.table_51.drink_orders)
        self.assertEqual([], self.table_51.food_orders)

    def test_free_table_info_method(self):
        table_1 = InsideTable(1, 4)
        table_2 = InsideTable(2, 8)
        table_6 = InsideTable(6, 5)
        table_3 = InsideTable(3, 10)
        table_51 = OutsideTable(51, 14)
        table_55 = OutsideTable(55, 6)
        table_100 = OutsideTable(100, 10)

        test_tables = [table_1, table_2, table_3, table_6, table_51, table_55, table_100]

        table_2.is_reserved = True
        table_100.is_reserved = True

        for table in test_tables:
            if table.is_reserved:
                expected = None
            else:
                expected = f"Table: {table.table_number}\nType: {table.type}\nCapacity: {table.capacity}"
            actual = table.free_table_info()
            self.assertEqual(actual, expected)

    def test_inside_table_proper_number(self):
        tests = [1, 30, 50]
        for x in tests:
            self.table_3.table_number = x
            self.assertEqual(x, self.table_3.table_number)

    def test_inside_table_not_valid_number_raises_value_error(self):
        tests = [-1, 0, 51, 5.5]
        for x in tests:
            with self.assertRaises(ValueError) as ve:
                self.table_3.table_number = x
            self.assertEqual("Inside table's number must be between 1 and 50 inclusive!", str(ve.exception))

    def test_outside_table_proper_number(self):
        tests = [51, 60, 100]
        for x in tests:
            self.table_51.table_number = x
            self.assertEqual(x, self.table_51.table_number)

    def test_outside_table_not_valid_number_raises_value_error(self):
        tests = [-1, 0, 50, 5.5, 59.5, 101]
        for x in tests:
            with self.assertRaises(ValueError) as ve:
                self.table_51.table_number = x
            self.assertEqual("Outside table's number must be between 51 and 100 inclusive!", str(ve.exception))


if __name__ == '__main__':
    unittest.main()
