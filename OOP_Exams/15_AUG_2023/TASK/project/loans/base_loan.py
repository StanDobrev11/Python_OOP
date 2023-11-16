from abc import ABC, abstractmethod


class BaseLoan(ABC):
    __INTEREST_RATES_INCREMENT = {"StudentLoan": 0.2, "MortgageLoan": 0.5}

    @abstractmethod
    def __init__(self, interest_rate: float, amount: float):
        self.interest_rate = interest_rate
        self.amount = amount

    @property
    def loan_type(self):
        return self.__class__.__name__

    def increase_interest_rate(self):
        """Method increases the loan’s interest rate. Keep in mind that each type of loan implements
        the method differently."""
        self.interest_rate += self.__INTEREST_RATES_INCREMENT[self.loan_type]
