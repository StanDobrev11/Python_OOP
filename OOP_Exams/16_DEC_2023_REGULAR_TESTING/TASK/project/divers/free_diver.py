from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):

    def __init__(self, name: str):
        super().__init__(name, 120)
