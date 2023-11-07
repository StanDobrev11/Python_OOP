class Appliance:
    def __init__(self, cost: float):
        self.cost = cost
        self.monthly_cost = self.get_monthly_expense()

    def get_monthly_expense(self):
        return self.cost * 30
