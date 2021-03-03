"""
This modules defines the classes used to store and manage the shares
"""

import algorithms.optimized as op
import algorithms.brute_force as bf
import algorithms.algo_utils as au

import csv


class Share:
    """
    This class is used to store the informations of a share
    """

    def __init__(self, name, value, yield_):
        self.name = name
        self.value = float(value)
        self.yield_ = float(yield_)
        self.profit = self.value * self.yield_ / 100


class SharesManager:
    """
    This class is used to store the list of shares availables for selection.
    """

    def __init__(self, *shares):
        if shares:
            self.shares = shares
        else:
            self.shares = []

    @property
    def values(self):
        return [share.value for share in self.shares]

    @property
    def profits(self):
        return [share.profit for share in self.shares]

    @property
    def names(self):
        return [share.name for share in self.shares]

    def import_csv(self, csv_path):
        """
        This method is called to import the shares from a csv file
        """

        with open(csv_path) as csvfile:
            spamreader = csv.reader(csvfile)
            shares_raw = [row for row in spamreader][1:]

        self.shares = [
                    Share(name, value, yield_)
                    for id_, name, value, yield_ in shares_raw
                ]

    def clean_up_ands_scale(self, wallet_capacity):
        """
        This method calls the dunction clean_sample and scale_sample to refine
        the shares sample
        """
        values, profits, names = au.clean_sample(
            self.values, self.profits, self.names, wallet_capacity)
        values, profits, wallet_capacity, scale_factor = au.scale_sample(
            values, profits, wallet_capacity)
        return values, profits, names, scale_factor

    def optimized(self, wallet_capacity):
        """
        This method is called to run the optimized algorithm on the list of
        shares of the ShareManager object.
        It returns the result as a tuple:
            * best_profit is the profit made in the shares currency
            * best_shares is a dictionnary that contains as key the name of the
            shares to be selected to achieve the best profit, and as values the
            quantity of shares to pick.
            * size of the sample analyzed
        """
        values, profits, names, scale_factor = self.clean_up_ands_scale(
            wallet_capacity)
        clean_sample_size = len(values)
        best_profit, best_shares = op.optimized(
            values, profits, names, wallet_capacity, scale_factor)

        return best_profit, best_shares, clean_sample_size

    def brute_force(self, wallet_capacity):
        """
        This method is called to run the brute force algorithm on the list
        of shares of the ShareManager object.
        It returns the result as a tuple:
            * best_profit is the profit made in the shares currency
            * best_shares is a dictionnary that contains as key the name of the
            shares to be selected to achieve the best profit, and as values the
            quantity of shares to pick.
            * size of the sample analyzed
        """

        best_profit, best_shares = bf.brute_force(
            self.values, self.profits, self.names, wallet_capacity)

        return best_profit, best_shares, len(self)

    def get_share_by_name(self, share_name):
        """
        This method returns a share object from the name of a share
        """
        for share in self.shares:
            if share.name == share_name:
                return share

    def __len__(self):
        return len(self.shares)
