import streamlit as st
import pandas as pd
from weather_api import get_weather
from datetime import datetime

# Load world cities
@st.cache_data
def load_cities():
    df = pd.read_csv("worldcities_full.csv")
    df["display"] = df["city"] + ", " + df["country"]
    return df

cities_df = load_cities()

st.title("🌍 Weekly Weather Forecast")

# Search bar for filtering
search_query = st.text_input("🔍 Search for a city", "")

# Filter cities by query
filtered_df = cities_df[cities_df["display"].str.lower().str.contains(search_query.lower())]

# Show selectbox with filtered options
selected_city = st.selectbox("Select a city", filtered_df["display"].tolist())

# Extract city name
city = selected_city.split(",")[0].strip() if selected_city else None

# Map icons or descriptions to animations
def get_icon(desc):
    if "rain" in desc:
        return "🌧️"
    elif "cloud" in desc:
        return "☁️"
    elif "sun" in desc or "clear" in desc:
        return "☀️"
    elif "storm" in desc:
        return "⛈️"
    else:
        return "🌡️"

if city:
    weather = get_weather(city)
    if weather:
        st.subheader(f"📍 Forecast for {weather['city']}")
        for day in weather["forecast"]:
    # Convert string to datetime and get weekday
            date_obj = datetime.strptime(day["date"], "%Y-%m-%d")
            weekday = date_obj.strftime("%A")  # e.g., Monday, Tuesday
    
            # Display with weekday
            st.markdown(f"### {weekday} ({day['date']}) - {get_icon(day['description'])}")
            st.metric("Temperature", f"{day['temperature']}°C")
            st.metric("Humidity", f"{day['humidity']}%")
            st.write(f"**{day['description'].capitalize()}**")
            st.markdown("---")
    else:
        st.error("City not found or API error.")
