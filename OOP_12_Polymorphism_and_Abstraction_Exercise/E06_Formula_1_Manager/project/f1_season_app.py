from typing import Dict

from project.formula_teams.formula_team import FormulaTeam
from project.formula_teams.mercedes_team import MercedesTeam
from project.formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp:
    VALID_TEAMS = {"Red Bull": RedBullTeam, "Mercedes": MercedesTeam}

    def __init__(self) -> None:
        self.red_bull_team = None
        self.mercedes_team = None

    def register_team_for_season(self, team_name: str, budget: int) -> str:
        if team_name not in F1SeasonApp.VALID_TEAMS:
            raise ValueError("Invalid team name!")

        if team_name == "Red Bull":
            self.red_bull_team = F1SeasonApp.VALID_TEAMS[team_name].create_team(budget)
        else:
            self.mercedes_team = F1SeasonApp.VALID_TEAMS[team_name].create_team(budget)

        return f"{team_name} has joined the new F1 season."

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int) -> str:
        if not self.mercedes_team or not self.red_bull_team:
            raise Exception("Not all teams have registered for the season.")

        return (f"Red Bull: {self.red_bull_team.calculate_revenue_after_race(red_bull_pos)}. "
                f"Mercedes: {self.mercedes_team.calculate_revenue_after_race(mercedes_pos)}. "
                f"{'Red Bull' if red_bull_pos < mercedes_pos else 'Mercedes'} is ahead at the {race_name} race.")
