from typing import List

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VEHICLE_TYPE = {'PassengerCar': PassengerCar, 'CargoVan': CargoVan}

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []  # [route, route_1, route_2,..., route_n]

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        """The method should create and add a new user to the users’ collection."""

        if driving_license_number in [user.driving_license_number for user in self.users]:
            return f"{driving_license_number} has already been registered to our platform."

        new_user = User(first_name, last_name, driving_license_number)
        self.users.append(new_user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        """The method should create and add a new vehicle to the vehicle collection."""

        if vehicle_type not in self.VEHICLE_TYPE:
            return f"Vehicle type {vehicle_type} is inaccessible."

        if license_plate_number in [vehicle.license_plate_number for vehicle in self.vehicles]:
            return f"{license_plate_number} belongs to another vehicle."

        new_vehicle = self.VEHICLE_TYPE[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(new_vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        """The method should create and add a new route to the routes’ collection."""

        filtered_routes = [r for r in self.routes if r.details == (start_point, end_point)]

        for route in filtered_routes:
            if route.__length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."

            elif route.__length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."

            elif route.__length > length:
                route.is_locked = True

        route_id = len(self.routes) + 1
        new_route = Route(start_point, end_point, length, route_id)
        self.routes.append(new_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
                  is_accident_happened: bool):
        """A user with the given driving license number will take a trip on the route with specified route id
        and vehicle with stated license plate number"""

        user = [u for u in self.users if u.driving_license_number == driving_license_number][0]
        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        vehicle = [v for v in self.vehicles if v.license_plate_number == license_plate_number][0]
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        route = [r for r in self.routes if r.route_id == route_id][0]
        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.__length)

        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count: int):
        """Repairs certain amount of vehicles"""

        damaged_vehicles = [v for v in self.vehicles if v.is_damaged]
        repaired = 0
        for vehicle in sorted(damaged_vehicles, key=lambda x: (x.brand, x.model)):
            if count == 0:
                break
            vehicle.change_status()
            vehicle.recharge()
            count -= 1
            repaired += 1

        return f"{repaired} vehicles were successfully repaired!"

    def users_report(self):
        """Returns information about each user from the users’ collection."""

        text = ["*** E-Drive-Rent ***"]
        text.extend(str(user) for user in sorted(self.users, key=lambda x: -x.rating))

        return '\n'.join(text)
