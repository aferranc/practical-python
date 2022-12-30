# report.py
#
# Exercise 2.4

import csv
from fileparse import parse_csv

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    portfolio = parse_csv(filename ,select=['name','shares','price'], types=[str,int,float])
    return portfolio

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    prices = parse_csv(filename ,types=[str,float], has_headers=False)
    return dict(prices)

def make_report_data(portfolio, prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    rows = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        # current_price = prices[stock['name']]
        change = current_price - stock['price']
        summary = (stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    return rows


portfolio = read_portfolio('Data/portfolio.csv')
prices    = read_prices('Data/prices.csv')

# Generate the report data
report = make_report_data(portfolio, prices)

# Output the report
headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * len(headers))
for row in report:
    price = '${:.2f}'.format(float(row[2]))
    print(f'{row[0]:>10s} {int(row[1]):>10d} {price:>10s} {float(row[3]):>10.2f}')