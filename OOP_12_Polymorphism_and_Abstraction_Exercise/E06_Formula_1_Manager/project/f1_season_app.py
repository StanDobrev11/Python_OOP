from typing import Dict

from project.formula_teams.formula_team import FormulaTeam
from project.formula_teams.mercedes_team import MercedesTeam
from project.formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp:
    VALID_TEAMS = {"Red Bull": RedBullTeam, "Mercedes": MercedesTeam}

    def __init__(self, red_bull_team: RedBullTeam = None, mercedes_team: MercedesTeam = None) -> None:
        self.red_bull_team = red_bull_team
        self.mercedes_team = mercedes_team
        self._registered_teams: Dict[str: FormulaTeam] = {}

    def register_team_for_season(self, team_name: str, budget: int) -> str:
        if team_name not in F1SeasonApp.VALID_TEAMS:
            raise ValueError("Invalid team name!")

        self._registered_teams[team_name] = self.create_team(team_name, budget)
        self._registered_teams[team_name].is_registered = True
        return f"{team_name} has joined the new F1 season."

    @staticmethod
    def create_team(team_name: str, budget: int) -> RedBullTeam or MercedesTeam:
        return F1SeasonApp.VALID_TEAMS[team_name](budget)

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int) -> str:
        if len(self._registered_teams) != 2:
            raise Exception("Not all teams have registered for the season.")

        return (f"Red Bull: {self._registered_teams['Red Bull'].add_revenue_to_budget(red_bull_pos)}. "
                f"Mercedes: {self._registered_teams['Mercedes'].add_revenue_to_budget(mercedes_pos)}. "
                f"{'Red Bull' if red_bull_pos < mercedes_pos else 'Mercedes'} is ahead at the {race_name} race.")
