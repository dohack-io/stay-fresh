import random
from datetime import datetime
from flask import Flask, request, send_from_directory, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)


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
        'intern': [
            {
                'id': "R1",
                'name': "Raum 1",
                'temp': random.randint(1, 1000),
                'hum': random.randint(1, 1000),
                'co2': random.randint(500, 3000),
                'voc': random.randint(300, 1500)
            },
            {
                'id': "R2",
                'name': "Raum 2",
                'temp': random.randint(1, 1000),
                'hum': random.randint(1, 1000),
                'co2': random.randint(500, 3000),
                'voc': random.randint(300, 1500)
            }
        ]
    }
    return jsonify(return_data)


@app.route('/send-data', methods=['GET', 'POST'])
def send_data():
    print("Connection")
    try:
        data = request.get_json(force=True)
        print(data)
        return "Done"
    except Exception as e:
        print(e)
        return e
