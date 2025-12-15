"""
 Challenge: CSV-TO-JSON Converter Tool

"""

import json
import csv
import os

INPUT_FILE= "weather_logs.csv"

OUTPUT_FILE= f"json{INPUT_FILE}.json"

def load_csv(INPUT_FILE):
    if not os.path.exists(INPUT_FILE):
        print("Csv FIle not found")
        return [] 
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        row= list(reader)
        # print(row)
        try:
            return row
        except:
            print("csv not loaded ")

def convert_json(OUTPUT_FILE,data):
    if not data:
        print("There is no data available to convert")
        return
    with open(OUTPUT_FILE, "w", newline='', encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"converted {len(data)} records to {OUTPUT_FILE}")

def preview_data(data, count=3):
    for row in data[:count]:
        print(json.dumps(row, indent=2)) # dumps use for print the json
    print(".......")
def main():
    print("Converting Csv to json")
    data= load_csv(INPUT_FILE)
    convert_json(OUTPUT_FILE, data )
    preview_data(data)
    print("Succefuly converted")

if __name__== "__main__":
    main()