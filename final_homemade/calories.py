import requests

def calories(QUERY, GENDER, AGE, WEIGHT, HEIGHT):
    URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

    id = "6217db9e"
    key = "ac102405d9dd79552e91f101f1bdb0a0"
    header = {
        "x-app-id": id,
        'x-app-key': key
    }

    parameters = {
        'query': QUERY,
        "gender": GENDER,
        "weight_kg": WEIGHT,
        "height_cm": HEIGHT,
        "age": AGE,
    }

    response = requests.post(url=URL, json=parameters, headers=header)
    response.raise_for_status()
    result = response.json()

    return result["exercises"][0]["nf_calories"]