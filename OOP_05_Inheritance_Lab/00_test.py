class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_name(self):
        return f"Hello, my name is {self.name}"

    def __str__(self):
        return f"{self.name} - {self.age}"


class Employee(Person):
    def __init__(self, name, age, security_number, school):
        super().__init__(name, age)
        self.security_number = security_number
        self.school = school

    def __str__(self):
        return f"{self.name} - {self.age} - {self.security_number} - {self.school}"


class Teacher(Employee):
    def __init__(self, name, age, security_number, children):
        super().__init__(name, age, security_number, 'Vasil Levski')
        self.children = children

    def __str__(self):
        return f"{self.name} - {self.age} - {self.security_number} - {self.school}"


t = Teacher('Ivan', 123, 15, 15)
# print(t.name)
# print(t.security_number)
# print(t.children)
# print(t.say_name())
print(t.school)

e = Employee('Ivan', 123, 15, 'Ivan Vazov')

print(t)
print(e)
