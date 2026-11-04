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
            holding = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2])
            }

            portfolio.append(holding)

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

def make_port(porfolio, prices):
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

# Read data files and create the report data
portfolio = read_portfolio('./Data/portfolio.csv')
prices = read_prices('./Data/prices.csv')
report = make_port(portfolio, prices)

# Generate the report data
headers = ('Name', 'Shares', 'Price', 'Changes')
print(f"{headers[0]:10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}")
print(('-'*10 + ' ')*len(headers))
for row in report:  
    print(f"{row[0]:10s} {row[1]:>10d} {row[2]:>10.2f}  {row[3]:>10.2f}")




# # Calculate the total cost of the portfolio
# total_cost = 0.0
# for s in portfolio:
#     total_cost += s['shares']*s['price']

# print('Total cost', total_cost)

# # Compute the current value of the portfolio
# total_value = 0.0
# for s in portfolio:
#     total_value += s['shares']*prices[s['name']]

# print('Current value', total_value)
# print('Gain', total_value - total_cost)

