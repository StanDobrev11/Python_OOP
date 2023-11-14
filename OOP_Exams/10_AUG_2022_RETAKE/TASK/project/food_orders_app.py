from typing import List

from project.client import Client
from project.meals.meal import Meal


class FoodOrdersApp:
    _MEALS = ["Starter", "MainDish", "Dessert"]
    __receipt_id = 0

    def __init__(self):
        self.menu: List[Meal] = []
        self.clients_list: List[Client] = []

    def register_client(self, client_phone_number: str):
        """ Creates a client (object) and adds it to the client list. """
        if client_phone_number in [client.phone_number for client in self.clients_list]:
            raise Exception("The client has already been registered!")

        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)

        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        """ Adds all the meals (objects) given to the menu list. """
        for meal in meals:
            if meal.__class__.__name__ in self._MEALS:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        return '\n'.join(meal.details() for meal in self.menu)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        """
        The client attempts to order food.
        All clients can add any meal that is on the menu if there is enough quantity.
        :param client_phone_number: Client's phone number
        :param meal_names_and_quantities: {meal_name: quantity, meal_name: quantity, ...}
        """
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        try:
            client = self.__get_client(client_phone_number)
        except IndexError:
            self.register_client(client_phone_number)
            client = self.__get_client(client_phone_number)

        for name, quantity_ordered in meal_names_and_quantities.items():

            try:
                meal = [m for m in self.menu if m.name == name][0]
            except IndexError:
                self.__reset_meal_quantities(client)
                self.__reset_bill_and_cart(client)
                raise Exception(f"{name} is not on the menu!")

            if meal.quantity < quantity_ordered:
                self.__reset_meal_quantities(client)
                self.__reset_bill_and_cart(client)
                raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal.name}!")

            if name not in client.meal_order:
                client.meal_order[name] = 0
            client.meal_order[name] += quantity_ordered

            if meal not in client.shopping_cart:
                client.shopping_cart.append(meal)

            client.bill += meal.price * quantity_ordered
            meal.quantity -= quantity_ordered

        return f"Client {client.phone_number} successfully ordered {', '.join(meal.name for meal in client.shopping_cart)} for {client.bill :.2f}lv."

    def __get_client(self, number):
        return [c for c in self.clients_list if c.phone_number == number][0]

    @staticmethod
    def __reset_meal_quantities(client):
        for ordered_meal in client.shopping_cart:
            ordered_meal.quantity += client.meal_order[ordered_meal.name]

    @staticmethod
    def __reset_bill_and_cart(client):
        client.bill = 0
        client.shopping_cart = []
        client.meal_order = {}

    def cancel_order(self, client_phone_number: str):

        client = self.__get_client(client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        self.__reset_meal_quantities(client)
        self.__reset_bill_and_cart(client)
        return f"Client {client_phone_number} successfully canceled his order."

    @property
    def __get_receipt_id(self):
        self.__receipt_id += 1
        return self.__receipt_id

    def finish_order(self, client_phone_number: str):

        client = self.__get_client(client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        total_paid = client.bill
        self.__reset_bill_and_cart(client)
        return f"Receipt #{self.__get_receipt_id} with total amount of {total_paid :.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
