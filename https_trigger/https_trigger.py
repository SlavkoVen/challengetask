from flask import Flask, request
import logging

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_https_request():
    # Print request details
    logging.info('Received HTTPS request')
    logging.info(f'Headers: {request.headers}')
    logging.info(f'Body: {request.get_data(as_text=True)}')
    
    return 'Request received', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
