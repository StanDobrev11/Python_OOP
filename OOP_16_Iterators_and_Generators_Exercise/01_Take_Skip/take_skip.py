class take_skip:
    def __init__(self, step: int, count: int) -> None:
        self.step = step
        self.count = count
        self.current_count = -1
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.current_count += 1
        if self.count <= self.current_count:
            raise StopIteration

        self.num += self.step
        return self.num


if __name__ == '__main__':
    numbers = take_skip(2, 6)
    for number in numbers:
        print(number)
