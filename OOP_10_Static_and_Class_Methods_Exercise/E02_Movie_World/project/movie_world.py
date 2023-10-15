from project.customer import Customer
from project.dvd import DVD
from typing import List


class MovieWorld:
    __DVD_CAPACITY = 15
    __CUSTOMER_CAPACITY = 10

    def __init__(self, name: str) -> None:
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []
        self.__dvd_capacity = 15
        self.__customer_capacity = 10

    @staticmethod
    def dvd_capacity():
        return MovieWorld.__DVD_CAPACITY

    @staticmethod
    def customer_capacity():
        return MovieWorld.__CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer) -> None:
        """add the customer if capacity not exceeded"""
        if len(self.customers) < MovieWorld.__CUSTOMER_CAPACITY:
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD) -> None:
        """add the DVD if capacity not exceeded"""
        if len(self.dvds) < MovieWorld.__DVD_CAPACITY:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int) -> str:
        dvd = [d for d in self.dvds if d.id == dvd_id][0]
        customer = [c for c in self.customers if c.id == customer_id][0]

        if dvd.is_rented:
            if dvd in customer.rented_dvds:
                return f"{customer.name} has already rented {dvd.name}"
            else:
                return "DVD is already rented"

        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int) -> str:
        dvd = [d for d in self.dvds if d.id == dvd_id][0]
        customer = [c for c in self.customers if c.id == customer_id][0]
        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"

        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False
        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self) -> str:
        result_str = '\n'.join(f"{customer}" for customer in self.customers)
        result_str += '\n' + '\n'.join(f"{dvd}" for dvd in self.dvds)
        return result_str
