from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = "sensor_data.db"

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute("CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, value REAL, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)")

@app.route("/sensor-data", methods=["POST"])
def receive_data():
    data = request.get_json()
    value = data.get("value")

    with sqlite3.connect(DATABASE) as conn:
        conn.execute("INSERT INTO data (value) VALUES (?)", (value,))

    return jsonify({"message": "Data received"}), 201

@app.route("/sensor-data", methods=["GET"])
def get_data():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.execute("SELECT * FROM data ORDER BY timestamp DESC LIMIT 10")
        data = [{"id": row[0], "value": row[1], "timestamp": row[2]} for row in cursor.fetchall()]
    return jsonify(data)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)

