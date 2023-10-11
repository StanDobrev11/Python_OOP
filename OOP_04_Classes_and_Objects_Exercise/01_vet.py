"""
Create a class called Vet. The Vet class represents a veterinary doctor in an animal clinic. Upon initialization, it
should receive a name (string - the name of the vet doctor). It should also have an instance attribute called
animals (empty list by default). There should also be 2 class attributes: animals (empty list) which will store the
total amount of animals for all vet doctors; and space (5 by default, representing the total capacity of the clinic).
You should create 3 additional instance methods:
- register_animal(animal_name)
o If there is available space in the vet clinic, add the animal to both animals' lists and return a
message: "{name} registered in the clinic"
o Otherwise, return "Not enough space"
- unregister_animal(animal_name)
o If the animal is in the clinic, remove it from both animals' lists and return "{animal}
unregistered successfully"
o Otherwise, return "{animal} not in the clinic"
- info()
o Return info about the vet doctor, the number of animals in his/her list, and the available space left
in the clinic:
"{vet_name} has {number_animals} animals. {space_left_in_clinic} space
left in clinic"

"""
from typing import List


class Vet:
    animals: List[str] = []
    space: int = 5

    def __init__(self, name: str):
        self.name = name
        self.animals: List[str] = []

    def register_animal(self, animal_name: str) -> str:
        if Vet.space > 0 and animal_name not in self.animals:
            Vet.space -= 1
            self.animals.append(animal_name)
            Vet.animals.append(animal_name)
            return f"{animal_name} registered in the clinic"
        return f"Not enough space"

    def unregister_animal(self, animal_name: str) -> str:
        if animal_name in self.animals:
            Vet.animals.remove(animal_name)
            self.animals.remove(animal_name)
            Vet.space += 1
            return f"{animal_name} unregistered successfully"
        return f"{animal_name} not in the clinic"

    def info(self) -> str:
        return f"{self.name} has {len(self.animals)} animals. {Vet.space} space left in clinic"

    def __repr__(self):
        return f"Vet doctor is {self.name}"


peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())
