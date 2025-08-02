from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("sensor_data.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS sensor_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        temperature REAL,
        humidity REAL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )''')
    conn.commit()
    conn.close()

@app.route('/sensor-data', methods=['POST'])
def receive_data():
    data = request.get_json()
    temperature = data.get("temperature")
    humidity = data.get("humidity")
    conn = sqlite3.connect("sensor_data.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO sensor_data (temperature, humidity) VALUES (?, ?)", (temperature, humidity))
    conn.commit()
    conn.close()
    return jsonify({"status": "success"}), 201

@app.route('/sensor-data', methods=['GET'])
def fetch_data():
    conn = sqlite3.connect("sensor_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sensor_data ORDER BY timestamp DESC LIMIT 20")
    rows = cursor.fetchall()
    conn.close()
    data = [{"id": r[0], "temperature": r[1], "humidity": r[2], "timestamp": r[3]} for r in rows]
    return jsonify(data)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

