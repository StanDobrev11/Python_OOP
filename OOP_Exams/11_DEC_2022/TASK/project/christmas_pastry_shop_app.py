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
        return next(d for d in self.delicacies if d.name == name)

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

    def __get_existing_booth(self, number: int):
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
