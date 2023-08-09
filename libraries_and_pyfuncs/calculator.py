import operator as op


def calculate(x, y, operator):
    d = {
        "+": op.add,
        "-": op.sub,
        "*": op.mul,
        "/": op.truediv,
        "//": op.floordiv,
        "**": op.pow
    }

    return d[operator](x, y)
