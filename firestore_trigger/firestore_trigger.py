from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def firestore_trigger():
    event_data = request.get_json()  # Get the JSON payload sent by Firestore
    if event_data:
        # Extract and print event details
        event_id = event_data.get('id', 'N/A')
        event_type = event_data.get('type', 'N/A')
        event_data = event_data.get('data', 'N/A')
        
        print(f"Event ID: {event_id}")
        print(f"Event Type: {event_type}")
        print(f"Event Data: {event_data}")

        return jsonify({"message": "Event received"}), 200
    else:
        return 'Invalid event data', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
