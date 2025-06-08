import requests

API_KEY = "46cb343f08c9edd5f22c5fc194ec480e"
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    if response.status_code != 200 or "list" not in data:
        return None
    
    forecast = []
    for i in range(0, len(data["list"]), 8):
        entry = data["list"][i]
        day_data = {
            "date": entry["dt_txt"].split(" ")[0],
            "temperature": entry["main"]["temp"],
            "humidity": entry["main"]["humidity"],
            "description": entry["weather"][0]["description"],
            "icon": entry["weather"][0]["icon"]
        }
        forecast.append(day_data)
    return {"city": data["city"]["name"], "forecast": forecast[:7]}  