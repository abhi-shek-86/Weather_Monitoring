from config import TEMP_THRESHOLD

def check_alerts(df):
    # Check if any city temperature exceeds the threshold for two consecutive updates
    for city in df['city'].unique():
        city_data = df[df['city'] == city]
        if len(city_data) >= 2:
            if city_data.iloc[-1]['temp'] > TEMP_THRESHOLD and city_data.iloc[-2]['temp'] > TEMP_THRESHOLD:
                print(f"Alert: Temperature in {city} exceeded {TEMP_THRESHOLD}°C for two consecutive updates.")
