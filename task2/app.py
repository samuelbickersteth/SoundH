from flask import Flask, request, jsonify
import os
import logging
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.INFO)

# Create a counter for the number of requests
REQUEST_COUNT = Counter('request_count', 'Total number of HTTP requests')

# The message to return, set via environment variable
MESSAGE = os.getenv('MESSAGE', 'Hello, World!')

@app.route('/api/message', methods=['GET'])
def get_message():
    REQUEST_COUNT.inc()  # Increment the counter
    logging.info(f'Request from {request.remote_addr}')
    return jsonify({"message": MESSAGE})

@app.route('/metrics', methods=['GET'])
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
