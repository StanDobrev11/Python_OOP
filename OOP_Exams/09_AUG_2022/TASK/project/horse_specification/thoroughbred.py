from project.horse_specification.horse import Horse


class Thoroughbred(Horse):

    @property
    def training_gain(self):
        return 2
