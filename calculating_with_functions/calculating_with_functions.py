import operator


def zero(t=None): return 0 if t is None else t[0](0, t[1])


def one(t=None): return 1 if t is None else t[0](1, t[1])


def two(t=None): return 2 if t is None else t[0](2, t[1])


def three(t=None): return 3 if t is None else t[0](3, t[1])


def four(t=None): return 4 if t is None else t[0](4, t[1])


def five(t=None): return 5 if t is None else t[0](5, t[1])


def six(t=None): return 6 if t is None else t[0](6, t[1])


def seven(t=None): return 7 if t is None else t[0](7, t[1])


def eight(t=None): return 8 if t is None else t[0](8, t[1])


def nine(t=None): return 9 if t is None else t[0](9, t[1])


def plus(n):
    return operator.add, n


def minus(n):
    return operator.sub, n


def times(n):
    return operator.mul, n


def divided_by(n):
    return operator.floordiv, n
