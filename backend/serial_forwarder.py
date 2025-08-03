import serial
import requests
import time

SERIAL_PORT = 'COM3'
BAUD_RATE = 9600
API_URL = 'http://127.0.0.1:5000/sensor-data'

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def read_and_send():
    with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2) as ser:
        time.sleep(2)  # Wait for Arduino reset
        while True:
            line = ser.readline().decode('utf-8').strip()
            if line:
                print(f"Raw data received: '{line}'")  # Debug print
                if is_float(line):
                    temperature = float(line)
                    try:
                        response = requests.post(API_URL, json={"temperature": temperature})
                        print(f"Sent {temperature}°F to API, response code: {response.status_code}")
                    except requests.exceptions.RequestException as e:
                        print(f"Failed to send data: {e}")
                else:
                    print("Received non-numeric data, skipping...")
            time.sleep(2)

if __name__ == "__main__":
    read_and_send()
