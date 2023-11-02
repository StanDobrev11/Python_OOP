"""
Create a class called store_results. It should be used as a decorator and store information about the executed
functions in a file called results.txt in the format: "Function {func_name} was called. Result:
{func_result}"

"""


class store_results:
    """class that does not accept arguments"""
    _file_name = "result.txt"

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        with open(self._file_name, 'a') as file:
            file.write(f"Function {self.func.__name__} was called. Result: {self.func(*args, **kwargs)}")
            file.write("\n")


class store_result_2:
    """accepts arguments"""

    _file_name = 'res_2.txt'

    def __init__(self, param):
        self.param = param

    def __call__(self, func):
        """ call method becomes decorator """

        def wrapper(*args):
            with open(self._file_name, 'a') as file:
                file.write(f"Function {func.__name__} was called. Result: {func(*args)}")
                file.write("\n")

        return wrapper


if __name__ == '__main__':
    @store_results
    def add(a, b):
        return a + b


    @store_result_2(2)
    def mult(a, b):
        return a * b


    add(2, 2)
    mult(6, 4)
