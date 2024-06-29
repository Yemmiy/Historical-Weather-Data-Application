import requests
import sqlite3
import openmeteo_requests
import requests_cache
from retry_requests import retry

connection = sqlite3.connect('db/CIS4044-N-SDI-OPENMETEO-PARTIAL.db')


def retreive_from_open_meteor():

    #Setup the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after = -1)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)
    # Open-Meteo API endpoint and parameters
    api_endpoint = "https://archive-api.open-meteo.com/v1/archive"
    # Define the parameters for fetching weather data
    # Add necessary parameters like location, time range, etc.
    params = {
        "latitude": 1.44367,
        "longitude": 43.60426,
        "start_date":"2016-01-01",
        "end_date": "2016-06-31",
        "daily": ["temperature_2m_max", "temperature_2m_min", "temperature_2m_mean", "precipitation_sum"],
        "timezone": "Europe/London"
    }

    #GET request to Open-Meteo API
    response = requests.get(api_endpoint, params=params)
    print(response.text)

    data = response.json()

    latitude = data['latitude']

    date = data['daily']['time']

    temperature_2m_max = data['daily']['temperature_2m_max']
    temperature_2m_min = data['daily']['temperature_2m_min']
    temperature_2m_mean = data['daily']['temperature_2m_mean']
    precipitation_sum = data['daily']['precipitation_sum']

    return date, temperature_2m_max, temperature_2m_min, temperature_2m_mean, precipitation_sum

def update_database(connection):
    # Connect to the database
    
    cursor = connection.cursor()

    # Iterate through the data and insert into the database
    date, temperature_2m_max, temperature_2m_min, temperature_2m_mean, precipitation_sum = retreive_from_open_meteor()
    for i in range(len(date)):
        cursor.execute('''
            INSERT INTO daily_weather_entries (date, min_temp, max_temp, mean_temp, precipitation, city_id)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (date[i], temperature_2m_max[i], temperature_2m_min[i], temperature_2m_mean[i], precipitation_sum[i], 1))

   

    connection.commit()  # Commit changes to the database
    connection.close()  # Close the database connection
update_database(connection)

# else:
#     print("Failed to retrieve data. Status code:", response.status_code)
