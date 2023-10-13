from project.animal import Animal
from project.worker import Worker
from typing import List


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int) -> None:
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        is_capacity_left = self.__animal_capacity > len(self.animals)
        is_budget_enough = self.__budget >= price
        if is_capacity_left and is_budget_enough:
            self.animals.append(animal)
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif is_capacity_left and not is_budget_enough:
            return "Not enough budget"

        else:
            return "Not enough space for animal"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name: str) -> str:
        try:
            worker = [worker for worker in self.workers if worker_name == worker.name][0]
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"

        except IndexError:
            return f"There is no {worker_name} in the zoo"

    