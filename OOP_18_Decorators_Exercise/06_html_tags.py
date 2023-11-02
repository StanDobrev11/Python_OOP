"""
Create a decorator called tags. It should receive an HTML tag as a parameter, wrap the result of a function with
the given tag and return the new result. For more clarification, see the examples below
"""


def tags(tag):
    def decorator(func):
        def wrapper(*args):
            return f"<{tag}>{func(*args)}</{tag}>"

        return wrapper

    return decorator


if __name__ == '__main__':
    @tags('p')
    def join_strings(*args):
        return "".join(args)


    print(join_strings("Hello", " you!"))
