from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    def __init__(self, budget: int) -> None:
        self.is_registered = False
        self.budget = budget

    @property
    def budget(self) -> int:
        return self.__budget

    @budget.setter
    def budget(self, amount: int) -> None:
        if amount < 1_000_000 and not self.is_registered:
            raise ValueError("F1 is an expensive sport, find more sponsors!")

        self.__budget = amount

    @abstractmethod
    def calculate_revenue_after_race(self, race_pos: int) -> int:
        pass

    @abstractmethod
    def add_revenue_to_budget(self, race_pos: int) -> str:
        pass
