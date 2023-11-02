def cache(func):
    def wrapper(num):
        if num not in wrapper.log:
            wrapper.log[num] = func(num)

        return wrapper.log[num]

    wrapper.log = {}
    return wrapper


if __name__ == '__main__':
    @cache
    def fibonacci(n):
        if n < 2:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)


    fibonacci(150)
    print(fibonacci.log)
