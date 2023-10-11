class Vehicle:
    DEFAULT_FUEL_CONSUMPTION: float = 1.25

    def __init__(self, fuel: float, horse_power: int) -> None:
        self.fuel = fuel  # quantity of fuel in a specific vehicle
        self.horse_power = horse_power
        self.fuel_consumption = self.__class__.DEFAULT_FUEL_CONSUMPTION  # fuel consumption per kilometer

    def drive(self, kilometers: int) -> None:
        fuel_needed = kilometers * self.__class__.DEFAULT_FUEL_CONSUMPTION

        if self.fuel >= fuel_needed:
            self.fuel -= fuel_needed
