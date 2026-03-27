import streamlit as st
import folium
from streamlit_folium import st_folium
import requests
import os
from dotenv import load_dotenv

# Import our custom export functions
from export_service import export_json, export_markdown

# Load environment variables
load_dotenv()
API_URL = os.getenv("FASTAPI_URL", "http://localhost:8000")

st.set_page_config(page_title="Global Weather App", layout="wide")
st.title("Interactive Weather App")

# Initialize session state so data persists between reruns
if "weather_data" not in st.session_state:
    st.session_state.weather_data = None

def fetch_weather(endpoint: str, params: dict):
    """Helper function to call the FastAPI backend."""
    try:
        response = requests.get(f"{API_URL}{endpoint}", params=params)
        if response.status_code == 200:
            st.session_state.weather_data = response.json()
        else:
            st.error(f"Error: {response.json().get('detail', 'Location not found')}")
    except Exception as e:
        st.error(f"Failed to connect to backend: {e}")

# Create a true pop-up dialog for the map
@st.dialog("Select Location on Map", width="large")
def map_dialog():
    st.markdown("Click anywhere on the map to drop a pin and get coordinates.")
    
    # Initialize Folium map
    m = folium.Map(location=[20.0, 0.0], zoom_start=2)
    m.add_child(folium.LatLngPopup()) # Enables clicking to get coordinates
    
    # Render interactive map inside Streamlit
    map_data = st_folium(m, height=400, width=600)
    
    if map_data and map_data.get("last_clicked"):
        lat = map_data["last_clicked"]["lat"]
        lon = map_data["last_clicked"]["lng"]
        st.success(f"Selected Coordinates: Latitude {lat:.4f}, Longitude {lon:.4f}")
        
        if st.button("Get Weather for this location", type="primary"):
            fetch_weather("/weather/coords", {"lat": lat, "lon": lon})
            st.rerun() # Closes dialog and updates main UI

# --- MAIN UI ---

st.write("Enter a location or select one from the interactive map to check the current weather.")

# Text Search
query = st.text_input("Enter Zip Code, City, or Landmark:", placeholder="e.g., Tokyo, JP or 10001")

col1, col2 = st.columns(2)
with col1:
    if st.button("Search via Text", use_container_width=True):
        if query:
            fetch_weather("/weather/search", {"query": query})
        else:
            st.warning("Please enter a location.")
            
with col2:
    if st.button("Open Interactive Map", use_container_width=True):
        map_dialog()

# --- WEATHER DISPLAY & EXPORT ---
if st.session_state.weather_data:
    data = st.session_state.weather_data
    st.markdown("---")
    st.subheader(f"Weather in {data.get('name', 'Unknown Location')}, {data.get('sys', {}).get('country', '')}")
    
    # Display primary metrics cleanly
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Temperature", f"{data['main']['temp']} °C")
    c2.metric("Condition", data['weather'][0]['description'].title())
    c3.metric("Humidity", f"{data['main']['humidity']}%")
    c4.metric("Wind Speed", f"{data['wind']['speed']} m/s")

    st.markdown("###Export Data")
    st.write("Save this report in your preferred format.")
    
    # Generate export files
    json_data = export_json(data)
    md_data = export_markdown(data)

    # Download Buttons
    e1, e2, e3 = st.columns(3)
    e1.download_button("Download JSON", data=json_data, file_name="weather.json", mime="application/json")
    e2.download_button("Download Markdown", data=md_data, file_name="weather.md", mime="text/markdown")
