"""
Create a decorator called type_check. It should receive a type (int/float/str/…), and it should check if the
parameter passed to the decorated function is of the type given to the decorator. If it is, execute the function and
return the result, otherwise return "Bad Type".
"""


def type_check(exp_type):
    def decorator(func):
        def wrapper(*args):
            if isinstance(*args, exp_type):
                return func(*args)

            return "Bad Type"

        return wrapper

    return decorator


if __name__ == '__main__':
    @type_check(int)
    def times2(num):
        return num * 2


    print(times2(2))
    print(times2('Not A Number'))
