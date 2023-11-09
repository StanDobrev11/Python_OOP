from typing import List

from project.baked_food.baked_food import BakedFood
from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.drink import Drink
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table


class Bakery:
    FOOD_TYPES = {'Bread': Bread, 'Cake': Cake}
    DRINK_TYPES = {'Tea': Tea, 'Water': Water}
    TABLE_TYPES = {"InsideTable": InsideTable, "OutsideTable": OutsideTable}

    def __init__(self, name: str):
        self.name = name
        self.food_menu: List[BakedFood] = []
        self.drinks_menu: List[Drink] = []
        self.tables_repository: List[Table] = []
        self.total_income: int = 0

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if value.strip() == "":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float) -> str:
        """Creates food with the correct type and adds it to the menu"""
        if food_type in self.FOOD_TYPES:
            try:
                if [food for food in self.food_menu if food.name == name and food.type == food_type][0]:
                    raise Exception(f"{food_type} {name} is already in the menu!")
            except IndexError:
                food = self.FOOD_TYPES[food_type](name, price)
                self.food_menu.append(food)
                return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str) -> str:
        """Creates drink with the correct type and adds it to the menu"""
        if drink_type in self.DRINK_TYPES:
            try:
                if [drink for drink in self.drinks_menu if drink.name == name and drink.type == drink_type][0]:
                    raise Exception(f"{drink_type} {name} is already in the menu!")
            except IndexError:
                drink = self.DRINK_TYPES[drink_type](name, portion, brand)
                self.drinks_menu.append(drink)
                return f"Added {name} ({drink.brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int) -> str:
        """Creates a table with the correct type, adds it to the table repository"""
        if table_type in self.TABLE_TYPES:
            try:
                if [table for table in self.tables_repository if table.table_number == table_number][0]:
                    raise Exception(f"Table {table_number} is already in the bakery!")
            except IndexError:

                table = self.TABLE_TYPES[table_type](table_number, capacity)
                self.tables_repository.append(table)
                return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int) -> str:
        """Finds the first possible table which is not reserved,
        and its capacity is enough for the number of people provided and reserves the table"""
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
        else:
            return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names) -> str:
        try:
            table = [table for table in self.tables_repository if table.table_number == table_number][0]
        except IndexError:
            return f"Could not find table {table_number}"

        table.is_reserved = True
        food_in_menu = []
        food_not_in_menu = []
        text = f'Table {table.table_number} ordered:\n'
        for food_name in food_names:
            try:
                food = [food for food in self.food_menu if food.name == food_name][0]
                food_in_menu.append(food)
                table.order_food(food)
            except IndexError:
                food_not_in_menu.append(food_name)

        text += '\n'.join(food.__repr__() for food in food_in_menu)
        text += f"\n{self.name} does not have in the menu:\n"
        text += '\n'.join(food_not_in_menu)
        return text

    def order_drink(self, table_number: int, *drink_names) -> str:
        try:
            table = [table for table in self.tables_repository if table.table_number == table_number][0]
        except IndexError:
            return f"Could not find table {table_number}"

        table.is_reserved = True
        drink_in_menu = []
        drink_not_in_menu = []
        text = f'Table {table.table_number} ordered:\n'
        for drink_name in drink_names:
            try:
                drink = [drink for drink in self.drinks_menu if drink.name == drink_name][0]
                drink_in_menu.append(drink)
                table.order_drink(drink)
            except IndexError:
                drink_not_in_menu.append(drink_name)

        text += '\n'.join(drink.__repr__() for drink in drink_in_menu)
        text += f"\n{self.name} does not have in the menu:\n"
        text += '\n'.join(drink_not_in_menu)
        return text

    def leave_table(self, table_number: int):
        try:
            table = [table for table in self.tables_repository if table.table_number == table_number][0]
        except IndexError:
            return

        bill = table.get_bill()
        self.total_income += bill
        table.clear()
        return f"Table: {table_number}\nBill: {bill :.2f}"

    def get_free_tables_info(self):
        free_tables = []
        for table in self.tables_repository:
            if not table.is_reserved:
                free_tables.append(table)

        return '\n'.join(table.free_table_info() for table in free_tables)

    def get_total_income(self):
        return f"{self.total_income :.2f}"
