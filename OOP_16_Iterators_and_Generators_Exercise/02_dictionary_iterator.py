"""
Create a class called dictionary_iter. Upon initialization, it should receive a dictionary object. Implement the
iterator to return each key-value pair of the dictionary as a tuple of two elements (the key and the value).
"""


class dictionary_iter:
    def __init__(self, some_dict: dict) -> None:
        self.res_list = list(some_dict.items())
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx == len(self.res_list) - 1:
            raise StopIteration

        self.idx += 1

        return self.res_list[self.idx]


if __name__ == '__main__':
    result = dictionary_iter({1: "1", 2: "2"})
    for x in result:
        print(x)

    result_1 = dictionary_iter({"name": "Peter", "age": 24})
    for x in result_1:
        print(x)
