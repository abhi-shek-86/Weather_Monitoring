import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

def plot_temperature_trends():
    # Connect to the SQLite database
    conn = sqlite3.connect('weather.db')
    
    # Fetch data from the database
    df = pd.read_sql_query("SELECT * FROM daily_summary", conn)
    
    # Close the database connection
    conn.close()
    
    # Convert 'date' column to datetime format if it's not already
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
