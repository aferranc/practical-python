# report.py
#
# Exercise 2.4

import csv
import sys

def read_prices(filename):
    '''Reads a set of prices into a dictionary'''

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if len(row) > 0:
                print(row)
            
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/prices.csv'

read_prices(filename)