"""
This modules contians utilities to optimise shares samples.
"""


def clean_sample(values, profits, names, wallet_capacity):
    """
    This function scans the share sample and remove the shares that are not
    required to calculate the best profit:
        share value <= 0
        share profit <= 0
        share value > wallet capacity.
    """
    clean_values, clean_profits, clean_names = zip(*[
        (value, profit, name) for value, profit, name
        in zip(values, profits, names)
        if value > 0
        and profit > 0
        and value <= wallet_capacity
    ])
    return list(clean_values), list(clean_profits), list(clean_names)


def scale_sample(values, profits, wallet_capacity):
    """
    This function turn the shares values, profits and wallet capacity to
    integers by multiplying them by a scale factor multiple of 10.
    """
    scale_factor = 1
    while True:
        for value in values:
            if value % 1 >= 0.01 and 1 - value % 1 >= 0.01:
                scale_factor *= 10
                values = [value * 10 for value in values]
                profits = [profit * 10 for profit in profits]
                wallet_capacity = wallet_capacity * 10
                break
        else:
            values = [round(value) for value in values]
            return values, profits, wallet_capacity, scale_factor
