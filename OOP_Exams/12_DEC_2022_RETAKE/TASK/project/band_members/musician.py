from abc import ABC, abstractmethod


class Musician(ABC):

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.skills = []

    @property
    @abstractmethod
    def skills_required(self):
        """ list of available to learn skills individual for each type of musician """
        ...

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if value.strip() == '':
            raise ValueError("Musician name cannot be empty!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value: int):
        if value < 16:
            raise ValueError("Musicians should be at least 16 years old!")
        self.__age = value

    def learn_new_skill(self, new_skill: str):

        if new_skill not in self.skills_required:
            raise ValueError(f"{new_skill} is not a needed skill!")

        if new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")

        self.skills.append(new_skill)
        return f"{self.name} learned to {new_skill}."

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.name}"