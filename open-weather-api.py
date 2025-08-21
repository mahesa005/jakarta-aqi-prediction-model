import requests
import json

# API_KEY= "29cdbe219b69b47d1c13fea1a85bf2e6"
# lat, lon = 106.79324, -6.236704

BASE_URL = "http://api.openweathermap.org/data/2.5/air_pollution/history"
params = {
    'lat': -6.29225, 
    'lon': 106.806111,
    # 'start': '1596646800',
    # 'end': '1723000799',
    'appid': '29cdbe219b69b47d1c13fea1a85bf2e6'
    }

response = requests.get(BASE_URL, params=params)
json_data = response.json()
output_filename = 'jkt_pol_hist.json'
with open(output_filename, 'w') as json_file:
    json.dump(json_data, json_file, indent=4)
print(response)
