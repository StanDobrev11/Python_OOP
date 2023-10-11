from employee import Employee
from person import Person


class Teacher(Employee, Person):
    @staticmethod
    def teach():
        return "teaching..."


p = Teacher()
print(p.teach())
print(p.get_fired())
print(p.sleep())
