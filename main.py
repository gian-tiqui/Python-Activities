def original_spot(moves: str):
    moves_dict = {
        "u": 0,
        "d": 0,
        "l": 0,
        "r": 0
    }

    for c in moves.lower():
        moves_dict[c] = moves_dict[c] + 1

    return moves_dict["u"] == moves_dict["d"] and moves_dict["l"] == moves_dict["r"]


def find_k_max(lst, n):
    max_nums = []

    return max_nums


if __name__ == '__main__':
    print(original_spot("UUD"))
    print(find_k_max([1, 2, 3, 4, 5, 6], 2))
