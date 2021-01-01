import requests
import json

# API　operation
city_name = "Mishima"
api_key = "api_key"
web_api = "http://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&APPID={key}"
url = web_api.format(city=city_name, key=api_key)
print(url)

# Json operation
requests = requests.get(url)
data = requests.json()
data = data["weather"][0]["main"]
json_text = json.dumps(data, indent=4)
print(json_text)
