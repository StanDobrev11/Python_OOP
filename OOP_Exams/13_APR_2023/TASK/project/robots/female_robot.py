from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, 7)

    @property
    def weight_gain(self):
        return 1

    @property
    def service(self):
        return "SecondaryService"
