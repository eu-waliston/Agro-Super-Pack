# CORE da API ( geração de alertas )
def generate_alerts(weather_data):
    alerts = []

    current = weather_data.get("current_weather", {})
    hourly = weather_data.get("hourly", {})

    temp = current.get("temperature")
    wind_speed = current.get("windspeed")

    # regra geada
    if temp is not None and temp <= 4:
        alerts.append("🚨 Risco de geada nas próximas horas.")

    if wind_speed is not None and wind_speed > 15:
        alerts.append("❌ Vento forte. Evitar pulverização.")

    # regra chuvas nas proximas horas
    precipitation = hourly.get("precipitations", [])

    if any(p > 0 for p in precipitation[:6]): #Proximas horas
        alerts.append("❌ Chuva prevista. Evitar pulverização.")

    if not alerts:
        alerts.append("✅ Condições climáticas estáveis.")

    return alerts

# função de SCORE ( transforma clima em número simples. )
def calculate_score(weather_data, cultura="geral"):
    score = 100

    current = weather_data.get("current_weather", {})
    hourly = weather_data.get("hourly", {})

    temp = current.get("temperature")
    wind = current.get("windspeed")
    precipitation = hourly.get("precipitation", [])


    if cultura == "milho":
        if temp is not None:
            if temp < 10:
                score -= 25

            if temp > 32:
                score -= 20

    elif cultura == "soja":
        if temp is not None:
            if temp < 12:
                score -= 20

            if temp > 35:
                score -= 15

    if temp is not None:
        if temp <= 4:
            score -= 5
        if temp > 35:
            score -= 15

    if wind is not None and wind > 15:
        score -= 20

    if any(p > 0 for p in precipitation[:6]):
        score -= 25

    return max(score, 0)