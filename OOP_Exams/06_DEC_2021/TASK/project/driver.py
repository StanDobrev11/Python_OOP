from project.car.car import Car


class Driver:
    def __init__(self, name: str):
        self.name = name
        self.car: Car or None = None  # only one car per driver
        self.number_of_wins: int = 0
        self.has_car = False

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if value.strip() == '':
            raise ValueError("Name should contain at least one character!")
        self.__name = value

    def assign_car(self, car: Car):
        self.car = car
        self.has_car = True

    def remove_car(self):
        self.car = None
        self.has_car = False
