"""
Create a generator function called get_primes() which should receive a list of integer numbers and return a list
containing only the prime numbers from the initial list.
"""
from math import sqrt, ceil


def get_primes(param):
    for num in param:

        if num <= 1:
            continue

        for div in range(2, int(sqrt(num)) + 1):
            if num % div == 0:
                break

        else:
            yield num


if __name__ == '__main__':
    print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
    print(list(get_primes([-2, 0, 0, 1, 1, 0])))
#
# print(9 / 3)
# print(9 // 3)
# print(11 % 1)
# print(11 % 2)
# print(11 % 3)
# print(11 % 4)
# print(11 % 5)
# print(11 % 6)
# print(11 % 7)
# print(11 % 8)
# print(11 % 9)
# print(11 % 10)
