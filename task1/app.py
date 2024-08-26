import logging
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', handlers=[logging.StreamHandler()])

request_count = 0

@app.route('/api/message', methods=['GET'])
def get_message():
    global request_count
    request_count += 1
    message = os.getenv('MESSAGE', 'Hello, World!')
    app.logger.info('Request from %s', request.remote_addr)
    return jsonify({"message": message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)