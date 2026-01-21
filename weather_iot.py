import requests
import random
import time

API_KEY = "YOUR_API_KEY"
URL = "https://api.thingspeak.com/update"

while True:
  temperature = round(random.uniform(20,40),2)
  humidity = round(random.uniform(40,90),2)
  rainfall = round(random.uniform(0,20),2)
  
  payload = {
    "api_key":API_KEY,
    "field1":temperature,
    "field2":humidity,
    "field3":rainfall
  }
  response = requests.get(URL,params=payload)
  print("Sent data -> Temp:",temperature,"Humidity:",humidity,"Rainfall:",rainfall)
  time.sleep(15)