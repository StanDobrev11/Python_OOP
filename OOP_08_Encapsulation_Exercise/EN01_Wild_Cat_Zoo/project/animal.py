class Animal:
    ttl_amount_for_care = 0

    def __init__(self, name: str, gender: str, age: int, money_for_care: int) -> None:
        self.name = name
        self.gender = gender
        self.age = age
        self.money_for_care = money_for_care

    def __repr__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

    @property
    def money_for_care(self):
        return self.__money_for_care

    @money_for_care.setter
    def money_for_care(self, value):
        Animal.ttl_amount_for_care += value
        self.__money_for_care = value
