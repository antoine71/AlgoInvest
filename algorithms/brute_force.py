"""This modules defines the brute force algorithm."""

from utils.lists_operations import product_lists

from itertools import product


def brute_force(values, profits, names, wallet_capacity):
    """This function implements a brute force algorithm. This algorithm evaluates all possible combination
    of shares for a given wallet. It then calculates the profit for each combination and selects the combination
    with the highest profit. The time complexity of this algorithm is O(2^n).
    It returns the result as a tuple:
    * best_profit is the profit made in the shares currency
    * best_shares is a dictionnary that contains as key the name of the shares to be selected to
    achieve the best profit, and as values the quantity of shares to pick."""

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
