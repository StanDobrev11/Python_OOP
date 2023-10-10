from animal import Animal


class Dog(Animal):

    @staticmethod
    def bark():
        return 'barking...'


d = Dog()
print(d.eat())
print(d.bark())