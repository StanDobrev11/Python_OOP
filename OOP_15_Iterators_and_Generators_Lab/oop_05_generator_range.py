def genrange(start, end):
    num = start
    while num <= end:
        yield num
        num += 1


if __name__ == '__main__':
    print(list(genrange(1, 10)))
