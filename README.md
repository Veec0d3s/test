## 🌤️ Weather Forecast App

This is a simple and interactive weather dashboard built with **Streamlit**, designed to display a **7-day forecast** for any city in the world. The app integrates a weather API to fetch real-time and forecasted weather data, including temperature, humidity, and descriptive conditions like sunny, rainy, or cloudy — all enhanced with **animated icons** and **weekday labeling** for an intuitive user experience.

### 🔧 Technologies Used

* **Streamlit** – for building the interactive frontend quickly and efficiently
* **Pandas** – to manage and manipulate city data from a large CSV of world cities
* **Requests** – to connect with the weather API and retrieve live data
* **Docker** – for containerizing the application and ensuring consistent deployment across environments

### 💡 Why These Technologies?

These tools were chosen to:

* Keep development lightweight and fast with Streamlit’s simplicity
* Ensure clean and scalable data handling using Pandas
* Support modern, deployable infrastructure using Docker
* Learn and practice the fundamentals of **API integration**, **containerization**, and **data visualization**

### ⚙️ Features

* Dropdown search for **all cities in the world**
* Displays full **7-day forecast**
* Animated weather icons (e.g., ☀️ 🌧️ ☁️)
* Day of the week displayed alongside forecast
* Clean, responsive UI built using Streamlit
* Runs seamlessly inside a Docker container

### 🧠 Challenges Faced

* Free APIs typically only offer 3–5 days of forecast; switching to the OpenWeather **One Call API** required using geographic coordinates (lat/lon)
* Ensuring the dropdown handled large datasets efficiently (150K+ cities)
* Mapping raw weather descriptions to accurate and animated icons
* Configuring Docker correctly for Streamlit and data file access

### 🚀 Future Improvements

* Add current weather stats with charts or icons
* Enable location detection for quicker access
* Improve UI styling with custom CSS or Streamlit themes
* Support for multiple languages and units
* Secure API key handling via environment variables

🛠️ How to Install and Run the Project
Follow the steps below to set up and run the Weather Forecast App locally using Docker:

✅ Prerequisites
Docker installed on your machine

(Optional) Git, if you want to clone the repository

🧩 1. Clone the Repository
bash
Copy code
git clone https://github.com/your-username/weather-forecast-app.git
cd weather-forecast-app
📦 2. Build the Docker Image
Make sure your terminal is in the project directory where the Dockerfile is located.

    docker build -t streamlit-weather .

▶️ 3. Run the Docker Container

    docker run -p 8501:8501 streamlit-weather

Once running, open your browser and go to:

    http://localhost:8501

📂 Folder Structure (for reference)
kotlin
Copy code
weather-forecast-app/
├── app.py
├── weather_api.py
├── worldcities_full.csv
├── requirements.txt
└── Dockerfile

📌 Notes
Make sure your worldcities_full.csv is in the correct path so Docker copies it during build.

If you’re using an API key, make sure to inject it securely (e.g., using environment variables).