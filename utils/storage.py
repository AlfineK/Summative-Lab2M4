import os
import json
from models.user import User

DATA_FILE="data/tracker_data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE,"r") as file:
            data=json.load(file)
            User._customers.clear()
            return [User.from_dict(user_data) for user_data in data]
    except json.JSONDecodeError:
        print("Error reading data file. starting with empty data")
        return []

def save_data(users):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    data=[user.to_dict() for user in users]

    with open(DATA_FILE,"w") as file:
        json.dump(data,file,indent=4)

