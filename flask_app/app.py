import json

from flask import Flask, request, Response

app = Flask(__name__)

pray_requests_data = []

latest_id = 1

@app.route('/pray-requests/', methods=['GET'])
def get_pray_requests():
    return Response(
        json.dumps(pray_requests_data),
        mimetype='application/json',
    )

@app.route('/pray-requests/', methods=['POST'])
def create_pray_request():
    global latest_id
    pray_requests_data.append({
        'id': latest_id,
        'massage': request.get_json()['massage'],
    })
    latest_id += 1
    return Response(
        json.dumps(pray_requests_data),
        mimetypes='application/json'
    )