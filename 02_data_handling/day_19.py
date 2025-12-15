"""
Challenge : JSON Flattener

{
  "user": {
    "id": 1,
    "name": "Riya",
    "email": "riya@example.com",
    "address": {
      "city": "Delhi",
      "pincode": 110001
    }
  },
  "roles": ["admin", "editor"],
  "is_active": true
}

Flatten this to:

{
  "user.id": 1,
  "user.name": "Riya",
  "user.email": "riya@example.com",
  "user.address.city": "Delhi",
  "user.address.pincode": 110001,
  "roles.0": "admin",
  "roles.1": "editor",
  "is_active": true
}



"""

import json
import os 

INPUT_FILE= "nested_data.json"
OUTPUT_FILE="flattened_data.json"

def flatten_json(data, parent_key='', sep='.'):
    items = {}


    if isinstance(data, dict):
         for k, v in data.items():
             full_key= f"{parent_key}{sep}{k}" if parent_key else k
            #  print(full_key)
             items.update(flatten_json(v, full_key,sep=sep))

    elif isinstance(data, list):
        for idx, item in enumerate(data):
            full_key = f"{parent_key}{sep}{idx}" if parent_key else str(idx)
            print(full_key)
            items.update(flatten_json(item,full_key,sep=sep))
    else:
        items[parent_key] = data # as example here parent key like {is_active : true}

    return items


def main():
    if not os.path.exists(INPUT_FILE):
        print("No Input File found")
        return
    try:
        with open(INPUT_FILE, "r", encoding="utf-8") as f:
            data= json.load(f)

        sep=input("Enter your seperator like {. or - } or skip: ").strip() or '.'


        flattend=flatten_json(data, sep=sep)


        with open(OUTPUT_FILE, "w", encoding="utf-8") as f: 
            json.dump(flattend,f, indent=2) # here f is used because its saving in the output file

        print(f"Flattend json save to {OUTPUT_FILE}")
        print(f"flattend data is\n{json.dumps(flattend)}")

    except Exception as e:
         print("Failed to flattend the data", e)

if __name__=="__main__":
    main()