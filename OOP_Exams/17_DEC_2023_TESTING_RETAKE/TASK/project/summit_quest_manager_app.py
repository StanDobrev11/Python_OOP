from typing import List

from project.climbers.arctic_climber import ArcticClimber
from project.climbers.base_climber import BaseClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.base_peak import BasePeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    CLIMBER_TYPES = {'ArcticClimber': ArcticClimber, 'SummitClimber': SummitClimber}
    PEAK_TYPES = {'ArcticPeak': ArcticPeak, 'SummitPeak': SummitPeak}

    def __init__(self):
        self.climbers: List[BaseClimber] = []
        self.peaks: List[BasePeak] = []

    def register_climber(self, climber_type: str, climber_name: str):
        """The method creates a climber of the given type and adds it to the climbers collection. """

        if climber_type not in self.CLIMBER_TYPES:
            return f"{climber_type} doesn't exist in our register."

        if climber_name in [climber.name for climber in self.climbers]:
            return f"{climber_name} has been already registered."

        climber = self.CLIMBER_TYPES[climber_type](climber_name)
        self.climbers.append(climber)
        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        """The method creates a peak of the given type and adds them to the peaks collection.
        The method is responsible for allowing a new peak to climb."""

        if peak_type not in self.PEAK_TYPES:
            return f"{peak_type} is unknown type of peaks."

        peak = self.PEAK_TYPES[peak_type](peak_name, peak_elevation)
        self.peaks.append(peak)
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):
        """The method is responsible for verifying if every climber has the required gear for each peak."""

        peak = [peak for peak in self.peaks if peak_name == peak.name][0]

        if set(peak.RECOMMENDED_GEAR[peak.summit_type]).issubset(set(gear)):
            return f"{climber_name} is prepared to climb {peak_name}."
        else:
            missing_gear = set(peak.RECOMMENDED_GEAR[peak.summit_type]).difference(set(gear))
            return (f"{climber_name} is not prepared to climb {peak_name}. "
                    f"Missing gear: {', '.join(sorted(missing_gear))}.")

    def perform_climbing(self, climber_name: str, peak_name: str):

        try:
            climber = [climber for climber in self.climbers if climber_name == climber.name][0]
        except IndexError:
            return f"Climber {climber_name} is not registered yet."

        try:
            peak = [peak for peak in self.peaks if peak_name == peak.name][0]
        except IndexError:
            return f"Peak {peak_name} is not part of the wish list."

        if climber.can_climb() and climber.is_prepared:
            climber.climb(peak)
            return f"{climber_name} conquered {peak_name} which difficulty level is {peak.difficulty_level}."
        else:
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

    def get_statistics(self):

        total_peaks_climbed = sum(len(climber.conquered_peaks) for climber in self.climbers)

        text = [f"Total climbed peaks: {total_peaks_climbed}"]
        text += ["**Climber's statistics:**"]
        text += [str(climber) for climber in self.climbers if climber.conquered_peaks]

        return '\n'.join(text)