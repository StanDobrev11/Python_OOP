from project.animal import Animal
from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.worker import Worker
from typing import ClassVar


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int) -> None:
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: list[ClassVar] = []
        self.workers: list[ClassVar] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        """Adds animal to the zoo list if certain conditions are met"""
        if self.__budget < price:
            return "Not enough budget"

        if self.__animal_capacity <= 0:
            return "Not enough space for animal"

        self.__animal_capacity -= 1
        self.__budget -= price
        self.animals.append(animal)
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker) -> str:
        """Add help to the zoo - hire workers"""
        if self.__workers_capacity <= 0:
            return "Not enough space for worker"

        self.__workers_capacity -= 1
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str) -> str:
        """Fire workers from the zoo"""
        try:
            worker = [worker for worker in self.workers if worker_name == worker.name][0]
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"

        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        """If budget is enough to pay all salaries, then pay"""
        if self.__budget >= Worker.ttl_salaries:
            self.__budget -= Worker.ttl_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    # def tend_animals(self):
    #     """Tending the animals by reducing budget"""
    #     if self.__budget >