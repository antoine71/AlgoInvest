def knapsack(values, profits, names, wallet_capacity):
    """This function implements the knapsack solution algorithm using dynamic programming."""
    number_of_shares = len(values)

    # This array store the profits for knapsacks of sizes from 0 to wallet capacity.
    # It contains only 2 rows to save memory.
    profits_array = [
            [
                0 for col in range(wallet_capacity + 1)
            ]
            for row in range(2)
        ]

    # This array store the shares used to achieve the maximum profit.
    # It contains only 2 rows to save memory.
    combinations = [
            [
                {} for col in range(wallet_capacity + 1)
            ]
            for i in range(2)
        ]

    for i in range(number_of_shares):
        for j in range(1, wallet_capacity + 1):

            including_current_share_profit = 0
            excluding_current_share_profit = 0

            if values[i] <= j:
                including_current_share_profit = profits[i] + profits_array[1][j - values[i]]

            if i > 0:
                excluding_current_share_profit = profits_array[0][j]

            profits_array[1][j] = max(including_current_share_profit, excluding_current_share_profit)

            if including_current_share_profit > excluding_current_share_profit:
                combinations[1][j] = dict(combinations[1][j - values[i]])
                try:
                    combinations[1][j][names[i]] += 1
                except KeyError:
                    combinations[1][j][names[i]] = 1
            else:
                combinations[1][j] = dict(combinations[0][j])

        profits_array[0] = list(profits_array[1])
        combinations[0] = list(combinations[1])

    max_profit = profits_array[1][wallet_capacity]
    max_combination = combinations[1][wallet_capacity]

    return max_profit, max_combination
