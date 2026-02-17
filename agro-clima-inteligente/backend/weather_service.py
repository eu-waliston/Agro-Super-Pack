import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timezone

load_dotenv()

def get_weather(lat: float, lon: float):

    url = "https://api.open-meteo.com/v1/forecast"

    params = {

        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        "hourly": "temperature_2m,precipitation,windspeed_10m",
        "forecast_days": 2,
        "timezone": "auto"
    }

    response = requests.get(url, params=params)

    response.raise_for_status()
    return response.json()


from datetime import datetime


def format_forecast(weather_data):
    hourly = weather_data.get("hourly", {})

    times = hourly.get("time", [])
    temps = hourly.get("temperature_2m", [])
    winds = hourly.get("windspeed_10m", [])
    rain = hourly.get("precipitation", [])

    forecast = []

    now_str = weather_data.get("current_weather", {}).get("time")
    if not now_str:
        return []

    now_dt = datetime.fromisoformat(now_str)

    start_index = 0

    for i, t in enumerate(times):
        t_dt = datetime.fromisoformat(t)
        if t_dt >= now_dt:
            start_index = i
            break

    for i in range(start_index, min(start_index + 12, len(times))):
        forecast.append({
            "hora": datetime.fromisoformat(times[i]).strftime("%Hh"),
            "temperatura": temps[i],
            "vento": winds[i],
            "chuva_mm": rain[i]
        })

    return forecast
