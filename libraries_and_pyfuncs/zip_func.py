def zip_test():
    lst = [i for i in range(1, 6)]
    lst2 = [i for i in range(6, 11)]
    lst3 = [i for i in range(6, 11)]

    d = {key: val + val2 for key, val, val2 in zip(lst, lst2, lst3)}

    print(d)
