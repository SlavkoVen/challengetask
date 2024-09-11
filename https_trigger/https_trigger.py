# https_trigger.py
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def https_trigger():
    print("HTTPS Trigger activated!")
    print("Request Method:", request.method)
    print("Request Headers:", request.headers)
    print("Request Data:", request.data)
    return "HTTPS Trigger received!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
