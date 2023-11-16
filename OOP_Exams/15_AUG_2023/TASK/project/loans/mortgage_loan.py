from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    def __init__(self):
        super().__init__(3.5, 50000)
