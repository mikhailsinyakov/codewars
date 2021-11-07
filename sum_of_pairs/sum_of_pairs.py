def sum_pairs(ints, _sum):
    d = {}

    for num2 in ints:
        num1 = _sum - num2
        if num1 in d:
            return [num1, num2]
        else:
            d[num2] = True

    return None
