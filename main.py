from controllers.application_controller import ApplicationController

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

controller = ApplicationController(args.file, args.wallet, args.algorithm)
controller.run()
