# Weather Application

## Overview

The Weather Application is a web-based platform that provides real-time weather data for multiple cities. Utilizing the OpenWeatherMap API, this application retrieves weather information such as temperature and weather descriptions, storing this data in a MongoDB database for further analysis and visualization. The application features a user-friendly interface built with HTML, CSS, and JavaScript, allowing users to easily access weather information.

## Features

- **Real-Time Weather Data:** Users can fetch current weather information for various cities.
- **Data Visualization:** The application generates temperature trend graphs to help users analyze weather changes over time.
- **Database Integration:** Weather data is stored in MongoDB, ensuring persistent storage for historical analysis.
- **Alerts:** The application checks for temperature alerts, notifying users when temperatures exceed a specified threshold.

## Architecture

### Front-End

The front-end of the application is built using:

- **HTML:** Provides the structure for the web application, including elements like headers, buttons, and result displays.
- **CSS:** Enhances the visual presentation, offering a responsive and attractive user interface with styled buttons and layout adjustments.
- **JavaScript:** Handles user interactions, such as fetching weather data from the server, updating the display with real-time information, and managing user input through event listeners.

The front-end communicates with the back-end using asynchronous HTTP requests, ensuring a smooth and responsive user experience.

### Back-End

The back-end of the application is developed using Flask, a lightweight Python web framework. Key components include:

- **Flask Routes:** Define endpoints that handle requests for weather data. The primary route (`/weather`) fetches weather information from the OpenWeatherMap API and returns it in JSON format.
- **Database Integration:** MongoDB is used to store daily weather summaries, enabling historical data retrieval and analysis. The application connects to the MongoDB database to save weather data and generate insights.
- **Weather Data Fetching:** The application retrieves real-time weather data from the OpenWeatherMap API based on the predefined list of cities. The data is processed and stored in the database for future reference.

## Data Storage

Weather data is stored in a MongoDB collection, allowing for efficient querying and analysis. The schema for each document includes:

- **City:** The name of the city.
- **Temperature:** The current temperature in Celsius.
- **Description:** A brief description of the weather conditions.
- **Timestamp:** The date and time when the data was fetched.

## Data Visualization

The application includes features to visualize temperature trends over time using Matplotlib and Pandas. Users can see how temperatures fluctuate across different cities, which can be valuable for personal or research purposes.


## Screenshots

### Create Rule Page
![Output](https://github.com/abhi-shek-86/Weather_Monitoring/blob/master/Output%20-%20Weather.png)


## Alerts

The application monitors temperature data to trigger alerts when specific thresholds are exceeded. This feature can help users stay informed about extreme weather conditions in their area.


