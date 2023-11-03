import math

from project.computer_types.computer import Computer


class Laptop(Computer):
    _processors_prices = {
        "AMD Ryzen 9 5950X": 900,
        "Intel Core i9-11900H": 1050,
        "Apple M1 Pro": 1200,
    }
    _max_ram_capacity = 64
    _ram_prices = {2 ** power_count: 100 * power_count for power_count in
                   range(1, int(math.log(_max_ram_capacity * 2, 2)))}

    def update_price(self):
        self.price = self.__class__._processors_prices[self.processor] + self.__class__._ram_prices[self.ram]

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.__class__._processors_prices:
            raise ValueError(f"{processor} is not compatible with laptop {self.manufacturer} {self.model}!")
        if ram not in self.__class__._ram_prices:
            raise ValueError(f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")
        self.processor = processor
        self.ram = ram
        self.update_price()
        return f"Created {self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM for {self.price}$."
