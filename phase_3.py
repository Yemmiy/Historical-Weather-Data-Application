import phase_1
import phase_2
import phase_4



connection = phase_2.connection


def average_annual_precipitation_by_country(connection, year):
    phase_2.average_annual_precipitation_by_country(connection, year)


def average_temp_rainfall_scatter(connection):
    phase_2.average_temp_rainfall_scatter(connection)


def grouped_bar_chart_city_weather(connection, city_ids):
    phase_2.grouped_bar_chart_city_weather(connection, city_ids)


def grouped_bar_chart_country_weather(connection, country_id):
     phase_2.grouped_bar_chart_country_weather(connection, country_id)


def avg_rainfall_vs_temp_by_date_for_city(connection, city_id):
     phase_2.avg_rainfall_vs_temp_by_date_for_city(connection, city_id)


def avg_precipitation_for_cities_in_period(connection, cities, start_date, end_date):
    phase_2.avg_precipitation_for_cities_in_period(connection, cities, start_date, end_date)




if __name__ == "__main__":
    connection = 'db/CIS4044-N-SDI-OPENMETEO-PARTIAL.db'

    print("1. Average Annual Precipitation by Country")
    print("2. Average Temperature vs Rainfall Scatter")
    print("3. Grouped Bar Chart for City Weather")
    print("4. Grouped Bar Chart for Country Weather")
    print("5. Average Rainfall vs Temperature by Date for City")
    print("6. Average Precipitation for Cities in a Period")

    selection = int(input("Please select the graph you'll like to check: "))
    if selection == 1:
        year = input("Enter year: ")
        average_annual_precipitation_by_country(connection, year)
    elif selection == 2:
            average_temp_rainfall_scatter(connection)
    elif selection == 3:
        city_id = input("Enter city_id: ")
        grouped_bar_chart_city_weather(connection, city_id) 
    elif selection == 4:
        country_id = input("Enter country_id: ")
        grouped_bar_chart_country_weather(connection, country_id)
    elif selection == 5:
        city_id = input("Enter city_id: ")
        avg_rainfall_vs_temp_by_date_for_city(connection, city_id)
    elif selection == 6:
        city_id = input("Enter city_id: ")
        start_date =input("Enter start date: ")
        end_date = input("Enter end date: ")
        avg_precipitation_for_cities_in_period(connection, [city_id], start_date, end_date)
    else:
        print("Invalid selection")




def  select_all_countries(connection):
    phase_1.select_all_countries(connection)

def  select_all_cities(connection):
    phase_1.select_all_cities(connection)


def average_annual_temperature(connection, city_id, year):
    phase_1.average_annual_temperature(connection, city_id, year)

def average_seven_day_precipitation(connection, city_id, start_date):
    phase_1.average_seven_day_precipitation(connection, city_id, start_date)

def average_mean_temp_by_city(connection, start_date, end_date):
    phase_1.average_mean_temp_by_city(connection, start_date, end_date)

def average_annual_precipitation_by_country(connection, year):
 phase_1.average_annual_precipitation_by_country(connection, year)




if __name__ == "__main__":
        connection = 'db/CIS4044-N-SDI-OPENMETEO-PARTIAL.db'


        print("Select an option:")
        print("1. Select all countries")
        print("2. Select all cities")
        print("3. Calculate average annual temperature")
        print("4. Calculate 7-day average precipitation")
        print("5. Calculate average mean temperature by city")
        print("6. Calculate average annual precipitation by country")
        

selection = int(input("Enter number between 1-6: "))


if selection == 1:
    country_id = input("Enter country_id:")
    select_all_countries(connection)
        
elif selection == 2:
    select_all_cities(connection)
elif selection == 3:
    city_id = (input("Enter city ID: "))
    year = (input("Enter year: "))
    average_annual_temperature(connection, city_id, year)
elif selection == 4:
    city_id = (input("Enter city ID: "))
    date = input("Enter start date (YYYY-MM-DD): ")
    average_seven_day_precipitation(connection, city_id, date)
elif selection == 5:
    start_date = input("Enter start date from 2016-01-01 ")
    end_date = input("Enter end date from 2022-12-31: ")
    average_mean_temp_by_city(connection, start_date, end_date)
elif selection == 6:
    year = (input("Enter year: "))
    average_annual_precipitation_by_country(connection, year)

else:
    print("Invalid selection")



if __name__ == "__main__":
             connection = 'db/CIS4044-N-SDI-OPENMETEO-PARTIAL.db'
def retreive_from_open_meteor():
  phase_4.retreive_from_open_meteor()

# Function logic to update the database using the provided connection

def update_database(connection):
    phase_4.update_database(connection)
    

def main():
    print("Welcome to the Meteor Data Management System")
    print("1. Retrieve data from Open Meteor")
    print("2. Update database")

selection = int(input("Enter number 1 or 2: "))

if selection == 1:
        retreive_from_open_meteor()
elif selection == 2:
        update_database(connection)
else:
        print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()





