from project.peaks.base_peak import BasePeak


class ArcticPeak(BasePeak):

    def calculate_difficulty_level(self):
        if self.elevation > 3000:
            return 'Extreme'
        elif self.elevation >= 2000:
            return 'Advanced'

        # return 'Extreme' if self.elevation > 3000 else 'Advanced'


if __name__ == '__main__':
    ap = ArcticPeak('ii', 10)
    print(ap.elevation)
    print(ap.difficulty_level)
    print(ap.get_recommended_gear())