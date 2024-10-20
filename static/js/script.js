document.getElementById('fetchWeather').addEventListener('click', async () => {
    const response = await fetch('/weather');
    const weatherData = await response.json();
    const weatherResults = document.getElementById('weatherResults');
    weatherResults.innerHTML = '';

    for (const city in weatherData) {
        if (weatherData[city].error) {
            weatherResults.innerHTML += `<p>${city}: ${weatherData[city].error}</p>`;
        } else {
            weatherResults.innerHTML += `
                <p>${city}: ${weatherData[city].temperature}°C, ${weatherData[city].description}</p>
            `;
        }
    }
});
