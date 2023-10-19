from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    SPONSORS = [{1: 1_000_000, 3: 500_000}, {5: 100_000, 7: 50_000}]
    EXPENSES_PER_RACE = 200_000

    def calculate_revenue_after_race(self, race_pos: int) -> str:
        awards = 0
        for idx in range(2):
            for psn, price in MercedesTeam.SPONSORS[idx].items():
                if race_pos <= psn:
                    awards += price
                    break

        race_revenue = awards - MercedesTeam.EXPENSES_PER_RACE
        self.add_revenue_to_budget(race_revenue)

        return f"The revenue after the race is {race_revenue}$. Current budget {self.budget}$"
