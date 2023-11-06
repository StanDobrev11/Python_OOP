class Appliance:
    def __init__(self, cost: float):
        self.cost = cost  # cost for single day

    def get_monthly_expense(self):
        """ cost for a month """
        return self.cost * 30
