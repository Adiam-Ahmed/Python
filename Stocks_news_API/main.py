import requests
import smtplib
from datetime import datetime, timedelta
from config import API_KEY_STOCKS, API_KEY_NEWS, smtp_server, my_email,password,smtp_port

my_email = "adiamburhan@gmail.com"
recipients = ["adu.adu911@gmail.com","jimmyhhughes@hotmail.com"]

STOCK_NAME = "TSLA"
COMPANY_NAME = "tesla"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


current_date = datetime.now().date()
yesterday_date = current_date - timedelta(days=1)
day_before_yesterday_date = current_date - timedelta(days=2)
green_arrow_up = "🔼"
red_emoji= "🔻"
stock_emoji=""


news_parameters = {
    "q": COMPANY_NAME,
    "from": current_date,
    "to": yesterday_date,
    "language":"en",
    "sortBy": "popularity",
    "apiKey": API_KEY_NEWS,
}
news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
news_data = news_response.json()


stocks_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": API_KEY_STOCKS,
}
response_stocks = requests.get(STOCK_ENDPOINT, params=stocks_parameters)
stock_data = response_stocks.json()

closing_stocking = [float(value['4. close']) for date, value in stock_data['Time Series (Daily)'].items()]
yesterday_closing_stock = closing_stocking[0]
before_yesterday_closing_stock = closing_stocking[1]

real_difference= yesterday_closing_stock - before_yesterday_closing_stock

positive_difference = abs(yesterday_closing_stock - before_yesterday_closing_stock)
percentage_difference = round((positive_difference / before_yesterday_closing_stock) * 100, 2)
print(percentage_difference)

if real_difference <= 0:
    stock_emoji=red_emoji
else:
    stock_emoji=green_arrow_up

if percentage_difference >= 0:
    with smtplib.SMTP(smtp_server, smtp_port) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        first_three_articles = news_data['articles'][:3]

        # Construct the message
        message = f"Subject: Breaking News: TSLA:{stock_emoji}{round(percentage_difference)}%\n\n"

        for index, news_article in enumerate(first_three_articles, start=1):
            message += f"News {index}:\n"
            message += f"Title: {news_article['title']}\n"
            max_description_length = 200  # Adjust this value based on your preference
            full_description = news_article['description'][:max_description_length]
            message += f"Description: {full_description}...\n"

            message += f"URL: {news_article['url']}\n\n"

        # Encode the message using UTF-8
        msg = message.encode('utf-8')

        # Send the email
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipients,
            msg=msg
        )
