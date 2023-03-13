from twilio.rest import Client

from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

import json
with open("./config/config.json") as f:
	config= json.load(f)
with open("./Users.json") as f:
	Users= json.load(f)

account_sid= config["app"]["TWILIO_ACCOUNT_SID"]
auth_token= config["app"]["TWILIO_AUTH_TOKEN"]

client= Client(account_sid,auth_token)


if __name__=='__main__':
	call= client.calls.create(
		twiml= '',
		to= config["app"]["RECIVER_PHONE"],
		from_=Users["user1"]["PHONE_NUMBER"]
		)

	print(call.sid)