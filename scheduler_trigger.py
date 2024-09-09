# scheduler_trigger.py
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def scheduler_trigger():
    scheduler_event = request.json
    print("Scheduler Trigger activated!")
    print("Event Details:", scheduler_event)
    return "Scheduled job received!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
