# firestore_trigger.py
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def firestore_trigger():
    firestore_event = request.json
    print("Firestore Trigger activated!")
    print("Event Details:", firestore_event)
    return "Firestore event received!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
