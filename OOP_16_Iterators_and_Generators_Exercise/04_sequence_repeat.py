"""
Create a class called sequence_repeat which should receive a sequence and a number upon initialization.
Implement an iterator to return the given elements, so they form a string with a length - the given number. If the
number is greater than the number of elements, then the sequence repeats as necessary.
"""


class sequence_repeat:
    def __init__(self, seq: str, count: int):
        self.seq = seq
        self.count = count
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx == self.count - 1:
            raise StopIteration

        self.idx += 1

        return self.seq[self.idx % len(self.seq)]


if __name__ == '__main__':
    result = sequence_repeat('abc', 5)
    for item in result:
        print(item, end='')

    print()

    result_1 = sequence_repeat('I Love Python', 3)
    for item in result_1:
        print(item, end='')
