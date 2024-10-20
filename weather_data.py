import requests
from datetime import datetime

def fetch_weather_data(city, API_KEY):
    response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric')
    if response.status_code == 200:
        data = response.json()
        city_weather = {
            'city': city,
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'timestamp': datetime.now()
        }
        return city_weather
    else:
        return None
