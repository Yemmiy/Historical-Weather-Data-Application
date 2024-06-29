Aim of the Project

This project involves managing and analyzing weather data stored in an SQLite database using Python,
specifically focusing on data retrieval from an external API (Open-Meteo), data visualization,perform various data analysis and
querying the database for various weather-related metrics.
Here's a breakdown of the project's aim, objectives, and steps:

Database Interaction:
Query and retrieve data from an SQLite database (CIS4044-N-SDI-OPENMETEO-PARTIAL.db).
Update the database with weather data retrieved from the Open-Meteo API.

Data Analysis and Visualization:
Calculate and display average annual temperature for cities.
Compute 7-day average precipitation for cities.
Determine average mean temperature by city within specified date ranges.
Compute average annual precipitation by country.
Visualize weather data using bar charts, scatter plots, and grouped bar charts to analyze trends and comparisons.

User Interaction:

Provide a user interface to interact with the database and retrieve specific weather metrics
(such as temperatures and precipitation) based on user input.
Steps Taken in the Project:
Here's a summary of the steps implemented in your project based on the provided code:

Phase 1: Database Interaction and Basic Queries

Implemented functions to query and display all countries and cities stored in the SQLite database 
(select_all_countries, select_all_cities).Calculated average annual temperature (average_annual_temperature)
and 7-day average precipitation (average_seven_day_precipitation) for specific cities.
Computed average mean temperature by city over a specified date range (average_mean_temp_by_city).
Calculated average annual precipitation by country (average_annual_precipitation_by_country).

Phase 2: Data Visualization

Developed functions to visualize average annual precipitation by country using bar charts
(average_annual_precipitation_by_country).Created a scatter plot to show the relationship between average
temperature and rainfall (average_temp_rainfall_scatter).Generated grouped bar charts to display weather data 
(temperature and precipitation) for selected cities (grouped_bar_chart_city_weather) and countries
(grouped_bar_chart_country_weather).Implemented a scatter plot to visualize average rainfall against
average temperature by date for a specific city (avg_rainfall_vs_temp_by_date_for_city).
Created a bar chart to show average precipitation for cities within a specified period
(avg_precipitation_for_cities_in_period).

Phase 3: User Interface

Developed a command-line interface (CLI) to allow users to interact with the database and 
choose specific weather metrics and visualizations based on their input.

Phase 4: Integration with Open-Meteo API

Integrated the Open-Meteo API to retrieve additional weather data such as maximum temperature,
minimum temperature, mean temperature, and precipitation sum.
Updated the SQLite database with the retrieved data using an update_database function.

Summary:
This project focuses on leveraging Python and SQLite to manage, analyze, and visualize weather data.
It includes database operations, API integration for data retrieval, and interactive data visualization to 
support decision-making based on weather patterns and trends. The user interface provides flexibility for 
users to select and view specific weather metrics and insights derived from the data.

