import pandas_datareader.data as web
from datetime import date
from chart import Grid

# take input
ticker = input("Enter a stock ticker: ")

# get real data
df = web.DataReader(ticker, 'yahoo', start=date.today().replace(year=date.today().year - 1), end=date.today())[['High', 'Low']]
high = df.High
low = df.Low

# chart data
g = Grid(max(high) * 1.1, min(low) * 0.9)

for i in range(len(high)):
    g.action(high[i], low[i])

g.printgrid()
