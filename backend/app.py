from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = "sensor_data.db"

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            temperature REAL NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)

@app.route("/sensor-data", methods=["POST"])
def receive_data():
    data = request.get_json()
    temperature = data.get("temperature")
    if temperature is None:
        return jsonify({"error": "Missing temperature value"}), 400

    with sqlite3.connect(DATABASE) as conn:
        conn.execute("INSERT INTO data (temperature) VALUES (?)", (temperature,))

    return jsonify({"message": "Data received"}), 201

@app.route("/sensor-data", methods=["GET"])
def get_data():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.execute(
            "SELECT id, temperature, timestamp FROM data ORDER BY timestamp DESC LIMIT 10"
        )
        data = [
            {"id": row[0], "temperature": row[1], "timestamp": row[2]}
            for row in cursor.fetchall()
        ]
    return jsonify(data)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
