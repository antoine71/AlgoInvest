from utils.utils import product_lists

from itertools import product


def brute_force(values, profits, names, wallet_capacity):

    max_number_of_shares = [wallet_capacity // share_value for share_value in values]

    shares_combinations_product = product(*[list(range(i + 1)) for i in max_number_of_shares])
    shares_combinations = [combinations for combinations in shares_combinations_product]

    possible_shares_combinations = [combinations for combinations in shares_combinations
                                    if sum(product_lists(values, combinations)) == wallet_capacity]

    possible_combinations_profits = [sum(product_lists(profits, combinations))
                                     for combinations in possible_shares_combinations]

    best_profit = max(possible_combinations_profits)
    best_shares_index = possible_combinations_profits.index(best_profit)
    best_shares_list = possible_shares_combinations[best_shares_index]
    best_shares = {names[i]: q for i, q in enumerate(best_shares_list) if q > 0}

    return best_profit, best_shares
