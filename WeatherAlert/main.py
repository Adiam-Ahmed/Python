import requests
from twilio.rest import Client
from config import API_KEY, ACCOUNT_SID, AUTH_TOKEN

client = Client(ACCOUNT_SID, AUTH_TOKEN)

API_endpoint = "https://api.openweathermap.org/data/2.5/weather"
MY_LAT = 43.734121
MY_LNG = -79.471066

parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": API_KEY,
    "exclude": "current,minutely,hourly,daily,alerts"
}

response = requests.get(API_endpoint, params=parameters)
weather_data = response.json()


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


wind = weather_data["wind"]["speed"]
weather_temp = round(kelvin_to_celsius(weather_data["main"]["temp"]))
weather_feels_like = round(kelvin_to_celsius(weather_data["main"]["feels_like"]))

print(wind)


if wind > 9:
    message = client.messages.create(
        from_='+15735694405',
        body= f"Hey Adiam, The wind is winding {wind} at {weather_temp}C but feels like {weather_feels_like}C ",
        to='+16477646110'
    )
    print(message.status)
    print(message.sid)

