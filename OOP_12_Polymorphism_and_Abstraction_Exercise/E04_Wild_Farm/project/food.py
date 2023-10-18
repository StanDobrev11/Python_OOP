from abc import ABC, abstractmethod


class Food(ABC):
    def __init__(self, quantity: int) -> None:
        self.quantity = quantity

    @abstractmethod
    def just_abstract(self):
        pass


class Vegetable(Food):
    def just_abstract(self):
        pass


class Fruit(Food):
    def just_abstract(self):
        pass


class Meat(Food):
    def just_abstract(self):
        pass


class Seed(Food):
    def just_abstract(self):
        pass
