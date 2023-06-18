def fib(lim: int):
    n, n1, t = 1, 1, 0

    while n < lim:
        t = n
        print(t, end=" ")
        n = n1
        n1 = n + t


def nth_fib_num(lim: int):

    n, n1, t = 1, 1, 0

    counter = 0

    while counter < lim:
        t = n
        n = n1
        n1 = n + t
        counter += 1

    return t
