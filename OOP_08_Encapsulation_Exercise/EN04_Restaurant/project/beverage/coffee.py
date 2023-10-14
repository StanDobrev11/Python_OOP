from project.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.50

    def __init__(self, name: str, caffeine: float) -> None:
        super().__init__(name, milliliters=Coffee.MILLILITERS, price=Coffee.PRICE)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine
