import math

from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    _processors_prices = {
        "AMD Ryzen 7 5700G": 500,
        "Intel Core i5-12600K": 600,
        "Apple M1 Max": 1800,
    }
    _max_ram_capacity = 128
    _ram_prices = {2 ** power_count: 100 * power_count for power_count in
                   range(1, int(math.log(_max_ram_capacity * 2, 2)))}

    @property
    def type(self):
        return "desktop computer"
