from datetime import datetime
import pandas as pd
from twilio.rest import Client


account_sid = "account sid from twilio"
auth_token = "auth token by twilio"
virtual_number = "virtual number by twilio"
my_number = "your number"
# link to twilio ---  https://console.twilio.com/

current_date_time = datetime.now()
current_year = current_date_time.year
current_month = current_date_time.month
current_day = current_date_time.day


file = pd.read_csv('bitsathy.csv')
birthday_dict = file.to_dict(orient="records")

for x in birthday_dict:
    if x['month'] == current_month and x['day'] == current_day:
        sms = f'''Radhea Radhea 🙏🙏
        Today is {x['name']} {x['mname']} {x['lname']}'s birthday.
        {x['nickname']} is keeping a new step to {current_year-int(x['year'])+1} year.
        It's {x['name']}'s {current_year-int(x['year'])} birthday.
        Wish {x['name']} a happy birthday.
        b12F'''
        client = Client(account_sid,auth_token)
        message = client.messages.create(
            from_=virtual_number,
            body=sms,
            to=my_number
        )
