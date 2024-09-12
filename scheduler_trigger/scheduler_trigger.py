from flask import Flask
import logging

app = Flask(__name__)

@app.route('/', methods=['GET'])
def handle_scheduler_request():
    # Print details of the scheduled job
    logging.info('Scheduler triggered')
    
    return 'Scheduler triggered', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
