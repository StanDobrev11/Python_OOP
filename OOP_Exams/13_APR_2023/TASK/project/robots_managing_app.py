from typing import List

from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICE = {"MainService": MainService, "SecondaryService": SecondaryService}
    VALID_ROBOTS = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}

    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    def add_service(self, service_type: str, name: str):
        """The method creates a service of the given type and adds it to the services' collection."""

        if service_type not in self.VALID_SERVICE:
            raise Exception("Invalid service type!")

        service = self.VALID_SERVICE[service_type](name)
        self.services.append(service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        """The method creates a robot of the given type and adds it to the robots' collection."""

        if robot_type not in self.VALID_ROBOTS:
            raise Exception("Invalid robot type!")

        robot = self.VALID_ROBOTS[robot_type](name, kind, price)
        self.robots.append(robot)
        return f"{robot_type} is successfully added."

    def __get_service(self, service_name: str):
        return [s for s in self.services if s.name == service_name][0]

    def __get_robot_from_managing_app(self, robot_name: str):
        return [r for r in self.robots if r.name == robot_name][0]

    @staticmethod
    def __get_robot_from_service(robot_name: str, service: BaseService):
        return [r for r in service.robots if r.name == robot_name][0]

    @staticmethod
    def __match_service_and_robot(robot: BaseRobot, service: BaseService):
        if service.loan_type == robot.service:
            return True

    @staticmethod
    def __available_service_capacity(service: BaseService):
        return service.capacity > len(service.robots)

    def add_robot_to_service(self, robot_name: str, service_name: str):
        """The method adds the robot with the given name to the service if there is a capacity for that."""

        robot = self.__get_robot_from_managing_app(robot_name)
        service = self.__get_service(service_name)

        if not self.__match_service_and_robot(robot, service):
            return "Unsuitable service."

        if not self.__available_service_capacity(service):
            raise Exception(f"Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        """The method removes the robot with the given name from the service."""

        service = self.__get_service(service_name)

        try:
            robot = self.__get_robot_from_service(robot_name, service)
        except IndexError:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        """The method feeds all robots from the service."""

        service = self.__get_service(service_name)

        for robot in service.robots:
            robot.eating()

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        """The method calculates the price of all robots that are in the service."""

        service = self.__get_service(service_name)
        total_price = sum(robot.price for robot in service.robots)

        return f"The value of service {service_name} is {total_price :.2f}."

    def __str__(self):
        text = []
        for service in self.services:
            text.append(service.details())

        return '\n'.join(text)
