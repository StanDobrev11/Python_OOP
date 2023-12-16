from project.climbers.base_climber import BaseClimber


class SummitClimber(BaseClimber):

    def __init__(self, name: str):
        super().__init__(name, 150)

    def climb(self, peak):
        if peak.difficulty_level == 'Extreme':
            self.strength -= 30 * 2.5
        # elif peak.difficulty_level == 'Advance':
        else:
            self.strength -= 30 * 1.3

        self.conquered_peaks.append(peak.name)
