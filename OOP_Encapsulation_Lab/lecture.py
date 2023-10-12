class Person:
    def __init__(self, name: str, faculty_id: int, security_number: int, test_var: str):
        self.name = name
        self.faculty_id = faculty_id
        self.security_number = security_number
        self.test_var = test_var

    @property
    def security_number(self):
        return self.__security_number

    @security_number.setter
    def security_number(self, value):
        if isinstance(value, int):
            self.__security_number = value

    @property
    def test_var(self):
        return self.__test_var

    @test_var.setter
    def test_var(self, value):
        self.__test_var = value.upper()

    def test_get(self):
        return self.test_var

    def set_security_num(self, value):
        pass


p = Person('Ivan', 123, 3343343, 'asas')
print(p.test_get())
print(p.security_number)
print(p.__dict__)
