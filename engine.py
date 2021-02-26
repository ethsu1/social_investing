import os
import alpaca_trade_api as tradeapi


API_KEY = os.environ["ALPACA_API_KEY"]
API_SECRET = os.environ["ALPACA_SECRET"]
APCA_API_BASE_URL = "https://paper-api.alpaca.markets"
'''
Get historical data for a particular ticket symbol
'''
def historical(ticker):
    print(ticker)
    api = tradeapi.REST(API_KEY, API_SECRET,APCA_API_BASE_URL)
    # Get daily price data for AAPL over the last 5 trading days.
    barset = api.get_barset(ticker, 'day', limit=5)
    aapl_bars = barset[ticker]

    # See how much AAPL moved in that timeframe.
    week_open = aapl_bars[0].o
    week_close = aapl_bars[-1].c
    percent_change = (week_close - week_open) / week_open * 100
    print('{} moved {}% over the last 5 days'.format(ticker, percent_change))

'''
get account's current positions
'''
def get_positions():
    api = tradeapi.REST(API_KEY, API_SECRET,APCA_API_BASE_URL)
    positions = api.list_positions()
    if(len(positions) > 0):
        print(positions)
    else:
        print("No positions")

'''
execute a buy order
'''
def buy(ticker, qty):
    api = tradeapi.REST(API_KEY, API_SECRET,APCA_API_BASE_URL)
    a = api.submit_order(symbol=ticker,qty=qty,side='buy',type='market',time_in_force='gtc')
    print(a)
    print(api.list_positions())

'''
get account's current orders
'''
def get_orders():
    api = tradeapi.REST(API_KEY, API_SECRET,APCA_API_BASE_URL)
    orders = api.list_orders()
    if(len(orders) > 0):
        print(order)
    else:
        print("No orders")

if __name__ == "__main__":
    #historical('SQ')
    buy('SQ', 2)
    get_orders()