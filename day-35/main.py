import os
import requests
from twilio.rest import Client

api_key = "YOUR_API_KEY"
url = f"https://api.openweathermap.org/data/2.5/forecast"
account_sid = "YOUR_TWILIO_SID"
auth_token = "YOUR_TWILIO_TOKEN"

weather_params = {
    "lat":24.672241,
    "lon":121.760341,
    "appid":api_key,
    "cnt":4,
}
will_rain = False
response = requests.get(url, params=weather_params)
weather_data = response.json()
print(weather_data)
# print(weather_data["list"][0]["weather"][0]["id"])
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Today is raining!. Remember to bring ☔☔",
        from_="+18125794047",
        to="+917671949628",
    )
    print(message.status)