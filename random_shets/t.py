def t():
    lst  = [1, 2, 3, 4, 5]
    lst2 = [6, 7, 8, 9, 10]
    lst3 = [11, 12, 13, 14, 15]

    for i, j, k in zip(lst, lst2, lst3):
        print(i, j, k)

    dictionary = {
        "lst": [1, 2, 3, 4, 5],
        "lst2": [6, 7, 8, 9, 10],
        "lst3": [11, 12, 13, 14, 15]
    }

    keys = list(dictionary.keys())

    for i, j, k in zip(keys, keys[1:], keys[2:]):
        print(dictionary[i], dictionary[j], dictionary[k])
