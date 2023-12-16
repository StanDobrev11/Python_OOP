from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):

    def __init__(self, name: str):
        super().__init__(name, 540)


if __name__ == '__main__':
    s = ScubaDiver('Ivan')
    print()