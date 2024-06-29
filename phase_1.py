

import sqlite3



# Phase 1 - Starter
# 
# Note: Display all real/float numbers to 2 decimal places.

connection = 'db/CIS4044-N-SDI-OPENMETEO-PARTIAL.db'
'''
Satisfactory
'''
#im
def select_all_countries(connection):
    # Queries the database and selects all the countries 
    # stored in the countries table of the database.
    # The returned results are then printed to the 
    # console.
    try:
        # Define the query
        query = "SELECT * from [countries]"
        with sqlite3.connect( connection) as connection:
        # Get a cursor object from the database connection
        # that will be used to execute database query.
            cursor = connection.cursor()

        # Execute the query via the cursor object.
            results = cursor.execute(query)

        # Iterate over the results and display the results.
            for row in results:
                  print(f"Country Id: {row[0]} -- Country Name: {row[1]} -- Country Timezone: {row[2]}")           
    except sqlite3.OperationalError as ex:
        print(ex)


def select_all_cities(connection):
    query = "SELECT * FROM cities"                                                             
    with sqlite3.connect(connection) as connection: 
        connection.row_factory = sqlite3.Row   
        cursor = connection.cursor()
        results = cursor.execute(query)

    for row in results:
        print(f"Cities Id: {row['id']} -- Cities Name: {row['name']} -- Cities Longitude:{row['longitude']} -- Cities Latitude:{row['latitude']} -- Country Id{row['country_id']}")


'''
Good
'''
def average_annual_temperature(connection, city_id, year):
    query = "SELECT city_id, strftime('%Y', date) AS year, AVG(mean_temp) AS Avg_ann_temp " \
            "FROM daily_weather_entries " \
            f"WHERE city_id = ? AND year = ? " \
            "GROUP BY city_id, year"

    with sqlite3.connect(connection) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        results = cursor.execute(query, (city_id, str(year)))

        for row in results:
            avg_ann_temp = round(row['Avg_ann_temp'], 2)
            print(f"city_id: {row['city_id']} -- Avg_ann_temp: {avg_ann_temp} -- year: {row['year']}")

            
pass


def average_seven_day_precipitation(connection, city_id, start_date):
    query = "SELECT AVG(precipitation) AS avg_7_day_precip " \
            "FROM daily_weather_entries " \
            "WHERE city_id = ? AND date BETWEEN ? AND date(?, '+7 days')"

    with sqlite3.connect(connection) as conn:
        cursor = conn.cursor()
        results = cursor.execute(query, (city_id, start_date, start_date))

        for row in results:
            avg_7_day_precip = round(row[0], 2)  # Fetching value from the first column (index 0) of the result row
            print(f"City ID: {city_id} -- Average 7-Day Precipitation from {start_date}: {avg_7_day_precip} mm")




'''
Very good
'''

def average_mean_temp_by_city(connection, date_from, date_to):
    query = "SELECT city_id, AVG(mean_temp) AS avg_mean_temp " \
            "FROM daily_weather_entries " \
            "WHERE date BETWEEN ? AND ? " \
            "GROUP BY city_id"

    with sqlite3.connect(connection) as conn:
        cursor = conn.cursor()
        results = cursor.execute(query, (date_from, date_to))

    for row in results:
            city_id = row[0]  
            avg_mean_temp = round(row[1], 2)  
            print(f"City ID: {city_id} -- Average Mean Temperature between {date_from} and {date_to}: {avg_mean_temp} °C")


   
pass

import sqlite3

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

        for row in results:
            country_name = row[0]  # Accessing the country name at index 0
            avg_annual_precipitation = round(row[1], 2)  # Accessing the avg annual precipitation at index 1
            print(f"Country: {country_name} -- Average Annual Precipitation in {year}: {avg_annual_precipitation} mm")



    
   

'''
Excellent

You have gone beyond the basic requirements for this aspect.

'''
if __name__ == "__main__":
    connection = 'db/CIS4044-N-SDI-OPENMETEO-PARTIAL.db'
    
    # Call all functions
    select_all_countries(connection)
    select_all_cities(connection)
    average_annual_temperature(connection, 1, 2020)
    average_seven_day_precipitation(connection, 1, '2020-01-01')
    average_mean_temp_by_city(connection, '2020-01-01', '2020-12-31')
    average_annual_precipitation_by_country(connection, 2020)

 #print(query)


    # Create a SQLite3 connection and call the various functions
    # above, printing the results to the terminal.


    
