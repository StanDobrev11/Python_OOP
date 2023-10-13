from project.animal import Animal
from project.worker import Worker
from typing import ClassVar


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int) -> None:
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals_by_class = {}
        self.animals: list[Animal] = []
        self.workers_by_class = {}
        self.workers: list[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        """Adds animal to the zoo list if certain conditions are met"""
        if self.__budget < price:
            Animal.ttl_amount_for_care -= animal.money_for_care
            return "Not enough budget"

        if self.__animal_capacity <= 0:
            Animal.ttl_amount_for_care -= animal.money_for_care
            return "Not enough space for animal"

        if animal.__class__.__name__ not in self.animals_by_class:
            self.animals_by_class[animal.__class__.__name__] = []

        self.animals_by_class[animal.__class__.__name__].append(animal)
        self.__animal_capacity -= 1
        self.__budget -= price
        self.animals.append(animal)
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker) -> str:
        """Add help to the zoo - hire workers"""
        if self.__workers_capacity == Worker.ttl_workers:
            Worker.ttl_salaries -= worker.salary
            return "Not enough space for worker"

        if worker.__class__.__name__ not in self.workers_by_class:
            self.workers_by_class[worker.__class__.__name__] = []

        Worker.ttl_workers += 1
        self.workers_by_class[worker.__class__.__name__].append(worker)
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str) -> str:
        """Fire workers from the zoo"""
        try:
            worker = [worker for worker in self.workers if worker_name == worker.name][0]
            self.workers_by_class[worker.__class__.__name__].remove(worker)
            self.workers.remove(worker)
            Worker.ttl_salaries -= worker.salary
            Worker.ttl_workers -= 1
            return f"{worker_name} fired successfully"

        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        """If budget is enough to pay all salaries, then pay"""
        if self.__budget >= Worker.ttl_salaries:
            self.__budget -= Worker.ttl_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        """Tending the animals by reducing budget"""
        if self.__budget >= Animal.ttl_amount_for_care:
            self.__budget -= Animal.ttl_amount_for_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        """Increase the budget with the given amount of profit"""
        self.__budget += amount

    def animals_status(self) -> str:
        output_data = f"You have {len(self.animals)} animals\n"
        output_data += f"----- {len(self.animals_by_class['Lion'])} Lions:\n"
        output_data += "\n".join(animal.__repr__() for animal in self.animals_by_class['Lion'])
        output_data += '\n' + f"----- {len(self.animals_by_class['Tiger'])} Tigers:\n"
        output_data += "\n".join(animal.__repr__() for animal in self.animals_by_class['Tiger'])
        output_data += '\n' + f"----- {len(self.animals_by_class['Cheetah'])} Cheetahs:\n"
        output_data += "\n".join(animal.__repr__() for animal in self.animals_by_class['Cheetah'])

        return output_data

    def workers_status(self) -> str:
        output_data = f"You have {len(self.workers)} workers\n"
        output_data += f"----- {len(self.workers_by_class['Keeper'])} Keepers:\n"
        output_data += "\n".join(worker.__repr__() for worker in self.workers_by_class['Keeper'])
        output_data += '\n' + f"----- {len(self.workers_by_class['Caretaker'])} Caretakers:\n"
        output_data += "\n".join(worker.__repr__() for worker in self.workers_by_class['Caretaker'])
        output_data += '\n' + f"----- {len(self.workers_by_class['Vet'])} Vets:\n"
        output_data += "\n".join(worker.__repr__() for worker in self.workers_by_class['Vet'])

        return output_data
