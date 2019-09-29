import random
from datetime import datetime
from flask import Flask, request, send_from_directory, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

room_1 = {
    'id': "",
    'name': "",
    'co2': 0,
    'hum': 0,
    'voc': 0,
    'tmp': 0
}

room_2 = {
    'id': "",
    'name': "",
    'co2': 0,
    'hum': 0,
    'voc': 0,
    'tmp': 0
}

room_list = [room_1, room_2]


@app.route('/')
def root():
    return send_from_directory('', 'index.html')


@app.route('/get-data')
def get_data():
    return_data = {
        'extern': {
            'id': "STAT1",
            'name': "Station 1",
            'date_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'no2': random.randint(15, 200),
            'pm10': random.randint(20, 70)
        },
        'intern': room_list
    }
    return jsonify(return_data)


@app.route('/send-data', methods=['GET', 'POST'])
def send_data():
    data = request.get_json(force=True)
    if data['id'] == "O1":
        room_1['id'] = data['id']
        room_1['name'] = data['name']
        room_1['temp'] = int(data['tmp'])
        room_1['hum'] = int(data['hum'])
        room_1['co2'] = int(data['co2'])
        room_1['voc'] = int(data['voc'])
    elif data['id'] == "O2":
        room_2['id'] = data['id']
        room_2['name'] = data['name']
        room_2['temp'] = int(data['tmp'])
        room_2['hum'] = int(data['hum'])
        room_2['co2'] = int(data['co2'])
        room_2['voc'] = int(data['voc'])
    print(data)
    return "Done"
