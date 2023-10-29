"""
Create a generator function called read_next() which should receive a different number of arguments (all
iterable). On each iteration, the function should return each element from each sequence
"""


# def read_next(*args):
#     for el in args:
#         for ch in el:
#             yield ch


def read_next(*args):
    for seq in args:
        yield from seq


if __name__ == '__main__':
    for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
        print(item, end='')
