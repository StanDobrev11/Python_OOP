class Vehicle:
    DEFAULT_FUEL_CONSUMPTION: float = 1.25

    def __init__(self, fuel: float, horse_power: int):
        self.fuel = fuel  # quantity of fuel in a specific vehicle
        self.horse_power = horse_power
        self.fuel_consumption = self.__class__.DEFAULT_FUEL_CONSUMPTION  # fuel consumption per kilometer

    def drive(self, kilometers: int):
        self.fuel_consumption = self.__class__.DEFAULT_FUEL_CONSUMPTION * kilometers
        self.fuel = 0 if self.fuel - self.fuel_consumption <= 0 else self.fuel - self.fuel_consumption

