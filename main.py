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


if __name__ == '__main__':
    print(original_spot("UUD"))
