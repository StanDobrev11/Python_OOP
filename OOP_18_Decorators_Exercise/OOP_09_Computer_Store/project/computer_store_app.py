from typing import List

from project.computer_types.computer import Computer
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    _valid_computer_types = {"Desktop Computer": DesktopComputer, "Laptop": Laptop}

    def __init__(self):
        self.warehouse: List[Computer] = []
        self.profits: int = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in self.__class__._valid_computer_types:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        computer = self.__class__._valid_computer_types[type_computer](manufacturer, model)
        config = computer.configure_computer(processor, ram)
        self.warehouse.append(computer)
        return config

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        for comp in self.warehouse:
            if comp.price <= client_budget and comp.processor == wanted_processor and comp.ram >= wanted_ram:
                self.profits += client_budget - comp.price
                self.warehouse.remove(comp)
                return f"{comp} sold for {client_budget}$."

        else:
            raise Exception("Sorry, we don't have a computer for you.")
