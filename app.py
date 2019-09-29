import random
from datetime import datetime
from flask import Flask, request, send_from_directory, jsonify
from flask_cors import CORS
from temp_u_hum import TempHum
from no_u_pm import NoPm

app = Flask(__name__, static_url_path='', static_folder='')
cors = CORS(app)

th = TempHum()
np = NoPm()

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
    return app.send_static_file('index.html')


@app.route('/get-data')
def get_data():
    th_data = th.get_data()
    np_data = np.get_data()
    return_data = {
        'extern': {
            'id': "STAT1",
            'name': "Station 1",
            'date_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'no2': random.randint(15, 200),
            'pm10': random.randint(20, 70),
            'temp': random.randint(0, 45),
            'hum': random.randint(20, 100)
            # 'no2': np_data['no2'],
            # 'pm10': np_data['pm10'],
            # 'temp': th_data['temp'],
            # 'hum': th_data['hum']
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
