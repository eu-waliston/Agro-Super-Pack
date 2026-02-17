import requests
import os
from dotenv import load_dotenv
from datetime import datetime

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

# def check_alerts(data):
#     alerts = []
#
#     if data["vento_kmh"] > 25:
#         alerts.append("⚠️ Risco de dano por vento forte")
#
#     if data["temperatura_atual"] < 5:
#         alerts.append("❄️ Risco de geada")
#
#     if chuva_proxima_6h > 30:
#         alerts.append("🌧️ Alerta de chuva intensa")
#
#     return alerts
#
# def apply_rules(weather, cultura):
#     rules = db.get_rules(cultura)
#     score = 100
#
#     for rule in rules:
#         if compare(weather[rule.parametro], rule.operador, rule.valor):
#             score += rule.impacto_score
#
#     return max(0, min(100, score))
