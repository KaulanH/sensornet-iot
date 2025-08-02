# SensorNet: Edge-to-Cloud IoT Monitoring System 🌡️📡

A full-stack project that captures environmental sensor data on a microcontroller and visualizes it in real time via a cloud-based dashboard.

---

## 📦 Project Overview

This system demonstrates how modern IoT systems collect, transmit, and visualize sensor data. Built with computer engineering and software engineering principles in mind.

**System Components:**

| Layer        | Technology            |
|--------------|------------------------|
| Embedded     | ESP32, DHT22 Sensor    |
| Backend API  | Python + Flask         |
| Database     | SQLite (PostgreSQL optional) |
| Frontend     | React + Chart.js       |
| Communication| HTTP (WiFi)            |
| Deployment   | Render / Vercel / GitHub Pages |

---

## 🚀 Features

- 📡 Real-time temperature/humidity data capture
- 🌐 REST API for data ingestion and retrieval
- 📊 Dashboard with dynamic data charts
- 🔔 Threshold alert system
- ☁️ Cloud-deployable

---
## LESGO ##
## 🗂️ Project Structure

## Setting Arduino Nano
Your goal is to:
Collect data from a sensor (e.g., temperature, light, motion) on your microcontroller.
Send that data over serial or Wi-Fi (depending on the board) to your MacBook.
POST that data to the Flask server at http://127.0.0.1:5000/sensor-data.