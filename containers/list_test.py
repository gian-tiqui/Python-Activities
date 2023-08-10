def increment(n: int):
    if n < 0:
        return n - 1

    return n + 1


def list_test():
    list_ = [i for i in range(1, increment(10))]
    print(list_)

    list_copy = list_.copy()
    print(list_copy)

    list_.append([1, 2, 3])
    print(list_)

    list_[10].append(1)
    print(list_)

    list_mul = [[]] * 3
    list_mul[0].append(1)
    print(list_mul)
    