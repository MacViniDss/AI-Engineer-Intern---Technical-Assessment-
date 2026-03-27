from fastapi import FastAPI, HTTPException
from weather_service import fetch_weather_by_name, fetch_weather_by_coords

app = FastAPI(title="Weather API")

@app.get("/weather/search")
def get_weather_search(query: str):
    data = fetch_weather_by_name(query)
    # Check if OpenWeatherMap returned a 200 OK status
    if data.get("cod") != 200:
        raise HTTPException(status_code=int(data.get("cod", 400)), detail=data.get("message", "Location not found"))
    return data

@app.get("/weather/coords")
def get_weather_coords(lat: float, lon: float):
    data = fetch_weather_by_coords(lat, lon)
    if data.get("cod") != 200:
        raise HTTPException(status_code=int(data.get("cod", 400)), detail=data.get("message", "Coordinates not found"))
    return data
