import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "API_KEY_FROM_OPENWEATHER"
account_sid = "ACCOUNT_ID_FROM_TWILIO"
auth_token = "TOKEN_FROM_TWILIO"

weather_params = {
    "lat": 36.055180,
    "lon": -95.833931,
    "cnt": 4,
    "appid": api_key
}


def check_for_rain(weather_list):
    for weather_id in weather_list:
        if weather_id["weather"][0]["id"] < 700:
            return True

    return False


response = requests.get(OWM_Endpoint, params=weather_params)
# print(response.status_code)
response.raise_for_status()
data = response.json()['list']

will_rain = check_for_rain(data)

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an ☔",
            from_='PHONE_NUMBER_FROM_TWILIO',
            to='TO_THE_NUMBER_YOU_WANT_TO_MESSAGE'
        )

    print(message.status)
