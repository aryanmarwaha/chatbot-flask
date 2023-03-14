import init
from flask import Flask
from flask_ngrok import run_with_ngrok
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)
run_with_ngrok(app)

@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    resp = VoiceResponse()
    resp.say("Hello 911, What's you'r emergency ?")

    return str(resp)

if __name__=='__main__':
	app.run()