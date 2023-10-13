class Worker:
    ttl_salaries = 0
    ttl_workers = 0
    def __init__(self, name: str, age: int, salary: int) -> None:
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        Worker.ttl_salaries += value
        self.__salary = value
