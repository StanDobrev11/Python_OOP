from project.animals.animal import Mammal
from project.food import Meat, Vegetable, Fruit


class Mouse(Mammal):

    def feed(self, food: "Vegetable" or "Fruit") -> None or str:
        if self.check_proper_food_type(food):
            self.food_consumption(food)
            self.increase_food_eaten(food)
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Dog(Mammal):

    def feed(self, food: "Meat") -> None or str:
        if self.check_proper_food_type(food):
            self.food_consumption(food)
            self.increase_food_eaten(food)
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Cat(Mammal):

    def feed(self, food: "Meat" or "Vegetable") -> None or str:
        if self.check_proper_food_type(food):
            self.food_consumption(food)
            self.increase_food_eaten(food)
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Tiger(Mammal):

    def feed(self, food: "Meat") -> None or str:
        if self.check_proper_food_type(food):
            self.food_consumption(food)
            self.increase_food_eaten(food)
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
