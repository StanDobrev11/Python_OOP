from abc import ABC, abstractmethod

from project.food import Vegetable, Meat, Fruit, Seed, Food


class Animal(ABC):
    SOUND = {
        'Hen': "Cluck",
        'Owl': "Hoot Hoot",
        'Cat': "Meow",
        'Dog': "Woof!",
        'Mouse': "Squeak",
        'Tiger': "ROAR!!!",
    }
    WEIGHT_INCREASE = {
        'Hen': 0.35,
        'Owl': 0.25,
        'Mouse': 0.10,
        'Cat': 0.30,
        'Dog': 0.40,
        'Tiger': 1.00,
    }

    @abstractmethod
    def __init__(self, name: str, weight: float, food_eaten: int = 0) -> None:
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten

    def make_sound(self) -> str:
        return f"{Animal.SOUND[self.__class__.__name__]}"

    @abstractmethod
    def feed(self, food: "Food"):
        pass

    def check_proper_food_type(self, food: "Food") -> bool:
        animal_food_mapper = {
            'Hen': [Meat, Vegetable, Fruit, Seed],
            'Owl': [Meat],
            'Cat': [Meat, Vegetable],
            'Dog': [Meat],
            'Mouse': [Vegetable, Fruit],
            'Tiger': [Meat],
        }
        if food.__class__ in animal_food_mapper[self.__class__.__name__]:
            return True
        return False

    def food_consumption(self, food: "Food") -> None:
        self.weight += Animal.WEIGHT_INCREASE[self.__class__.__name__] * food.quantity

    def increase_food_eaten(self, food) -> None:
        self.food_eaten += food.quantity


class Bird(Animal, ABC):
    def __init__(self, name: str, weight: float, wing_size: float, food_eaten: int = 0, ):
        super().__init__(name, weight, food_eaten)
        self.wing_size = wing_size

    @abstractmethod
    def feed(self, food):
        pass

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):
    def __init__(self, name: str, weight: float, living_region: str, food_eaten: int = 0, ):
        super().__init__(name, weight, food_eaten)
        self.living_region = living_region

    @abstractmethod
    def feed(self, food):
        pass

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
