import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_URL = "https://www.alphavantage.co/query?"
STOCK_API = "XXXXXXXXXXXXXXXXXXXXX"
STOCK_PARAMETERS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API
}
account_sid = "XXXXXXXXXXXXXXXXXXXXX"
auth_token = "XXXXXXXXXXXXXXXXXXXXX"
# STEP 1: Use https://www.alphavantage.co
response = requests.get(url=STOCK_URL, params=STOCK_PARAMETERS)
response.raise_for_status()
my_stock_data = response.json()['Time Series (Daily)']
lis = [key for (key, value) in my_stock_data.items()]
my_stock_list = lis[:4]
percent_change = (float(my_stock_data[my_stock_list[0]]["1. open"]) - float(
    my_stock_data[my_stock_list[1]]["4. close"])) / float(my_stock_data[my_stock_list[1]]["4. close"])
percent_change *= 100
print(f"{round(percent_change, 2)}%")
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
NEWS_URL = "https://newsapi.org/v2/everything"
NEWS_API = "XXXXXXXXXXXXXXXXXXXXX"
NEWS_PARAMETERS = {
    "qInTitle": "tesla",
    "from": my_stock_list[0],
    "language": "en",
    "sortBy": "popularity",
    "apikey": NEWS_API
}
if abs(percent_change) >= 0.1:
    news_response = requests.get(url=NEWS_URL, params=NEWS_PARAMETERS)
    print(news_response)
    my_news = news_response.json()['articles']
    print(my_news)
    client = Client(account_sid, auth_token)
    for i in range(3):
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=f"{my_news[i]['title']}",
            to='whatsapp:+91xxxxxxxxxx'
        )
