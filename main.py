import requests
import os
from twilio.rest import Client
from datetime import date

MY_URL = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("OWN_ACCOUNT_SID")
auth_token = os.environ.get("OWN_AUTH_TOKEN")

parameters = {
    "lat": 44.837788,
    "lon": -0.579180,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=MY_URL, params=parameters)
response.raise_for_status()
weather_data = response.json()
hourly_data = weather_data["hourly"][:12]

raining = False
for data in hourly_data:
    if int(data["weather"][0]["id"]) < 700:
        raining = True

if raining:
    today = date.today()
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"Today's | {today.strftime('%d/%m/%Y')} | Weather report indicates it is going to rain☔, so remember"
             f" your umbrella☂",
        from_='+19388000690',
        to='+447597044364'
    )
else:
    today = date.today()
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f"Today's | {today.strftime('%d/%m/%Y')} | Weather report indicates no rain☔",
        from_='+19388000690',
        to='+447597044364'
    )
    print(message.status)
