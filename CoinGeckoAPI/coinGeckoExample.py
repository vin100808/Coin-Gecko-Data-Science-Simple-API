from pycoingecko import CoinGeckoAPI
import pandas as pd
import plotly.graph_objects as go
import plotly.offline as offline

cg = CoinGeckoAPI() # Instance 

# This returns the price, market cap, volumns of bitcoin in the last 30 days with their corresponding Unix timestamp
bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)

# Only interested in the time and the price at that time
bitcoin_price_data = bitcoin_data['prices']

# Convert the nested list into a DataFrame
data = pd.DataFrame(bitcoin_price_data, columns = ['TimeStamp', 'Price'])

# Given timestamp data is in Unix and difficult to understand
# We append a new column Data using the pandas to_datatime with the timestamp as input and unit in ms
data['Date'] = pd.to_datetime(data['TimeStamp'], unit='ms')

# Create a candlestick plot
# For the daily candlesticks, we will group the date to find the min, max, first and last price of the day
candlestick_data = data.groupby(data.Date.dt.date).agg({'Price': ['min', 'max', 'first', 'last']})

# Use Plotly to create the candlestick chart and plot it
fig = go.Figure(data=[go.Candlestick(x= candlestick_data.index,
                open=candlestick_data['Price']['first'],
                high=candlestick_data['Price']['max'],
                low=candlestick_data['Price']['min'],
                close=candlestick_data['Price']['last'])
                ])

fig.update_layout(xaxis_rangeslider_visible=False, xaxis_title='Date',
yaxis_title='Price (USD $)', title='Bitcoin Candlestick Chart Over Past 30 Days')

offline.plot(fig, filename='candlestick_plot.html')


#print(candlestick_data)
