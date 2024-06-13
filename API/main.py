import requests
from twilio.rest import Client

min_temp = 100
max_temp = 0
will_rain = False

account_sid = "account_sid from twilio"
auth_token = "auth token from twilio"
api = "api key by openweather"
parameter = {
    'lat': 27.717245,
    'lon': 85.323959,
    'appid':api,
    'cnt':8,
    'units':'metric'
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameter)
response.raise_for_status()

data = response.json()
print(data)

for x in data['list']:
    if x['main']['temp_min'] < min_temp:
        min_temp = x['main']['temp_min']

    if x['main']['temp_max'] > max_temp:
        max_temp = x['main']['temp_max']

    if x['weather'][0]['id'] < 700:
        will_rain = True

if will_rain:
    sms = f"\nRadhea Radhea🙏🙏Jay Shree Krishna\nToday's weather forecast:\nMax temperature: {max_temp}\nMin_temperature: {min_temp}\nThere is a chance of rain, so please carry an umbrella with you\nb12F_msh\n5n64A"
else:
    sms = f"\nRadhea Radhea🙏🙏Jay Shree Krishna\nToday's weather forecast:\nMax temperature: {max_temp}\nMin_temperature: {min_temp}\nb12F_msh\n5n64A"
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='virtual number by twilio',
    body=sms,
    to='register number on twilio'
)


# link to twilio:   https://www.twilio.com/en-us
# link to openweather api https://openweathermap.org/api