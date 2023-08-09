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

    for i in range(len(lst) - n + 1):
        max_num = lst[i]
        for j in range(i, i + n):
            max_num = max(max_num, lst[j])
        max_nums.append(max_num)

    return max_nums
