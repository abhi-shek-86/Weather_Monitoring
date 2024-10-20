from flask import Flask, jsonify, render_template
from pymongo import MongoClient
import requests
from datetime import datetime

app = Flask(__name__)

# MongoDB Connection Setup
client = MongoClient('mongodb://localhost:27017/')  # Your MongoDB connection string
db = client['weather_data']  # Database name
collection = db['daily_summary']  # Collection name

API_KEY = '90a5f96984ee931d5a1674ba70172055'  # Replace with your OpenWeatherMap API key
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    weather_data = {}

    # Fetch weather data for each city
    for city in CITIES:
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric')

        if response.status_code == 200:
            data = response.json()
            city_weather = {
                'city': city,
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'timestamp': datetime.now()  # Store the current timestamp
            }
            
            # Insert the weather data into MongoDB
            collection.insert_one(city_weather)

            # Prepare data for display in the frontend
            weather_data[city] = {
                'temperature': city_weather['temperature'],
                'description': city_weather['description'],
                'timestamp': city_weather['timestamp'].strftime('%Y-%m-%d %H:%M:%S')
            }
        else:
            weather_data[city] = {'error': 'City not found or Invalid API key'}

    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True)
