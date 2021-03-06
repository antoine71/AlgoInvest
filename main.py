"""
This is the main script of the application.
"""

from controllers.application_controller import ApplicationController

import argparse


parser = argparse.ArgumentParser(description="Find the most valuable shares combination")
parser.add_argument(
    "-f", "--file",
    type=str,
    default="data/dataset2.csv",
    help="Path to the csv file containing a list of shares, values and yields\
    (default: data/dataset2.csv)")
parser.add_argument(
    "-w", "--wallet",
    type=int,
    default=500,
    help="Wallet capacity in Euros (default: 500)")
parser.add_argument(
    "-a", "--algorithm",
    type=str,
    default="optimized",
    help="Type of algorithm: optimized or brute_force\
    (brute force algorithm is not recommended to compute more than 5 shares)\
    (default: optimized)")

args = parser.parse_args()

controller = ApplicationController(args.file, args.wallet, args.algorithm)
controller.run()
