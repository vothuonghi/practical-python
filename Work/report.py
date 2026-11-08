# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                'name': record['name'],
                'shares': int(record['shares']),
                'price': float(record['price'])
            }

            portfolio.append(stock)

    return portfolio

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    prices = {}
    with open(filename, 'rt') as f:
        rows= csv.reader(f)

        for row in rows:
            try:
                prices[row[0]]=float(row[1])
            except IndexError:
                pass
    return prices

def make_report_data(portfolio, prices):
    """
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    """
    rows = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        summary = (stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    return rows


def print_report(reportdata):
    '''
    Print a nicely formated table from a list of (name, shares, price, change) tuples.
    '''
    headers = ('Name', 'Shares', 'Price', 'Changes')
    print(f"{headers[0]:10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}")
    print(('-'*10 + ' ')*len(headers))
    for row in reportdata:  
        print(f"{row[0]:10s} {row[1]:>10d} {row[2]:>10.2f} {row[3]:>10.2f}")

def portfolio_report(portfoliofile, pricefile):
    '''
    Make a stock report given portfolio and price data file.
    '''
    # Read date file
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report_data(portfolio, prices)

    # Print it out
    print_report(report)

portfolio_report('Data/portfolio.csv', 'Data/prices.csv')