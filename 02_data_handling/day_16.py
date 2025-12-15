"""
Sample data:
Date,City,Temperature,Condition
2025-06-11,Delhi,36.5,Clear
2025-06-12,Delhi,37.8,Sunny
2025-06-13,Delhi,38.0,Sunny
2025-06-14,Delhi,34.2,Rain
2025-06-15,Delhi,35.0,Clouds
2025-06-16,Delhi,33.4,Rain
2025-06-17,Delhi,34.7,Clear

Plot graphs from this data


"""



import csv
from collections import defaultdict 
import matplotlib.pyplot as plt


FILENAME= "weather_logs.csv"

def visualize_weather():
    date=[]
    temps = []
    condition= defaultdict(int)

    with open(FILENAME, 'r', encoding="utf-8") as f:
        reader= csv.DictReader(f)
        for row in reader:
            try:
                date.append(row["Date"])
                temps.append(float(row["Temperature"]))
                condition[row["Condition"]] +=1
            except Exception:
                continue
    if not date:
        print("No data found in weather_logs.csv to plot.")
        return
    plt.figure(figsize=(10,7))
    plt.plot(date, temps, marker='o')
    plt.title("Temperature over time")
    plt.xlabel("Date")
    plt.ylabel("Temperature")
    plt.tight_layout()
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(7,5))
    plt.bar(condition.keys(), condition.values(), color='skyblue')
    plt.xlabel("Condition")
    plt.ylabel("Days")
    plt.show()


visualize_weather()