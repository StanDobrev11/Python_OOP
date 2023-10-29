def solution():
    def integers():
        """ generates an infinite amount of integers (starting from 1) """
        num = 1
        while True:
            yield num
            num += 1

    def halves():
        """ generates the halves of those integers (each integer / 2) """
        for i in integers():
            yield i / 2

    def take(n, seq):
        """ takes the first n halves of the integers """
        return [next(seq) for _ in range(n)]


    return (take, halves, integers)


if __name__ == '__main__':
    take = solution()[0]
    halves = solution()[1]
    print(take(5, halves()))
