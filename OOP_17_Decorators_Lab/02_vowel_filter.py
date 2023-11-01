def vowel_filter(function):
    vowels = ['a', 'e', 'o', 'u', 'y', 'i']

    def wrapper():
        return [x for x in function() if x in vowels]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


if __name__ == '__main__':
    print(get_letters())
