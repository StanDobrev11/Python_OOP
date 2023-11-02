def multiply(times):
    def decorator(function):

        def wrapper(*args, **kwargs):
            return function(*args, **kwargs) * times

        return wrapper

    # TODO: Implement
    return decorator


@multiply(3)
def add_ten(number):
    return number + 10


if __name__ == '__main__':
    print(add_ten(3))
