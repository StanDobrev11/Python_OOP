def repeater(n):
    """the decorator, accepting arguments"""

    def decorator(func):
        """ accepts the reference to the function"""

        def wrapper(*args, **kwargs):
            """ the function to be executed once the decorated functions is
            called. Accepts args and kwargs in order to be sure that nothing is left behind"""

            for _ in range(n):
                func(*args, **kwargs)  # calls the original function  and return NONE
                print(func(*args, **kwargs))

        return wrapper

    return decorator  # must be returned by repeater


if __name__ == '__main__':
    def hi(name):
        return f"Hi, my name is {name}"


    # print(hi('Slim Shady'))  # here the function is executed directly!! no decoration

    @repeater(2)
    def hi(name):
        return f"Hi, my name is {name}"


    # print(
    #     hi('Slim Shady'))  # this example the decorated funtion returns 'None' since int he func
    # body the wrapper returns nothing

    hi('Slim Shady')  # the base function body is overwritten by the wrapper function since it is decorated
