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
    def type(self):
        return "laptop"
