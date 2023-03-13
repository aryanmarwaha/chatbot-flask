import init

app = Flask(__name__)

@app.route("/answer", methods=['GET', 'POST'])
def answer_call():
    resp = VoiceResponse()
    resp.say("Hello 911. What's Your Emergency")
    return str(resp)

if __name__ == "__main__":
    app.run()