from pymongo import MongoClient

# MongoDB Connection
MONGO_URI = "mongodb://localhost:27017/"  # Change to your MongoDB URI if using Atlas
DB_NAME = "weather_data"
COLLECTION_NAME = "daily_summary"


API_KEY = '90a5f96984ee931d5a1674ba70172055'
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']

def get_db_connection():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    return db[COLLECTION_NAME]

def store_summary(daily_summary):
    collection = get_db_connection()
    for index, row in daily_summary.iterrows():
        document = {
            "city": row['city'],
            "avg_temp": row['avg_temp'],
            "max_temp": row['max_temp'],
            "min_temp": row['min_temp'],
            "dominant_condition": row['dominant_condition'],
            "date": row['date'].strftime('%Y-%m-%d')
        }
        collection.insert_one(document)
