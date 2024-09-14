from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def firestore_trigger():
    event_data = request.get_json()  # Отримання JSON-повідомлення від Firestore
    if event_data:
        # Розбір та виведення деталей події
        print("Firestore Trigger activated!")
        print("Event Data:", event_data)
        
        return jsonify({"message": "Event received", "event_data": event_data}), 200
    else:
        return 'Invalid event data', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
