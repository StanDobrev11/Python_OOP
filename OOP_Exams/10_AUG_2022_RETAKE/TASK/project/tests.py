import unittest

from project.food_orders_app import FoodOrdersApp
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.starter import Starter


class TestFoodOrdersApp(unittest.TestCase):
    def setUp(self) -> None:
        self.f = FoodOrdersApp()
        self.f.register_client("0899999999")
        self.french_toast = Starter("French toast", 6.50, 5)
        self.hummus_and_avocado_sandwich = Starter("Hummus and Avocado Sandwich", 7.90)
        self.tortilla_with_beef_and_pork = MainDish("Tortilla with Beef and Pork", 12.50, 12)
        self.risotto_with_wild_mushrooms = MainDish("Risotto with Wild Mushrooms", 15)
        self.chocolate_cake_with_mascarpone = Dessert("Chocolate Cake with Mascarpone", 4.60, 17)
        self.chocolate_and_violets = Dessert("Chocolate and Violets", 5.20)

        self.food = {"Hummus and Avocado Sandwich": 5,
                     "Risotto with Wild Mushrooms": 1,
                     "Chocolate and Violets": 4}

        self.non_ex_food = {"Hummus and Avocado Sandwich": 5,
                            "Risotto with Wild Mushrooms": 1,
                            "Chocolate and Violets": 4,
                            "Non Existing": 5}

        self.greater_qtity_food = {"Hummus and Avocado Sandwich": 5,
                                   "Risotto with Wild Mushrooms": 1,
                                   "Chocolate and Violets": 4,
                                   "French toast": 10}

        self.four_meals = (
            self.french_toast,
            self.hummus_and_avocado_sandwich,
            self.tortilla_with_beef_and_pork,
            self.risotto_with_wild_mushrooms,
        )
        self.six_meals = (
            self.french_toast,
            self.hummus_and_avocado_sandwich,
            self.tortilla_with_beef_and_pork,
            self.risotto_with_wild_mushrooms,
            self.chocolate_cake_with_mascarpone,
            self.chocolate_and_violets
        )

    def test_add_meals_to_shopping_cart_menu_not_ready(self):
        self.f.add_meals_to_menu(*self.four_meals)

        with self.assertRaises(Exception) as ex:
            self.f.add_meals_to_shopping_cart('0899999999', **self.food)
        self.assertEqual("The menu is not ready!", str(ex.exception))

    def test_add_meals_to_cart_menu_ready_client_not_existing_raises_name_exception(self):
        self.f.add_meals_to_menu(*self.six_meals)

        with self.assertRaises(Exception) as ex:
            self.f.add_meals_to_shopping_cart('0888888888', **self.non_ex_food)

        self.assertEqual("Non Existing is not on the menu!", str(ex.exception))
        client = self.f.get_registered_client('0888888888')
        self.assertEqual([], client.shopping_cart)
        self.assertEqual(0, client.bill)

    def test_add_meals_to_cart_existing_client_raises_quantity_exception(self):
        self.f.add_meals_to_menu(*self.six_meals)

        client = self.f.get_registered_client('0899999999')
        self.assertEqual(0, client.bill)
        self.assertEqual([], client.shopping_cart)

        with self.assertRaises(Exception) as ex:
            self.f.add_meals_to_shopping_cart('0899999999', **self.greater_qtity_food)
        self.assertEqual("Not enough quantity of Starter: French toast!", str(ex.exception))

        self.assertEqual(0, client.bill)
        self.assertEqual([], client.shopping_cart)

    def test_add_meal_to_cart_success(self):
        self.f.add_meals_to_menu(*self.six_meals)
        test_meal = [m for m in self.f.menu if m.name == "Hummus and Avocado Sandwich"][0]
        self.assertEqual(60, test_meal.quantity)

        actual = self.f.add_meals_to_shopping_cart('0899999999', **self.food)
        expected = "Client 0899999999 successfully ordered Hummus and Avocado Sandwich, Risotto with Wild Mushrooms, Chocolate and Violets for 75.30lv."

        self.assertEqual(expected, actual)
        self.assertEqual(55, test_meal.quantity)


if __name__ == '__main__':
    unittest.main()
