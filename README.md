# SensorNet: Edge-to-Cloud IoT Monitoring System 🌡️📡

A full-stack project that captures environmental sensor data on a microcontroller and visualizes it in real time via a dashboard.

---
Material Needed:
Arduino IDE
Arduino Nano
USB Cable
---

## 📦 Project Overview

This system demonstrates how modern IoT systems collect, transmit, and visualize sensor data. Built using both computer engineering and software engineering principles.

**System Components:**

| Layer        | Technology                      |
|--------------|----------------------------------|
| Embedded     | Arduino Nano + TMP36 Sensor      |
| Communication| Serial (USB) or HTTP (WiFi*)     |
| Backend API  | Python + Flask                   |
| Database     | SQLite                           |
| Frontend     | React + Chart.js (planned)       |
| Deployment   | Localhost (Render/GitHub optional) |

> *Originally designed for ESP32 over Wi-Fi, currently implemented using Arduino Nano over USB serial.

---

## 🚀 Features

- 📡 Real-time temperature data capture from TMP36 sensor
- 🔌 Serial communication from Arduino to Mac/PC
- 🌐 Flask API for POSTing and retrieving sensor data
- 📊 Backend stores and serves sensor readings
- 🛠️ Ready for frontend integration (React + Chart.js)
- ☁️ Designed to be cloud-deployable

---

## 🧰 Getting Started (Current Progress)

### 1. Arduino Nano + TMP36 Setup

- TMP36 sensor connected to analog pin A0
- Code reads analog voltage, converts to Celsius
- Data is sent via Serial (USB) every few seconds

### 2. Flask Backend (Python)

- Reads serial data from Arduino using `pyserial`
- Sends data to `/sensor-data` POST endpoint
- Stores data in memory or SQLite

Run the backend server:
```bash
source venv/bin/activate      # Activate virtual environment
python app.py                 # Starts Flask server at http://127.0.0.1:5000

### Current Status:
You have a working Flask backend (app.py) that:

Receives temperature data via a POST API (/sensor-data).

Stores data in a SQLite database.

Serves stored data via GET API (/sensor-data).

Your Arduino Nano reads temperature from a TMP36 sensor and sends the temperature as a plain numeric string via serial (USB).

The Python script serial_forwarder.py:

Reads the serial data from Arduino over USB (e.g., COM3).

Parses the temperature values.

Forwards those temperature readings to the Flask backend API by making POST requests.

# SensorNet IoT Dashboard

## Overview

This project captures temperature data from a TMP36 sensor connected to an Arduino Nano, sends it via serial to a Python backend, which exposes a RESTful API built with Flask. The data is stored in a SQLite database and displayed live on a web dashboard.

## Features

- Arduino TMP36 temperature sensing
- Python serial forwarder to POST sensor data to API
- Flask REST API with GET and POST endpoints
- SQLite for lightweight data storage
- Responsive web dashboard with live updating via JavaScript
- Separation of frontend and backend concerns

## Folder Structure
/frontend
/backend
app.py
serial_forwarder.py
create_table.py
sensor_data.db
venv/


## Requirements

- Python 3.x
- Flask
- pyserial
- SQLite3

## Setup Instructions

1. Clone the repo
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows

pip install -r requirements.txt
python create_table.py
python app.py
python serial_forwarder.py
http://127.0.0.1:5000
