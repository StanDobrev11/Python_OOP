def even_numbers(function):
    def wrapper(*args):
        return [num for num in function(*args) if num % 2 == 0]

    return wrapper


@even_numbers
def get_numbers(numbers: list):
    return numbers


if __name__ == '__main__':
    print(get_numbers([1, 2, 3, 4, 5]))
