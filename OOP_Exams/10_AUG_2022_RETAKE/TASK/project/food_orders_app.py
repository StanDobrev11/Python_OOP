from typing import List

from project.client import Client
from project.meals.meal import Meal


class FoodOrdersApp:
    _MEALS = ["Starter", "MainDish", "Dessert"]

    def __init__(self):
        self.menu: List[Meal] = []
        self.client_list: List[Client] = []

    def is_menu_ready(self):
        if len(self.menu) >= 5:
            return True
        raise Exception("The menu is not ready!")

    def is_client_registered(self, phone_number: str):
        if phone_number in [client.phone_number for client in self.client_list]:
            raise Exception("The client has already been registered!")
        return False

    def get_registered_client(self, phone_number: str):
        return [c for c in self.client_list if c.phone_number == phone_number][0]

    @staticmethod
    def reset_clients_cart_and_bill(client: Client):
        client.shopping_cart = []
        client.bill = 0

    def register_client(self, phone_number: str):
        """ Creates a client (object) and adds it to the client list. """

        if not self.is_client_registered(phone_number):
            new_client = Client(phone_number)
            self.client_list.append(new_client)

            return f"Client {phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        """ Adds all the meals (objects) given to the menu list. """
        for meal in meals:
            if meal.__class__.__name__ in self._MEALS:
                self.menu.append(meal)

    def show_menu(self):
        if not self.is_menu_ready:
            raise Exception("The menu is not ready!")

        return '\n'.join(meal.details() for meal in self.menu)

    def add_meals_to_shopping_cart(self, number: str, **meals):
        """
        The client attempts to order food.
        All clients can add any meal that is on the menu if there is enough quantity.
        :param number: Client's phone number
        :param meals: {meal_name: quantity, meal_name: quantity, ...}
        """
        if self.is_menu_ready():
            try:
                client = self.get_registered_client(number)
            except IndexError:
                self.register_client(number)
                client = self.get_registered_client(number)

            for name, qtity in meals.items():
                if name not in [meal.name for meal in self.menu]:
                    self.reset_clients_cart_and_bill(client)
                    raise Exception(f"{name} is not on the menu!")

                meal = [m for m in self.menu if m.name == name][0]
                if qtity > meal.quantity:
                    self.reset_clients_cart_and_bill(client)
                    raise Exception(f"Not enough quantity of {meal.type}: {meal.name}!")

                client.shopping_cart.append(meal)
                client.bill += meal.price * qtity
                meal.quantity -= qtity

            return f"Client {client.phone_number} successfully ordered {', '.join(meal.name for meal in client.shopping_cart)} for {client.bill :.2f}lv."
