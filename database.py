import matplotlib.pyplot as plt
import pandas as pd
from pymongo import MongoClient

def fetch_data_from_mongo():
    client = MongoClient("mongodb://localhost:27017/")  # Change to your MongoDB URI if using Atlas
    db = client['weather_data']
    collection = db['daily_summary']
    
    # Fetch data from MongoDB
    df = pd.DataFrame(list(collection.find()))
    return df

def plot_temperature_trends():
    df = fetch_data_from_mongo()
    
    # Convert 'date' column to datetime format
    df['date'] = pd.to_datetime(df['date'])

    # Plot temperature trends for each city
    for city in df['city'].unique():
        city_data = df[df['city'] == city]
        plt.plot(city_data['date'], city_data['avg_temp'], label=f"{city} Avg Temp")

    # Add titles and labels
    plt.title("Daily Temperature Trends")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")

    # Rotate the date labels on the x-axis for better readability
    plt.xticks(rotation=45)

    # Add a legend
    plt.legend()

    # Display the plot
    plt.show()

# Call this function in the web app or during testing
plot_temperature_trends()
