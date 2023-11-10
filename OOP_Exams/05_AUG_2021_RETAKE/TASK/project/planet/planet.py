from typing import List


class Planet:
    def __init__(self, name: str):
        self.name = name
        self.items: List = []
        self.is_explored = False

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        if value.strip() == '':
            raise ValueError("Planet name cannot be empty string or whitespace!")
        self.__name = value

    def add_items(self, items: str):
        items = items.split(', ')
        for item in items:
            self.items.append(item)
