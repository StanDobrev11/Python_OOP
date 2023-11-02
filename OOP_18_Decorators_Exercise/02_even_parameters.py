"""
Create a decorator function called even_parameters. It should check if all parameters passed to a function are
even numbers and only then execute the function and return the result. Otherwise, don't execute the function and
return "Please use only even numbers!"
"""


def even_parameters(func):
    def wrapper(*args):
        if all(isinstance(x, int) and x % 2 == 0 for x in args):
            return func(*args)

        return "Please use only even numbers!"

    return wrapper


if __name__ == '__main__':
    @even_parameters
    def add(a, b):
        return a + b


    print(add(2, 4))
    print(add("Peter", 1))
