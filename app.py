import csv
import io
from base64 import b64decode

from flask import Flask, request, jsonify

from solver import build_graph


app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/api/graph', methods=['POST'])
def create_dot_file():
    try:
        num_partitions = request.json['num_partitions']
    except KeyError:
        return json_error(400, 'Missing parameter num_partitions')

    # decode CSV data, parse with DictReader and convert to list
    csv_encoded = request.json.get('csv_encoded')
    csv_decoded = b64decode(csv_encoded).decode('utf-8')
    students = list(csv.DictReader(io.StringIO(csv_decoded), delimiter=';'))

    try:
        cost, G = build_graph(
            students=students,
            num_partitions=num_partitions,
            friendship_weight=request.json.get('friendship_weight', 30),
            classmate_weight=request.json.get('classmate_weight', 3),
            schoolmate_weight=request.json.get('schoolmate_weight', 1),
            teacher_multiplier=request.json.get('teacher_multiplier', 100),
            node_weights_to_ubvec=request.json.get('node_weights_to_ubvec', {
                'total': 1.05,
            }),
        )
    except ValueError as e:
        # usually when METIS fails to partitionfor some reason
        return json_error(400, str(e))

    return jsonify({
        'cost': cost,
        'dot': G.to_string(),
    })


# helper class for JSON errors
def json_error(status_code, message):
    response = jsonify({
        'status': status_code,
        'message': message,
    })
    response.status_code = status_code
    return response


# Enable CORS for local development
@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Headers'] = '*'
    header['Access-Control-Allow-Methods'] = '*'
    return response


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
