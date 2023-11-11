from typing import List

from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    CAR_TYPES = {'MuscleCar': MuscleCar, 'SportsCar': SportsCar}

    def __init__(self):
        self.cars: List[Car] = []
        self.drivers: List[Driver] = []
        self.races: List[Race] = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type in self.CAR_TYPES:
            try:
                car = [c for c in self.cars if c.model == model][0]
                if car:
                    raise Exception(f"Car {model} is already created!")
            except IndexError:
                car = self.CAR_TYPES[car_type](model, speed_limit)
                self.cars.append(car)
                return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        try:
            if [d for d in self.drivers if d.name == driver_name][0]:
                raise Exception(f"Driver {driver_name} is already created!")
        except IndexError:
            driver = Driver(driver_name)
            self.drivers.append(driver)
            return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        try:
            if [r for r in self.races if r.name == race_name][0]:
                raise Exception(f"Race {race_name} is already created!")
        except IndexError:
            race = Race(race_name)
            self.races.append(race)
            return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        """ Set the last car added from the given type to the driver with the given name (if they both exist)."""
        # check if both exists
        try:
            driver = [d for d in self.drivers if d.name == driver_name][0]
        except IndexError:
            raise Exception(f"Driver {driver_name} could not be found!")

        try:
            car = [c for c in self.cars if c.type == car_type and not c.is_taken][-1]
        except IndexError:
            raise Exception(f"Car {car_type} could not be found!")

        if driver.has_car:
            old_car = driver.car
            old_car.remove_driver()
            car.assign_driver()
            driver.assign_car(car)
            return f"Driver {driver_name} changed his car from {old_car.model} to {car.model}."
        else:
            driver.assign_car(car)
            car.assign_driver()
            return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        try:
            race = [r for r in self.races if r.name == race_name][0]
        except IndexError:
            raise Exception(f"Race {race_name} could not be found!")

        try:
            driver = [d for d in self.drivers if d.name == driver_name][0]
        except IndexError:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not driver.has_car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        for drv in race.drivers:
            if drv.name == driver_name:
                raise Exception(f"Driver {driver_name} is already added in {race_name} race.")

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

        # try:
        #     drv = [drv for drv in race.drivers if drv.name == driver_name][0]
        #     if drv:
        #         raise Exception(f"Driver {driver_name} is already added in {race_name} race.")
        # except IndexError:
        #     race.drivers.append(driver)
        #     return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        try:
            race = [r for r in self.races if r.name == race_name][0]
        except IndexError:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        fastest_drivers = sorted(race.drivers, reverse=True)[:3]

        winning_text = ''
        for driver in fastest_drivers:
            driver.number_of_wins += 1
            winning_text += f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.\n"

        return winning_text.strip()
