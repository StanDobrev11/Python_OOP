from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    SPONSORS = [{1: 1_500_000, 2: 800_000}, {8: 20_000, 10: 10_000}]
    EXPENSES_PER_RACE = 250_000

    def calculate_revenue_after_race(self, race_pos: int) -> int:
        awards = 0
        for idx in range(2):
            for psn, price in RedBullTeam.SPONSORS[idx].items():
                if race_pos <= psn:
                    awards += price
                    break

        race_revenue = awards - RedBullTeam.EXPENSES_PER_RACE
        return race_revenue

    def add_revenue_to_budget(self, race_pos: int) -> str:
        race_revenue = self.calculate_revenue_after_race(race_pos)
        self.budget += race_revenue

        return f"The revenue after the race is {race_revenue}$. Current budget {self.budget}$"
