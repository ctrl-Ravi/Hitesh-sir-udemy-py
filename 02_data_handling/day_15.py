"""
 Challenge: Real-Time Weather Logger (API + CSV)

Build a Python CLI tool that fetches real-time weather data for a given city and logs it to a CSV file for daily tracking.

Your program should:
1. Ask the user for a city name.
2. Fetch weather data using the OpenWeatherMap API.
3. Store the following in a CSV file (`weather_log.csv`):
   - Date (auto-filled as today's date)
   - City
   - Temperature (in °C)
   - Weather condition (e.g., Clear, Rain)
4. Prevent duplicate entries for the same city on the same day.
5. Allow users to:
   - Add new weather log
   - View all logs
   - Show average, highest, lowest temperatures, and most frequent condition

Bonus:
- Format the output like a table
- Handle API failures and invalid city names gracefully
"""

import csv
import os
from datetime import datetime
import requests
from collections import Counter


FILENAME= "weather_logs.csv"

API_KEY="hidden"
#Key are usually hidden in .env file but that is for later

if not os.path.exists(FILENAME):
    with open(FILENAME, 'w', newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "City", "Temperature", "Condition"])


def log_weather():
    cityname= input("Enter Your City Name: ").strip().lower()
    date= datetime.now().strftime("%Y-%m-%d")

    with open(FILENAME, 'r', encoding="utf-8") as f:
        reader=csv.DictReader(f)


        for row in reader:
            if row['Date']== date and row["City"].lower()== cityname:
                print("Entry for this city and date exists")
                return
            
    try:
        url =f"https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={API_KEY}&units=metric"
        response= requests.get(url)
        object= response.json()

        if response.status_code !=200:
            print(f"API Error")
            return
        temp= object["main"]["temp"]
        condition = object["weather"][0]["main"]

        with open(FILENAME, "+a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([date,cityname.title(),temp, condition])
            print("👇" * 30)
            print(f"Logged: {temp} {condition}, in {cityname.title()} on {date}")

    except Exception as e:
        print("Failed to API call")


def view_logs():
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        if len(rows) <=1:
            print("No Entry Available")
            return
        for row in rows:
            print(f"{row['Date']}, {row['City']}, {row['Temperature']}, {row['Condition']}")

def stat_logs():
    with open(FILENAME, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        stats = list(reader)
        if len(stats) <=1:
            print("No Entry Available")
            return
        max_temp= max(row['Temperature'] for row in stats)
        min_temp= min(row['Temperature'] for row in stats)
        average_temp= sum(float(row['Temperature']) for row in stats)/len(stats)
        freq_condition, count= Counter(row['Condition'] for row in stats).most_common(1)[0]
        print("_" * 30)

        print(f" Average temp: {average_temp}\n Highest Temperature: {max_temp}\n lowest temp: {min_temp}\n most frequent condition: {freq_condition}")

        print("_" * 30)

def main(): 
    while True:
        print("*" * 30)
        print("Real time weather logger")
        print("1. Add weather log")
        print("2. View All logs")
        print("3. Show average, highest, lowest temperatures, and most frequent condition logs")
        print("*" * 30)

        Choice = input("Choose and option: ").strip().lower()

        match Choice:
            case "1": log_weather()
            case "2": view_logs()
            case "3": stat_logs()
            case _ : print("Invalid Choice")


if __name__ == "__main__":
    main()