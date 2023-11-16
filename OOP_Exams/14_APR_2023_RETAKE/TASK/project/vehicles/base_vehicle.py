from abc import ABC, abstractmethod


class BaseVehicle(ABC):

    def __init__(self, brand: str, model: str, license_plate_number: str, max_mileage: float):
        self.brand = brand
        self.model = model
        self.license_plate_number = license_plate_number
        self.max_mileage = max_mileage  # maximum mileage of the vehicle
        self.battery_level: int = 100  # the battery level of the vehicle.
        self.is_damaged = False  # the damage status of the vehicle

    @property
    def brand(self):

        return self.__brand

    @brand.setter
    def brand(self, value: str):
        if value.strip() == '':
            raise ValueError("Brand cannot be empty!")
        self.__brand = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value: str):
        if value.strip() == '':
            raise ValueError("Model cannot be empty!")
        self.__model = value

    @property
    def license_plate_number(self):
        return self.__license_plate_number

    @license_plate_number.setter
    def license_plate_number(self, value: str):
        if value.strip() == '':
            raise ValueError("License plate number is required!")
        self.__license_plate_number = value

    @abstractmethod
    def drive(self, mileage: float):
        """The method reduces the battery level by a certain percentage.
        Each type of vehicle implements this method differently."""
        ...

    def recharge(self):
        """This method restores the value of the battery level to 100%."""
        self.battery_level = 100

    def change_status(self):
        """This method sets the value of is_damaged."""
        self.is_damaged = not self.is_damaged

    def __str__(self):
        return (f"{self.brand} {self.model} "
                f"License plate: {self.license_plate_number} "
                f"Battery: {self.battery_level}% "
                f"Status: {'OK' if not self.is_damaged else 'Damaged'}")
