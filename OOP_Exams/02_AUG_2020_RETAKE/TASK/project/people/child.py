class Child:
    def __init__(self, food_cost: float, *toys_cost):
        self.food_cost = food_cost
        self.toys_cost = toys_cost
        self.cost = food_cost + sum(toys_cost)

    def get_monthly_expense(self):
        """ cost for a month """
        return self.cost * 30
