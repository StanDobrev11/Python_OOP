from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):
    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, 9)

    @property
    def weight_gain(self):
        return 3

    @property
    def service(self):
        return "MainService"
