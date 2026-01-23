# ☁️Cloud-Based-IoT-Weather-Monitoring-System (Simulated)
## 🌦️IoT Weather Monitoring System 
An Internet of Things (IoT) project that simulates real-time weather data and uploads it to the ThingSpeak cloud platform for visualization and analysis. 
This system continuously sends temperature, humidity, and rainfall data at fixed intervals using Python.

## 📌Project Overview

This project demonstrates how sensor-like data can be generated, transmitted, and visualized using cloud-based IoT services. Instead of physical sensors, randomized values are used to simulate real environmental conditions, making it ideal for learning and prototyping IoT workflows.

## 🔍Data Parameters

* 🌡️Temperature (°C)

* 💧Humidity (%)

* 🌧️Rainfall (mm)

## ⚙️Technologies Used
* Python 3
* ThingSpeak IoT Platform
* REST API
* Requests Library
* Cloud Data Visualization

## 🧠How It Works
* Random values for temperature, humidity, and rainfall are generated.
* Data is sent to ThingSpeak using its REST API.
* Each parameter is mapped to a separate field in a ThingSpeak channel.
* Data is uploaded every 15 seconds.
* Values can be viewed live on ThingSpeak dashboards and charts.

## Clone The repository
```
git clone https://github.com/your-username/iot-weather-thingspeak.git
cd iot-weather-thingspeak
```
### Configure API Key
```
API_KEY = "YOUR_API_KEY"
```
### Run The Script
```
python weather_iot.py
```
## ✨Output Visualizer

### Temperature
<img width="562" height="275" alt="image" src="https://github.com/user-attachments/assets/cfce3471-40ae-4ce3-a3ec-f4322bc097f6" />



### Humidity
<img width="562" height="275" alt="image" src="https://github.com/user-attachments/assets/c794363d-f388-4c8a-91ab-cc110f58344f" />




### Rainfall
<img width="562" height="275" alt="image" src="https://github.com/user-attachments/assets/12f05633-7f35-479b-baf0-81e5b147b69b" />

## 📊Logs


<img width="562" height="400" alt="image" src="https://github.com/user-attachments/assets/38628797-262d-4efc-b922-8c21179c9d82" />


