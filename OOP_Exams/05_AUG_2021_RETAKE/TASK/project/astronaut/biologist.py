from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):

    def __init__(self, name: str):
        super().__init__(name, 70)

    @property
    def oxygen_consumption(self):
        return 5
