from project.animals.animal import Bird
from project.food import Vegetable, Fruit, Seed, Meat


class Owl(Bird):

    def feed(self, food: "Meat") -> None or str:
        if self.check_proper_food_type(food):
            self.food_consumption(food)
            self.increase_food_eaten(food)
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Hen(Bird):

    def feed(self, food: "Vegetable" or "Fruit" or "Meat" or "Seed") -> None or str:
        if self.check_proper_food_type(food):
            self.food_consumption(food)
            self.increase_food_eaten(food)
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
