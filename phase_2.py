import matplotlib.pyplot as plt
import sqlite3
import numpy as np

connection = 'db/CIS4044-N-SDI-OPENMETEO-PARTIAL.db'

def average_annual_precipitation_by_country(connection, year):
    query = "SELECT c.name, AVG(dwe.precipitation) AS avg_annual_precipitation " \
            "FROM daily_weather_entries dwe " \
            "JOIN cities ci ON dwe.city_id = ci.id " \
            "JOIN countries c ON ci.country_id = c.id " \
            "WHERE strftime('%Y', dwe.date) = ? " \
            "GROUP BY c.name"

    with sqlite3.connect(connection) as conn:
        cursor = conn.cursor()
        results = cursor.execute(query, (str(year),))

        countries = []
        avg_precipitation = []

        for row in results:
            countries.append(row[0])
            avg_precipitation.append(round(row[1], 2))

        # Creating a bar chart for average yearly precipitation by country
        plt.figure(figsize=(10, 6))
        plt.bar(countries, avg_precipitation, color='blue')
        plt.xlabel('Country')
        plt.ylabel('Average Yearly Precipitation (mm)')
        plt.title(f'Average Yearly Precipitation by Country ({year})')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()




def average_temp_rainfall_scatter(connection):
    query = "SELECT AVG(mean_temp) AS avg_temp, AVG(precipitation) AS avg_precip, city_id " \
            "FROM daily_weather_entries " \
            "GROUP BY city_id"

    with sqlite3.connect(connection) as conn:
        cursor = conn.cursor()
        results = cursor.execute(query)

        avg_temp = []
        avg_precip = []

        for row in results:
            avg_temp.append(round(row[0], 2))
            avg_precip.append(round(row[1], 2))

        # Creating a scatter plot for average temperature against average rainfall for cities
        plt.figure(figsize=(8, 6))
        plt.scatter(avg_precip, avg_temp, color='blue', alpha=0.7)
        plt.xlabel('Average Rainfall')
        plt.ylabel('Average Temperature')
        plt.title('Average Temperature vs Average Rainfall for Cities')
        plt.tight_layout()
        plt.show()



def grouped_bar_chart_city_weather(connection, city_ids):
    query = "SELECT city_id, MIN(mean_temp) AS min_temp, MAX(mean_temp) AS max_temp, AVG(mean_temp) AS avg_temp, " \
            "MIN(precipitation) AS min_precip, MAX(precipitation) AS max_precip, AVG(precipitation) AS avg_precip " \
            "FROM daily_weather_entries " \
            f"WHERE city_id IN ({','.join(map(str, city_ids))}) " \
            "GROUP BY city_id"

    with sqlite3.connect(connection) as conn:
        cursor = conn.cursor()
        results = cursor.execute(query)

        city_ids = []
        min_temp = []
        max_temp = []
        avg_temp = []
        min_precip = []
        max_precip = []
        avg_precip = []

        for row in results:
            city_ids.append(row[0])
            min_temp.append(round(row[1], 2))
            max_temp.append(round(row[2], 2))
            avg_temp.append(round(row[3], 2))
            min_precip.append(round(row[4], 2))
            max_precip.append(round(row[5], 2))
            avg_precip.append(round(row[6], 2))

        # Creating grouped bar charts for weather data of selected cities
        bar_width = 0.2
        index = range(len(city_ids))
        plt.figure(figsize=(12, 6))

        plt.bar(index, min_temp, width=bar_width, label='Min Temp')
        plt.bar([i + bar_width for i in index], max_temp, width=bar_width, label='Max Temp')
        plt.bar([i + 2 * bar_width for i in index], avg_temp, width=bar_width, label='Avg Temp')
        plt.bar([i + 3 * bar_width for i in index], min_precip, width=bar_width, label='Min Precip')
        plt.bar([i + 4 * bar_width for i in index], max_precip, width=bar_width, label='Max Precip')
        plt.bar([i + 5 * bar_width for i in index], avg_precip, width=bar_width, label='Avg Precip')

        plt.xlabel('City IDs')
        plt.ylabel('Values')
        plt.title('Weather Data for Selected Cities')
        plt.xticks([i + 2 * bar_width for i in index], city_ids)
        plt.legend()
        plt.tight_layout()
        plt.show()


def grouped_bar_chart_country_weather(connection, country_id):
    query = "SELECT MIN(mean_temp) AS min_temp, MAX(mean_temp) AS max_temp, AVG(mean_temp) AS avg_temp, " \
            "MIN(precipitation) AS min_precip, MAX(precipitation) AS max_precip, AVG(precipitation) AS avg_precip " \
            "FROM daily_weather_entries dwe " \
            "JOIN cities ci ON dwe.city_id = ci.id " \
            "JOIN countries c ON ci.country_id = c.id " \
            "WHERE c.id = ?"

    with sqlite3.connect(connection) as conn:
        cursor = conn.cursor()
        results = cursor.execute(query, (country_id,))

        for row in results:
            min_temp, max_temp, avg_temp = round(row[0], 2), round(row[1], 2), round(row[2], 2)
            min_precip, max_precip, avg_precip = round(row[3], 2), round(row[4], 2), round(row[5], 2)

            # Data for bar chart
            temp_values = [min_temp, max_temp, avg_temp]
            precip_values = [min_precip, max_precip, avg_precip]

            bar_width = 0.35
            index = np.arange(3)

            # Creating grouped bar chart for temperature and precipitation
            plt.figure(figsize=(10, 6))
            plt.bar(index, temp_values, bar_width, label='Temperature')
            plt.bar(index + bar_width, precip_values, bar_width, label='Precipitation')

            plt.xlabel('Metrics')
            plt.ylabel('Values')
            plt.title(f'Temperature and Precipitation Metrics for Country ID: {country_id}')
            plt.xticks(index + bar_width / 2, ['Min', 'Max', 'Avg'])
            plt.legend()
            plt.tight_layout()
            plt.show()


def avg_rainfall_vs_temp_by_date_for_city(connection, city_id):
    query = "SELECT AVG(mean_temp) AS avg_temp, AVG(precipitation) AS avg_precip, date " \
            "FROM daily_weather_entries " \
            "WHERE city_id = ? " \
            "GROUP BY date"

    with sqlite3.connect(connection) as conn:
        cursor = conn.cursor()
        results = cursor.execute(query, (city_id,))

        avg_temp = []
        avg_precip = []
        dates = []

        for row in results:
            avg_temp.append(round(row[0], 2))
            avg_precip.append(round(row[1], 2))
            dates.append(row[2])  # Assuming 'date' is in a suitable format

        # Creating a scatter plot for average rainfall against average temperature by date for the city
        plt.figure(figsize=(8, 6))
        plt.scatter(avg_precip, avg_temp, color='blue', alpha=0.7)
        plt.xlabel('Average Rainfall')
        plt.ylabel('Average Temperature')
        plt.title(f'Average Rainfall vs Average Temperature by Date for City ID: {city_id}')
        plt.tight_layout()
        plt.show()

def avg_precipitation_for_cities_in_period(connection, cities, start_date, end_date):
    query = f"SELECT city_id, AVG(precipitation) AS avg_precipitation " \
            f"FROM daily_weather_entries " \
            f"WHERE city_id IN ({','.join(map(str, cities))}) AND date BETWEEN ? AND ? " \
            f"GROUP BY city_id"

    with sqlite3.connect(connection) as conn:
        cursor = conn.cursor()
        results = cursor.execute(query, (start_date, end_date))

        city_ids = []
        avg_precipitation = []

        for row in results:
            city_ids.append(row[0])
            avg_precipitation.append(round(row[1], 2))

        # Creating a list of colors for each bar
        colors = ['blue', 'green', 'red', 'orange', 'purple']  

        # Creating a bar chart for average precipitation by city within the specified period
        plt.figure(figsize=(10, 6))
        bars = plt.bar(city_ids, avg_precipitation, color=colors[:len(city_ids)])  # Assigning colors to bars
        plt.xlabel('City IDs')
        plt.ylabel('Average Precipitation')
        plt.title(f'Average Precipitation for Cities ({start_date} to {end_date})')
        plt.xticks(rotation=45, ha='right')

        # Adding a legend for colors
        plt.legend(bars, [f'City {city_id}' for city_id in city_ids])

        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    connection = 'db/CIS4044-N-SDI-OPENMETEO-PARTIAL.db'

    average_annual_precipitation_by_country(connection, '2020')
    average_temp_rainfall_scatter(connection)
    grouped_bar_chart_city_weather(connection, [1, 2, 3, 4])
    grouped_bar_chart_country_weather(connection, 2)
    avg_rainfall_vs_temp_by_date_for_city(connection, 2)
    avg_precipitation_for_cities_in_period(connection, [1, 2, 3, 4], '2020-01-01', '2022-12-31')



