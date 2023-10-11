"""
Create a program that reads a positive integer N as input and prints on the console a rhombus with size n:
Input Output
3
  *
 * *
* * *
 * *
  *
4
   *
  * *
 * * *
* * * *
 * * *
  * *
   *
"""


def print_row(n, count):
    print(' ' * (n - count) + ' *' * count)


def print_upper_triangle(n):
    for star in range(1, n + 1):
        print_row(n, star)


def print_reversed_triangle(n):
    for star in range(n - 1, 0, -1):
        print_row(n, star)


def print_rombus(n):
    print_upper_triangle(n)
    print_reversed_triangle(n)


n = int(input())
print_rombus(n)
