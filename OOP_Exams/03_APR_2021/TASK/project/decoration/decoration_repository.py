from typing import List

from project.decoration.base_decoration import BaseDecoration


class DecorationRepository:
    def __init__(self):
        self.decorations: List[BaseDecoration] = []

    def add(self, decoration: BaseDecoration) -> None:
        """ adds decoration to the list """
        self.decorations.append(decoration)

    def remove(self, decoration: BaseDecoration) -> bool:
        """ removes decoration """
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True
        return False

    def find_by_type(self, decoration_type: str):
        try:
            return [decor for decor in self.decorations if decor.type == decoration_type][0]
        except IndexError:
            return None

