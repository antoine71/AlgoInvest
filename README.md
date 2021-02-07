# ALGOINVEST
Openclassrooms - Parcours développement Python Projet 7

## Status
Under development

## Description
This program allows to pick the best combination of shares to maximize the profits after 2 years.
The program can run 2 algorithms:
1. Knapsack: this algorithm is derived from the dynamic programming solution to the knapsack problem. The time complexity of this algorithm is O(n) (time required to evaluate a sample of 100,000 shares: approx. 2 min).
2. Brute Force: this algorithm evaluates all possible combination of shares for a given wallet. It then calculates the profit for each combination and selects the combination with the highest profit. The time complexity of this algorithm is O(2^n) (time required to evaluate a sample of 6 shares: approx. 1 min). This algorithm is very inefficient and is implemented only for testing purpose.

## Installation
* Install Python 3.
* Clone this repository using `$ git clone https://github.com/antoine71/AlgoInvest.git` (you can also download the code [as a zip file](https://github.com/antoine71/AlgoInvest/archive/main.zip)).
* It is not required to setup a virtual environment and install packages to run the application.

## Usage
```
$ python main.py [-h] [-f FILE] [-w WALLET] [-a ALGORITHM]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Path to the csv file containing a list of shares, values and yields 
                        (default: "data/sample.csv")
  -w WALLET, --wallet WALLET
                        Wallet capacity in Euros (default: 500)
  -a ALGORITHM, --algorithm ALGORITHM
                        Type of algorithm: "knapsack" or "brute_force" (brute force algorithm is not 
                        recommended to compute more than 6 shares) (default: "knapsack")
```

The repository contains 3 shares sample files located in the subfolder data that can be used for testing purpose or as templates:
* dataFinance.csv (100,000 shares)
* sample.csv (20 shares)
* sample_short.csv (6 shares)

## Preview
![](/preview.jpg)