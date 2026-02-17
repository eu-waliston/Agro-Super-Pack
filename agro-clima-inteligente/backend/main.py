from fastapi import FastAPI, Query
from weather_service import get_weather
from rules_engine import generate_alerts, calculate_score
from weather_service import format_forecast
from cache import load_cache, save_cache

app = FastAPI(title="AgroClima Inteligente API")


@app.get("/clima")
def clima(lat: float = Query(...), lon: float = Query(...), cultura: str = Query("geral")):
    weather_data = get_weather(lat, lon)
    alerts = generate_alerts(weather_data)
    forecast = format_forecast(weather_data)

    cached = load_cache()
    if cached:
        weather_data = cached
    else:
        weather_data = get_weather(lat, lon)
        save_cache(weather_data)


    current = weather_data.get("current_weather", {})
    score = calculate_score(weather_data, cultura)
    return {
        "latitude": lat,
        "longitude": lon,
        "cultura": cultura,
        "temperatura_atual": current.get("temperature"),
        "vento_kmh": current.get("windspeed"),
        "alertas": alerts,
        "score_climatico": score,
        "previsao_proximas_horas": forecast
    }
