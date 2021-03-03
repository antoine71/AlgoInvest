"""
This modules defines the brute force algorithm.
"""

from utils.lists_operations import product_lists

from itertools import product


def brute_force(values, profits, names, wallet_capacity):
    """
    This function implements a brute force algorithm. This algorithm
    evaluates all possible combination of shares for a given wallet. It then
    calculates the profit for each combination and selects the combination
    with the highest profit. The time complexity of this algorithm is O(2^n).
    It returns the result as a tuple:
    * best_profit is the profit made in the shares currency
    * best_shares is a dictionnary that contains as key the name of the shares
    to be selected to achieve the best profit, and as values the quantity of
    shares to pick.
    """

    max_number_of_shares = [
        int(wallet_capacity // share_value) for share_value in values]

    yields = [profits[i] / values[i] for i in range(len(values))]
    values_shares = [
        [values[i] * j for j in range(n + 1)]
        for i, n in enumerate(max_number_of_shares)]

    possible_shares_combinations = [
        combination for combination in product(*values_shares)
        if sum(combination) <= wallet_capacity]

    possible_combinations_profits = [
        sum(product_lists(combinations, yields))
        for combinations in possible_shares_combinations]

    best_profit = max(possible_combinations_profits)
    best_shares_index = possible_combinations_profits.index(best_profit)
    best_shares_list = possible_shares_combinations[best_shares_index]
    best_shares = {
        names[i]: (q / values[i])
        for i, q in enumerate(best_shares_list) if q > 0}

    return best_profit, best_shares
