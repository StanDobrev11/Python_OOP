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

    @property
    def processor(self):
        return self.__processor

    @processor.setter
    def processor(self, value):
        if value not in self.__class__._processors_prices and value is not None:
            raise ValueError(f"{value} is not compatible with laptop {self.manufacturer} {self.model}!")
        self.__processor = value

    @property
    def ram(self):
        return self.__ram

    @ram.setter
    def ram(self, value):
        if value not in self.__class__._ram_prices and value is not None:
            raise ValueError(f"{value}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")
        self.__ram = value
