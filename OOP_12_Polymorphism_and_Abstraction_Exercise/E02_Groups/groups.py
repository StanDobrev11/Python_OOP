from typing import List


class Person:
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname

    def __repr__(self) -> str:
        """Each person could be represented by their names, separated by a single space."""
        return f"{self.name} {self.surname}"

    def __add__(self, other: "Person") -> "Person":
        """
        When you concatenate two people, you should return a new instance of a person who will take the first
        name from the first person and the surname from the second person.
        """
        return Person(self.name, other.surname)


class Group:
    def __init__(self, name: str, people: List[Person]) -> None:
        self.name = name
        self.people = people

    def __len__(self) -> int:
        """
        When you access the length of a group instance, you should receive the total number of
        people in the group
        """
        return len(self.people)

    def __add__(self, other: "Group") -> "Group":
        """
        When you concatenate two groups, you should return a new instance of a group which will have a name -
        string in the format "{first_name} {second_name}" and all the people in the two groups will
        participate in the new one too.
        """
        return Group(f"{self.name} {other.name}", self.people + other.people)

    def __repr__(self) -> str:
        """
        Each group should be represented in the format "Group {name} with members {members' names
        separated by comma and space}
        """
        members = ', '.join(f"{member}" for member in self.people)
        return f"Group {self.name} with members {members}"

    def __getitem__(self, item) -> str:
        """
        You could iterate over a group, and each person (element of the group) should be represented in the
        format "Person {index}: {person's name}"
        """
        return f"Person {item}: {self.people[item]}"


p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3
first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group
print(len(first_group))
print(second_group)
print(third_group[0])
for person in third_group:
    print(person)
