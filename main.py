from shares.shares import SharesManager
from views.result_view import ResultView

import argparse

parser = argparse.ArgumentParser(description="Find the most valuable shares combination")
parser.add_argument(
    "-f", "--file",
    type=str,
    default="data/sample.csv",
    help="Path to the csv file containing a list of shares, values and yields\
    (default: data/sample.csv)")
parser.add_argument(
    "-w", "--wallet",
    type=int,
    default=500,
    help="Wallet capacity in Euros (default: 500)")
parser.add_argument(
    "-a", "--algorithm",
    type=str,
    default="knapsack",
    help="Type of algorithm: knapsack or brute_force\
    (brute force algorithm is not recommended to compute more than 5 shares)\
    (default: knapsack)")

args = parser.parse_args()

shares = SharesManager()
shares.import_csv(args.file)

if args.algorithm == "knapsack":
    result = shares.knapsack(args.wallet)
elif args.algorithm == "brute_force":
    result = shares.brute_force(args.wallet)

ResultView(result, shares).display_result()
