import requests
import matplotlib.pyplot as plt


stock_name = input('Enter the Stock name:').upper()
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = 'https://www.alphavantage.co/query'
NEWS_ENDPOINT = 'https://www.alphavantage.co/query'
SMS_ENDPOINT = 'https://www.twilio.com'

STOCK_API_KEY = 'ENTER YOUR API KEY HERE'

NEWS_PARAMS = {
    'function': 'NEWS_SENTIMENT',
    'tickers': stock_name,
    'apikey': STOCK_API_KEY,
}


STOCK_PARAMS = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': stock_name,
    'apikey': STOCK_API_KEY,
}


response_stock = requests.get(STOCK_ENDPOINT, params=STOCK_PARAMS)

response_news = requests.get(NEWS_ENDPOINT, params=NEWS_PARAMS)
# print(response_stock.json())

data_stock = response_stock.json()['Time Series (Daily)']
data_news = response_news.json()
data_stock_list = list(data_stock.items())
prev_date = data_stock_list[0][0]
prev_prev_date = data_stock_list[1][0]
closing_price_list = []
dates_list = []
for i in range(1, 8):
    closing_price_list.append(float(data_stock_list[i][1]['4. close']))
for i in range(1, 8):
    dates_list.append(data_stock_list[i][0])
y = closing_price_list
x = dates_list[::-1]
plt.plot(x, y)
plt.xlabel('date')
plt.ylabel('closing price')
plt.show()

yesterdays_closing_price = data_stock[str(prev_date)]['4. close']
day_before_yesterday_opening_price = data_stock[str(prev_prev_date)]['1. open']

difference = round(abs(float(day_before_yesterday_opening_price) - float(yesterdays_closing_price)), 2)

print('Closing price on: '+prev_date+' is ' + '$' + yesterdays_closing_price)
print('Opening price on: '+prev_prev_date+' is ' + '$' + day_before_yesterday_opening_price)

print('The difference between the closing price of '+prev_date+' and the opening price of '+prev_prev_date+" is : " +
      str(difference))

# print(data_news['feed'])
for i in data_news['feed']:
    print('\n\n')
    print('Title: \n' + i['title'])
    print('Summary: \n' + i['summary'])
