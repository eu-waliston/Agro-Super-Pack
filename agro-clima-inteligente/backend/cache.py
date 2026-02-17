import json
import os
import time

CACHE_FILE = "weather_cache.json"
CACHE_TTL = 1000 #30 minutos

def save_cache(data):
    payload = {
        "timestamp": time.time(),
        "data": data
    }

    with open(CACHE_FILE, "w") as f:
        json.dump(payload, f)

def load_cache():
    if not os.path.exists(CACHE_FILE):
        return None

    with open(CACHE_FILE, "r") as f:
        payload = json.load(f)

    if time.time() - payload["timestamp"] < CACHE_TTL:
        return payload["data"]

    return None