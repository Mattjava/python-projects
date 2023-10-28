import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

load_dotenv("D:/Programs/Python/.env.txt")

NEWS_KEY = os.getenv("NewsAPIKey")
STOCK_KEY = os.getenv("StockAPIKey")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

yesterday = datetime.today().date() - timedelta(days = 1)

day_before = yesterday - timedelta(days=1)


news_param = {
    "apiKey": NEWS_KEY,
    "q": COMPANY_NAME
}

news_url = requests.get(url=NEWS_ENDPOINT, params=news_param)
news_articles = news_url.json()["articles"]
recent_news_articles = news_articles[:2]

stock_param = {
    "apikey": STOCK_KEY,
    "symbol": STOCK,
    "function": "TIME_SERIES_DAILY"
}

stock_url = requests.get(url=STOCK_ENDPOINT, params=stock_param)
stock_data = stock_url.json()["Time Series (Daily)"]

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 

yesterday_stock = stock_data[str(yesterday)]
previous_stock = stock_data[str(day_before)]

stock_change = round((float(yesterday_stock["4. close"]) - float(previous_stock["4. close"]))/float(previous_stock["4. close"]) * 100)


## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator

if stock_change >= 5 or stock_change <= -5:
    print(f"Tesla stock has by {stock_change}%")

print(recent_news_articles)

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

