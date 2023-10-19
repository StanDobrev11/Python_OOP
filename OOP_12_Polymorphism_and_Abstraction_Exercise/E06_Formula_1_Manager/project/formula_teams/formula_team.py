from abc import ABC, abstractmethod
from typing import List, Dict


class FormulaTeam(ABC):
    def __init__(self, budget: int) -> None:
        self.is_registered = False
        self.budget = budget

    @property
    @abstractmethod
    def sponsors(self) -> List[Dict]:
        pass

    @property
    @abstractmethod
    def expenses(self) -> int:
        pass

    @property
    def budget(self) -> int:
        return self.__budget

    @budget.setter
    def budget(self, amount: int) -> None:
        if amount < 1_000_000 and not self.is_registered:
            raise ValueError("F1 is an expensive sport, find more sponsors!")

        self.__budget = amount

    def calculate_revenue_after_race(self, race_pos: int) -> str:
        awards = 0
        for idx in range(2):
            for psn, price in self.sponsors[idx].items():
                if race_pos <= psn:
                    awards += price
                    break

        race_revenue = awards - self.expenses
        self.add_revenue_to_budget(race_revenue)

        return f"The revenue after the race is {race_revenue}$. Current budget {self.budget}$"

    @classmethod
    def create_team(cls, budget: int):
        return cls(budget)

    def add_revenue_to_budget(self, race_revenue: int) -> None:
        self.budget += race_revenue
