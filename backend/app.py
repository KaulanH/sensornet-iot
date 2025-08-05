from flask import Flask, jsonify, request, send_from_directory
import sqlite3
import os

app = Flask(__name__)

# Serve index.html from frontend folder
@app.route('/')
def serve_index():
    return send_from_directory('../frontend', 'dashboard.html')

# Serve any other frontend assets if you add (e.g. CSS, JS)
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('../frontend', path)

# Your existing sensor-data endpoints:

@app.route('/sensor-data', methods=['GET'])
def get_sensor_data():
    conn = sqlite3.connect('sensor_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, temperature, timestamp FROM sensor_data ORDER BY id DESC LIMIT 10')
    rows = cursor.fetchall()
    conn.close()
    data = [{'id': r[0], 'temperature': r[1], 'timestamp': r[2]} for r in rows]
    return jsonify(data)

@app.route('/sensor-data', methods=['POST'])
def post_sensor_data():
    data = request.get_json()
    print("Received POST data:", data)
    temp = data.get('temperature')
    if temp is None:
        return jsonify({'error': 'Temperature missing'}), 400
    conn = sqlite3.connect('sensor_data.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO sensor_data (temperature, timestamp) VALUES (?, datetime("now"))', (temp,))
    conn.commit()
    conn.close()
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

