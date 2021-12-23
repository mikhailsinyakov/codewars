from itertools import product


def rolldice_sum_prob(sum_, dice_amount):
    all_combs = list(product(range(1, 7), repeat=dice_amount))
    return sum([True for comb in all_combs if sum(comb) == sum_]) / len(all_combs)
