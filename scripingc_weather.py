import requests
import json

city_name = "Mishima"
api_key = "3c170209ee20b3f00a6b7225d6338cc3"
web_api = "http://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&APPID={key}"
url = web_api.format(city=city_name, key=api_key)
print(url)

requests = requests.get(url)
data = requests.json()
data = data["weather"][0]["main"]
json_text = json.dumps(data, indent=4)
print(json_text)
