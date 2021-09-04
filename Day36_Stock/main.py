from datetime import date
from datetime import timedelta

import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY = 'WZPM0O9AJBDD69S5'
NEWS_API_KEY = '5588e163888a4f0cb7ec2facd2a8941b'

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]


param = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": API_KEY
}
request = requests.get(STOCK_ENDPOINT, params=param)
data = request.json()["Time Series (Daily)"]

today = date.today()
yesterday = today - timedelta(days=1)

yesterday_closing_price = data[str(yesterday)]['4. close']

# of
data_list = [value for (key, value) in data.items()]
print(type(yesterday_closing_price))
print(yesterday_closing_price)

# TODO 2. - Get the day before yesterday's closing stock price
day_before_day = data[str(yesterday - timedelta(days=1))]
# print(day_before_day)

# of
new_day_before = data_list[1]['4. close']
print(new_day_before)

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
#  Hint: https://www.w3schools.com/python/ref_func_abs.asp

positive_difference = abs(float(yesterday_closing_price) - float(new_day_before))
print(positive_difference)
# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day
#  before yesterday.

difference_percentage = (positive_difference / float(new_day_before)) * 100
print(difference_percentage)

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if difference_percentage > 0.1:
    param_news = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }
    news_request = requests.get(NEWS_ENDPOINT, params=param_news)
    news_data = news_request.json()["articles"]

    # TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

    first_three_articles = news_data[0:3]

    print(first_three_articles)

    # TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

    headline_and_desc = [f"Headline: {article['title']}.\nBrief: {article['description']} " for article in
                         first_three_articles]
    print(headline_and_desc)
## STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 9. - Send each article as a separate message via Twilio.
else:
    print("Nada")

# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
