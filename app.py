from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/proxy', methods=['GET'])
def proxy():
    key = request.args.get('api_key')
    f1 = request.args.get('field1')
    f2 = request.args.get('field2')
    f3 = request.args.get('field3')
    f4 = request.args.get('field4')

    url = f"https://api.thingspeak.com/update?api_key={key}&field1={f1}&field2={f2}&field3={f3}&field4={f4}"
    r = requests.get(url)
    return f"ThingSpeak response: {r.text}", 200
