from typing import List

from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    DIVER_TYPES = {'FreeDiver': FreeDiver, 'ScubaDiver': ScubaDiver}
    FISH_TYPES = {'PredatoryFish': PredatoryFish, 'DeepSeaFish': DeepSeaFish}

    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        """ The method creates a diver of the given type and adds it to the divers collection """

        if diver_type not in self.DIVER_TYPES:
            return f"{diver_type} is not allowed in our competition."

        try:
            diver = [diver for diver in self.divers if diver.name == diver_name][0]
            return f"{diver_name} is already a participant -> {diver.kind}."
        except IndexError:
            diver = self.DIVER_TYPES[diver_type](diver_name)
            self.divers.append(diver)
            return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        """The method creates a fish of the given type and adds them to the fish collection.
        The method is responsible for allowing a new fish to chase into the competition."""

        if fish_type not in self.FISH_TYPES:
            return f"{fish_type} is forbidden for chasing in our competition."

        try:
            fish = [fish for fish in self.fish_list if fish.name == fish_name][0]
            return f"{fish_name} is already allowed as a {fish.kind}."
        except IndexError:
            fish = self.FISH_TYPES[fish_type](fish_name, points)
            self.fish_list.append(fish)
            return f"{fish_name} is allowed for chasing."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        """The method is responsible for allowing the specific diver to chase and attempt to catch a specific fish"""

        try:
            diver = [diver for diver in self.divers if diver.name == diver_name][0]
        except IndexError:
            return f"{diver_name} is not registered for the competition."

        try:
            fish = [fish for fish in self.fish_list if fish.name == fish_name][0]
        except IndexError:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."

        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."
            else:
                diver.miss(fish.time_to_catch)
                return f"{diver_name} missed a good {fish_name}."

        elif diver.oxygen_level > fish.time_to_catch:
            diver.hit(fish)
            return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        """Its main purpose is to scan through the collection of divers and identify those facing health issues"""

        count = 0

        for diver in self.divers:
            if diver.has_health_issue:
                diver.renew_oxy()
                diver.update_health_status()
                count += 1

        return f"Divers recovered: {count}"

    def diver_catch_report(self, diver_name: str):

        diver = [diver for diver in self.divers if diver.name == diver_name][0]

        result = f"**{diver_name} Catch Report**\n"
        result += '\n'.join(fish.fish_details() for fish in diver.catch)

        return result

    def competition_statistics(self):
        """Return information about each diver, arranging them in descending order based on competition_points.
        If more than one diver has the same number of points, further arrange them in descending order based
        on the count of catches. For divers with the same catch count, arrange them alphabetically by name.
        Return only divers that are in good health condition. """

        result = ["**Nautical Catch Challenge Statistics**"]

        filter_by_health = [diver for diver in self.divers if not diver.has_health_issue]

        for diver in sorted(filter_by_health, key=lambda x: (-x.competition_points, -len(x.catch))):
            result.append(str(diver))

        return '\n'.join(result)
