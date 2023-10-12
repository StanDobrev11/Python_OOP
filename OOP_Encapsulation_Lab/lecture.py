class Person:
    def __init__(self, name):
        self.name = name
        self.faculty_id = '22322'
        self.__security_number = '123456'
        self.test_var = 'A'

    def get_security_number(self):
        return self.__security_number[-4:]

    def set_security_number(self, new_value):
        today = '2024-01-01'
        if today > '2024-03-01':
            self.__security_number = new_value

    def test_get(self):
        return self.test_var


p = Person('Ivan')
print(p.test_get())