from project.peaks.base_peak import BasePeak


class SummitPeak(BasePeak):

    def calculate_difficulty_level(self):
        if self.elevation > 2500:
            return 'Extreme'
        elif self.elevation >= 1500:
            return 'Advanced'

        # return 'Extreme' if self.elevation > 2500 else 'Advanced'
