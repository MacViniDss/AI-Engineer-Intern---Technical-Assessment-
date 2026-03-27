# Interactive Global Weather App

## Overview
A full-stack Python application that allows users to check the current weather for any location around the globe. Users can search by ZIP code, city name, or landmarks, or use an interactive map to pinpoint exact GPS coordinates. The app features a robust FastAPI backend and a highly interactive Streamlit frontend.

<p align="center">
  <img src="https://github.com/MacViniDss/AI-Engineer-Intern---Technical-Assessment-/blob/main/weather_service/output/weather_info.png" width="45%" />
  <img src="https://github.com/MacViniDss/AI-Engineer-Intern---Technical-Assessment-/blob/main/weather_service/output interative_map.png" width="45%" />
</p>

## Features
* **Text Search:** Find weather data using city names, ZIP codes, or landmarks.
* **Interactive Map Pop-up:** Click anywhere on an embedded Folium map to fetch weather data for specific coordinates.
* **Real-time Data:** Pulls live weather metrics (temperature, humidity, wind speed, conditions) using the OpenWeatherMap API.
* **Data Export:** Download the fetched weather reports locally in JSON or Markdown formats.

## Tech Stack
* **Backend:** FastAPI, Uvicorn, Python's requests
* **Frontend:** Streamlit, Folium, Streamlit-folium
* **External API:** OpenWeatherMap

## Prerequisites
* Python 3.8+
* An API key from [OpenWeatherMap](https://openweathermap.org/api)

## Installation & Setup

**1. Clone the repository (or create the project folder)**
```bash 
git clone <your-repo-url>
cd weather_app
```
**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up Environment Variables**
Create a .env file in the root directory and add your API key and backend URL:
```bash
OPENWEATHERMAP_API_KEY=your_actual_api_key_here
FASTAPI_URL=http://localhost:8000
```
## Running the Application

This project requires running the backend and frontend simultaneously in separate terminal windows.

### Terminal 1: Start the FastAPI Backend
```bash
uvicorn backend.main:app --reload
```
The API will be available at http://localhost:8000

### Terminal 2: Start the Streamlit Frontend
```bash
streamlit run frontend/app.py
``` 
The web interface will automatically open in your default browser at http://localhost:8501
