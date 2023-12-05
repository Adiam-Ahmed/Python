import requests
import json
from datetime import datetime
from config import APP_ID, API_KEY, AUTHORIZATION, SHEET_ENDPOINT, GENDER, WEIGHT_KG, HEIGHT_CM, AGE


query = input("What exercise did you do today? ")
url = "https://trackapi.nutritionix.com/v2/natural/exercise"
current_datetime = datetime.now()

# Content-Type": "application/json indicates to server that request body in JSON format,
# allowing the server to properly parse and interpret the data.
headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

data = {
    'query': query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE

}

# Construct the request
# json.dumps(data) method is used to convert the Python dictionary (data) to a JSON string,
# similar to JSON.stringify() in JavaScript.
response = requests.post(url, headers=headers, data=json.dumps(data))

# Handle the response
if response.status_code == 200:
    # Successful request, handle the response
    data = response.json()
    print(data)
    exercise = data["exercises"][0]
    name = exercise["name"]
    duration_min = exercise["duration_min"]
    calories_burned = exercise["nf_calories"]
    date = current_datetime.strftime("%Y/%m/%d")
    time = current_datetime.strftime("%H:%M:%S")
    

    body = {
        'workout': {
            "date": date,
            "time": time,
            "exercise": name,
            "duration": duration_min,
            "calories": calories_burned
        }
    }

    header = {
        "Content-Type": "application/json",
        "Authorization": AUTHORIZATION,
    }

    response = requests.post(SHEET_ENDPOINT, data=json.dumps(body), headers=header)

    if response.status_code == 200:
        result = response.json()
        print(f"Row added successfully. Response: {result}")
    else:
        # Handle the error
        print(f"Error: {response.status_code} - {response.text}")


else:
    # Handle the error
    print(f"Error: {response.status_code} - {response.text}")


