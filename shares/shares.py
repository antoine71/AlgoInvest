from utils.utils import product_lists
import algorithms.knapsack as ks
import algorithms.brute_force as bf

from itertools import product
import csv


class Share:

    def __init__(self, name, value, yield_):
        self.name = name
        self.value = float(value)
        self.yield_ = float(yield_)
        self.profit = self.value * self.yield_ / 100


class SharesManager:

    def __init__(self, *shares):
        if shares:
            self.shares = shares
        else:
            self.shares = []

    def import_csv(self, csv_path):
        with open(csv_path) as csvfile:
            spamreader = csv.reader(csvfile)
            shares_raw = [row for row in spamreader][1:]

        self.shares = [
                    Share(name, value, yield_)
                    for id_, name, value, yield_ in shares_raw
                ]

    def knapsack(self, wallet_capacity, step=0.1):
        shares = [share for share in self.shares if share.value <= wallet_capacity]
        values = [int((1 / step) * share.value) for share in shares]
        profits = [share.profit for share in shares]
        names = [share.name for share in shares]
        knapsack_wallet_capacity = int((1 / step) * wallet_capacity)

        best_profit, best_shares = ks.knapsack(values, profits, names, knapsack_wallet_capacity)

        return best_profit, best_shares

    def get_share_by_name(self, share_name):
        for share in self.shares:
            if share.name == share_name:
                return share

    def brute_force(self, wallet_capacity):
        shares = [share for share in self.shares if share.value <= wallet_capacity]
        values = [int(share.value) for share in shares]
        profits = [share.profit for share in shares]
        names = [share.name for share in shares]

        best_profit, best_shares = bf.brute_force(values, profits, names, wallet_capacity)

        return best_profit, best_shares

    def brute_force_(self, wallet_capacity):

        max_number_of_shares = [wallet_capacity // share_value for share_value in self.values]

        shares_combinations_product = product(*[list(range(i + 1)) for i in max_number_of_shares])
        shares_combinations = [combinations for combinations in shares_combinations_product]

        possible_shares_combinations = [combinations for combinations in shares_combinations
                                        if sum(product_lists(self.values, combinations)) == wallet_capacity]

        possible_combinations_profits = [sum(product_lists(self.profits, combinations))
                                         for combinations in possible_shares_combinations]

        best_combinations_profit = max(possible_combinations_profits)
        best_combinations_index = possible_combinations_profits.index(best_combinations_profit)
        best_combinations = possible_shares_combinations[best_combinations_index]

        return best_combinations_profit, best_combinations

    def __len__(self):
        return len(self.shares)
