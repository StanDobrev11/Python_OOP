from project.climbers.base_climber import BaseClimber


class ArcticClimber(BaseClimber):

    def __init__(self, name: str):
        super().__init__(name, 200)

    def climb(self, peak):
        if peak.difficulty_level == 'Extreme':
            self.strength -= 20 * 2
        # elif peak.difficulty_level == 'Advance':
        else:
            self.strength -= 20 * 1.5

        self.conquered_peaks.append(peak.name)

if __name__ == '__main__':
    ac = ArcticClimber('ivo')
    print(ac.can_climb())
    ac.strength = 100
    print(ac.can_climb())
    ac.strength = 99
    print(ac.can_climb())
    print(ac)
