from typing import List

from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    DELICACY_KINDS = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    BOOTH_KINDS = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income = 0  # total income of the pastry shop.

    def __check_for_existing_delicacy(self, name: str) -> bool:
        """ checks if existing and return bool """
        if name in [d.name for d in self.delicacies]:
            return True
        return False

    def __get_existing_delicacy(self, name: str):
        """ return existing delicacy """
        return [d for d in self.delicacies if d.name == name][0]

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        """ The method creates a delicacy of the given type and adds it to the delicacies' collection.
        All delicacy names should be unique. """

        if self.__check_for_existing_delicacy(name):
            raise Exception(f"{name} already exists!")

        if type_delicacy not in self.DELICACY_KINDS:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        delicacy = self.DELICACY_KINDS[type_delicacy](name, price)
        self.delicacies.append(delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def __check_for_existing_booth(self, number: int) -> bool:
        """ checks if existing and return bool """
        if number in [b.booth_number for b in self.booths]:
            return True
        return False

    def __get_existing_booth_by_number(self, number: int):
        """ return existing booth """
        return [b for b in self.booths if b.booth_number == number][0]

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        """ The method creates a booth of the given type and adds it to the booths' collection.
        All booth numbers should be unique. """

        if self.__check_for_existing_booth(booth_number):
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self.BOOTH_KINDS:
            raise Exception(f"{type_booth} is not a valid booth!")

        booth = self.BOOTH_KINDS[type_booth](booth_number, capacity)
        self.booths.append(booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        """ Finds the first booth that is not reserved and whose capacity is enough
        for the number of people provided and reserves it  """

        try:
            booth = [b for b in self.booths if b.capacity >= number_of_people and not b.is_reserved][0]
        except IndexError:
            raise Exception(f"No available booth for {number_of_people} people!")

        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        """ Finds the booth with the provided number and the delicacy with the provided name
         and orders the delicacy for that booth """

        try:
            booth = self.__get_existing_booth_by_number(booth_number)
        except IndexError:
            raise Exception(f"Could not find booth {booth_number}!")

        try:
            delicacy = self.__get_existing_delicacy(delicacy_name)
        except IndexError:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        booth.price_per_delicacy += delicacy.price
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        """ Calculates the bill for that booth taking the price for reservation and all the price of all orders.
        The bill is added to the pastry shop's total income.
        Removes all the ordered delicacies, frees the booth, and sets the price for reservation to 0 """

        booth = self.__get_existing_booth_by_number(booth_number)
        booth_income = booth.price_per_delicacy + booth.price_for_reservation

        self.income += booth_income
        booth.free_booth()

        return f"Booth {booth_number}:\nBill: {booth_income :.2f}lv."

    def get_income(self):
        """ Returns the total income for the pastry shop for all completed bills """

        return f"Income: {self.income :.2f}lv."
