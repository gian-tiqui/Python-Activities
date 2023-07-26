def original_spot(moves: str):
    u, d = 0, 0
    l, r = 0, 0

    for c in moves.lower():
        if c == "u":
            u += 1
        elif c == "d":
            d += 1
        elif c == "l":
            l += 1
        elif c == "r":
            r += 1

    return u == d and l == r


if __name__ == '__main__':
    print(original_spot("UUDD"))
