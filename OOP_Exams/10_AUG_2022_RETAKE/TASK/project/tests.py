import unittest

from project.food_orders_app import FoodOrdersApp
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.starter import Starter


class TestFoodOrdersApp(unittest.TestCase):
    def setUp(self) -> None:
        self.f = FoodOrdersApp()
        self.f.register_client("0899999999")
        self.toast = Starter("toast", 6.50, 5)
        self.oats = Starter("oats", 7.90)
        self.pork = MainDish("pork", 12.50, 12)
        self.beef = MainDish("beef", 15)
        self.cake = Dessert("cake", 4.60, 17)
        self.coffee = Dessert("coffee", 5.20)

        self.food = {"toast": 5,
                     "pork": 1,
                     "cake": 4}

        self.additional_food = {"cake": 2,
                                "coffee": 2}

        self.non_ex_food = {"toast": 5,
                            "pork": 1,
                            "cake": 4,
                            "Non Existing": 5}

        self.greater_qtity_food = {"beef": 5,
                                   "pork": 1,
                                   "cake": 4,
                                   "toast": 10}

        self.four_meals = (
            self.toast,
            self.beef,
            self.pork,
            self.cake,
        )
        self.six_meals = (
            self.toast,
            self.oats,
            self.pork,
            self.beef,
            self.cake,
            self.coffee
        )

    def test_add_meals_to_shopping_cart_menu_not_ready(self):
        self.f.add_meals_to_menu(*self.four_meals)

        with self.assertRaises(Exception) as ex:
            self.f.add_meals_to_shopping_cart('0899999999', **self.food)
        self.assertEqual("The menu is not ready!", str(ex.exception))

    def test_client_throws_exception_adding_items(self):
        self.f.add_meals_to_menu(*self.six_meals)

        with self.assertRaises(ValueError) as ve:
            self.f.add_meals_to_shopping_cart('Not valid', **self.food)
        self.assertEqual("Invalid phone number!", str(ve.exception))

    def test_add_meals_to_cart_menu_ready_client_not_existing_raises_name_exception(self):
        self.f.add_meals_to_menu(*self.six_meals)

        with self.assertRaises(Exception) as ex:
            self.f.add_meals_to_shopping_cart('0888888888', **self.non_ex_food)

        self.assertEqual("Non Existing is not on the menu!", str(ex.exception))
        client = [c for c in self.f.clients_list if c.phone_number == '0888888888'][0]
        self.assertEqual([], client.shopping_cart)
        self.assertEqual(0, client.bill)
        self.assertEqual({}, client.meal_order)

    def test_add_meals_to_cart_existing_client_raises_quantity_exception(self):
        self.f.add_meals_to_menu(*self.six_meals)

        client = [c for c in self.f.clients_list if c.phone_number == '0899999999'][0]
        self.assertEqual(0, client.bill)
        self.assertEqual([], client.shopping_cart)

        with self.assertRaises(Exception) as ex:
            self.f.add_meals_to_shopping_cart('0899999999', **self.greater_qtity_food)
        self.assertEqual("Not enough quantity of Starter: toast!", str(ex.exception))

        self.assertEqual(0, client.bill)
        self.assertEqual([], client.shopping_cart)
        self.assertEqual({}, client.meal_order)

    def test_add_meal_to_cart_success(self):
        self.f.add_meals_to_menu(*self.six_meals)
        test_meal = [m for m in self.f.menu if m.name == "pork"][0]
        self.assertEqual(12, test_meal.quantity)

        actual = self.f.add_meals_to_shopping_cart('0899999999', **self.food)
        expected = "Client 0899999999 successfully ordered toast, pork, cake for 63.40lv."
        client = [c for c in self.f.clients_list if c.phone_number == '0899999999'][0]
        self.assertEqual(expected, actual)
        self.assertEqual(11, test_meal.quantity)
        self.assertEqual(3, len(client.meal_order))

    def test_add_additional_meal_success(self):
        self.f.add_meals_to_menu(*self.six_meals)
        self.f.add_meals_to_shopping_cart('0899999999', **self.food)
        actual = self.f.add_meals_to_shopping_cart('0899999999', **self.additional_food)
        expected = "Client 0899999999 successfully ordered toast, pork, cake, coffee for 83.00lv."
        self.assertEqual(expected, actual)
        client = [c for c in self.f.clients_list if c.phone_number == '0899999999'][0]
        test_meal = [m for m in self.f.menu if m.name == "cake"][0]
        self.assertEqual(4, len(client.shopping_cart))
        self.assertEqual(4, len(client.meal_order))
        self.assertEqual(11, test_meal.quantity)


if __name__ == '__main__':
    unittest.main()
