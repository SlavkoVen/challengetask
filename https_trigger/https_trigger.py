from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_request():
    if request.method == 'GET':
        return 'GET request received'
    elif request.method == 'POST':
        return 'POST request received'
    elif request.method == 'PUT':
        return 'PUT request received'
    elif request.method == 'DELETE':
        return 'DELETE request received'
    else:
        return 'Method Not Allowed', 405

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
