from abc import ABC, abstractmethod


class BaseDecoration(ABC):
    base_types = {'Ornament', 'Plant'}

    def __init__(self, comfort: int, price: float):
        self.comfort = comfort
        self.price = price

    @property
    @abstractmethod
    def type(self):
        ...
