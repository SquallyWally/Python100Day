import os

import requests
from twilio.http.http_client import TwilioHttpClient
from twilio.rest import Client

proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})
account_sid = 'AC20ee3ef84c3fb17b32ec6eba113d40b8'
auth_token = '8f8ede6480d1d1f49824f9b81c0f1f58'
api_key = "9680c16f19b7f57d60a6261b3f053bb3"
OMW_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

link = "https://jsonviewer.stack.hu/"

param = {
    "lat": 52.07667,
    "lon": 4.29861,
    "appid": api_key,
    "exclude": "current,minutely,daily"

}

res = requests.get(OMW_Endpoint, params=param)
res.raise_for_status()
data = res.json()
data_slice = data["hourly"][:12]

gaat_het_regenen = False
for hourly in data_slice:
    condition_code = hourly["weather"][0]["id"]
    # weather codes: https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
    # if ID < 700 --> rain and shit
    if int(condition_code) < 700:
        gaat_het_regenen = True

if gaat_het_regenen:
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(
        body="Het gaat regenen guyo.☂️",
        from_='+16468591457',
        to='+31620406653'
    )

    print(message.status)
