from typing import List, Dict

from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):

    @property
    def sponsors(self) -> List[Dict]:
        return [{1: 1_000_000, 3: 500_000}, {5: 100_000, 7: 50_000}]

    @property
    def expenses(self) -> int:
        return 200_000
