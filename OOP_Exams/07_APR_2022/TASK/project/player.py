from project.supply.supply import Supply


class Player:
    _used_names = set()

    def __init__(self, name: str, age: int, stamina: int = 100):
        self.name = name
        self.age = age
        self.stamina = stamina

    @classmethod
    def clear_used_names(cls):
        cls._used_names = set()

    @property
    def need_sustenance(self):
        return True if self.stamina < 100 else False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if value.strip() == '':
            raise ValueError("Name not valid!")
        if value in Player._used_names:
            raise Exception(f"Name {value} is already used!")
        Player._used_names.add(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value: int):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value: int):
        if 0 <= value <= 100:
            self.__stamina = value
            return
        raise ValueError("Stamina not valid!")

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"

    def replenish_stamina(self, sustenance: Supply):
        if self.stamina + sustenance.energy > 100:
            self.stamina = 100

        self.stamina += sustenance.energy
        return f"{self.name} sustained successfully with {sustenance.name}."
