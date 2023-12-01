"""In this workshop, we are going to create a custom data structure, which has similar functionalities as the Python List,
and create unit tests for its functionalities. It will have the same functionalities as the original List:
• append(value) - Adds a value to the end of the list. Returns the list.
• remove(index) - Removes the value on the index. Returns the value removed.
• get(index) - Returns the value on the index.
• extend(iterable) - Appends the iterable to the list. Returns the new list.
• insert(index, value) - Adds the value on the specific index. Returns the list.
• pop() - Removes the last value and returns it.
• clear() - Removes all values, contained in the list.
• index(value) - Returns the index of the given value.
• count(value) - Returns the number of times the value is contained in the list.
• reverse() - Returns the values of the list in reverse order.
• copy() - Returns a copy of the list.
We will also add our own custom functionalities:
• size() - Returns the length of the list.
• add_first(value) - Adds the value at the beginning of the list
• dictionize() - Returns the list as a dictionary: The keys will be each value on an even position and their
values will be each value on an odd position. If the last value on an even position, its value will be " " (space)
• move(amount) - Move the first "amount" of values to the end of the list. Returns the list.
• sum() - Returns the sum of the list. If the value is not a number, add the length of the value to the overall
number.
• overbound() - Returns the index of the biggest value. If the value is not a number, check its length.
• underbound() - Returns the index of the smallest value. If the value is not a number, check its length.
Do not inherit List. Feel free to implement your own functionality (and unit tests) or to
write the methods by yourself"""
from typing import Any


class CustomList:
    def __init__(self, *args) -> None:
        self.__capacity = 4
        self.__list = [None] * self.__capacity
        self.__length = 0
        if args:
            self.extend(args)

    @property
    def size(self):
        return self.__length

    def sum(self):
        """ Returns the sum of the list. If the value is not a number,
        add the length of the value to the overall number. """

        ttl_sum = 0

        for i in range(self.size):
            item = self.__list[i]

            try:
                item = float(item)
            except ValueError:
                item = len(item)
            ttl_sum += item

        return ttl_sum

    def append(self, value: Any):
        """ Appends any type of value to the list and returns the list. """

        next_idx = self.size
        if next_idx >= self.__capacity:
            self.__resize_list()

        self.__list[next_idx] = value
        self.__length += 1

        return self

    def remove(self, index: int) -> Any:
        """ Removes the value on the index. Returns the value removed. """

        index = self.__validate_idx(index)
        value = self.__list[index]
        self.__list[index] = None

        self.__shift_left(index)

        self.__length -= 1

        return value

    def get(self, index: int):
        """ Returns the value on the index. """

        return self.__list[index]

    def extend(self, iterable):
        """ Appends the iterable to the list. Returns the new list. """

        for item in iterable:
            self.append(item)

        return self.__list

    def pop(self):
        """ Removes the last value and returns it. """

        return self.remove(-1)

    def clear(self):
        """ Removes all values, contained in the list. """

        self.__list = [None] * self.__capacity

    def insert(self, index, value):
        """ Adds the value on the specific index. Returns the list. """

        index = self.__validate_idx(index)  # validate the index

        if len(self) >= self.__capacity:  # resize the array if so required
            self.__resize_list()

        # recursively shift elements to accommodate the new value on the given index
        self.__shift_right(index)

        self.__list[index] = value  # place the value on the index
        self.__length += 1  # adjust the new array length

        return self

    def index(self, value):
        """ Returns the index of the given value. (First encounter) """

        for i in range(self.__length):
            if self.__list[i] == value:
                return i

    def count(self, value):
        """ Returns the number of times the value is contained in the list. """

        count = 0

        for i in range(self.__length):
            if self.__list[i] == value:
                count += 1

        return count

    def reverse(self):
        """ Returns the values of the list in reverse order. """

        reversed_list = []
        for i in range(self.__length - 1, -1, -1):
            reversed_list.append(self.__list[i])

        return "[" + ', '.join(str(item) for item in reversed_list if item) + "]"

    def copy(self):
        """ Returns a copy of the list. """

        copied_list = []
        for i in range(self.__length):
            copied_list.append(self.__list[i])

        return copied_list

    def add_first(self, value):
        """ Adds the value at the beginning of the list """

        self.insert(0, value)

    def dictionize(self):
        """ Returns the list as a dictionary: The keys will be each value on an even position and their
values will be each value on an odd position. If the last value on an even position, its value will be " " (space) """

        even_list = [self.__list[i] for i in range(len(self)) if i % 2 == 0]
        odd_list = [self.__list[i] for i in range(len(self)) if i % 2 == 1]

        if len(even_list) > len(odd_list):
            odd_list.append(' ')

        return {x: y for x, y in zip(even_list, odd_list)}

    def move(self, amount):
        """ Move the first "amount" of values to the end of the list. Returns the list. """

        for i in range(amount):
            el = self.remove(0)
            self.append(el)

        return self

    def overbound(self):
        """ Returns the index of the biggest value. If the value is not a number, check its length. """

        biggest_num = -float('inf')

        for i in range(self.size):
            item = self.__list[i]

            try:
                item = float(item)

            except ValueError:
                item = len(item)

            if item > biggest_num:
                biggest_num = item

        return biggest_num

    def underbound(self):
        """ Returns the index of the smallest value. If the value is not a number, check its length. """

        smallest_num = float('inf')

        for i in range(self.size):
            item = self.__list[i]

            try:
                item = float(item)

            except ValueError:
                item = len(item)

            if item < smallest_num:
                smallest_num = item

        return smallest_num

    def __shift_left(self, index):
        """ shift elements left to occupy the vacant space """

        for i in range(index, self.__length):
            if i == self.__length - 1:
                break
            self.__list[i], self.__list[i + 1] = self.__list[i + 1], self.__list[i]

    def __shift_right(self, i):
        """ Recursive shift of elements """
        if self.__list[i] is None:
            return

        if i == len(self):
            return

        self.__shift_right(i + 1)

        self.__list[i + 1], self.__list[i] = self.__list[i], None

    def __validate_idx(self, index: int):
        """ checks and validates index """

        # type validation
        if not isinstance(index, int):
            raise TypeError("Index must be of type int")

        # convert index to positive number
        if index < 0:
            index += len(self)

        # check for proper range of the index
        if index not in range(len(self)):
            raise IndexError("Not a valid index")

        return index

    def __resize_list(self):
        """ extends the list by doubling the capacity """

        self.__list.extend([None] * self.__capacity)
        self.__capacity *= 2

    def __len__(self) -> int:
        return self.__length

    def __repr__(self):
        return "[" + ', '.join(str(item) for item in self.__list if item) + "]"


if __name__ == '__main__':
    ll = CustomList('a', 'b', 'c', 'e', 'f', 'g')
    print(ll.insert(3, 'd'))
    print(ll.remove(3))
    print(ll)
    print(len(ll))
    print(ll.reverse())
    print(ll.dictionize())
    print(len(ll))
    ll.move(3)
    print(ll)
    print(len(ll))
    print(ll.insert(0, 'ace'))
    print(len(ll))
    print(ll.insert(6, 'of bace'))
    print(len(ll))
    print(ll.remove(4))
    print(ll.remove(-1))
    print(ll.get(1))
    print(ll.pop())
    ll.append(5)
    ll.extend([5, 6, 7])
    print(ll)
    print(ll.sum())
    print(ll.overbound())
    ll.insert(0, -2)
    print(ll.underbound())
