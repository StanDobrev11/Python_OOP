class reverse_iter:
    def __init__(self, iter_obj):
        self.iter_obj = iter_obj
        self.start_idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.start_idx -= 1
            return self.iter_obj[self.start_idx]
        except IndexError:
            raise StopIteration


if __name__ == "__main__":
    reversed_list = reverse_iter([1, 2, 3, 4])
    for item in reversed_list:
        print(item)
