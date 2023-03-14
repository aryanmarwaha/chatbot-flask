from twilio.rest import Client
import json
import os

with open("./config/Users.json") as f1:
	Users= json.load(f1)

account_sid= os.environ.get('TWILIO_ACCOUNT_SID')
auth_token= os.environ.get('TWILIO_AUTH_TOKEN')

client= Client(account_sid,auth_token)

# print(client)
# call= client.calls.create(
# 	twiml="<Response><Say>Hello this is 911, What's you'r emergency ? </Say></Response>",
# 	to=Config['app']['RECIVER_PHONE'],
# 	from_=Users['user1']['PHONE_NUMBER']
# 	)

# print(call.sid)