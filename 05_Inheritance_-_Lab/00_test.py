class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_name(self):
        return f"Hello, my name is {self.name}"


class Employee(Person):
    def __init__(self, name, age, security_number):
        super().__init__(name, age)
        self.security_number = security_number


class Teacher(Employee):
    def __init__(self, name, age, security_number, children):
        super().__init__(name, security_number, age)
        self.children = children


t = Teacher('Ivan', 123, 15)
print(t.name)
print(t.security_number)
print(t.children)
print(t.say_name())
