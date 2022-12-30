# pcost.py
#
# Exercise 1.27

import csv
import sys

def portfolio_cost(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        types = [str, int, float]
        for rowno, row in enumerate(rows, start=1):
            record = { name: func(val) for name, func, val in zip(headers, types, row) }
            try:
                total_cost += record['shares'] * record['price']
            except ValueError:
                print(f"Row {rowno}: Couldn't parse: {row}")
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total purchase cost: {cost:0.2f}')