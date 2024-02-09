import streamlit as st
import pytz
from datetime import datetime
import time
import requests  # For fetching real-time data

# List of time zones
time_zones = list(pytz.all_timezones)

# Function to convert UNIX timestamp to human-readable format
def unix_to_human(unix_time):
    return datetime.utcfromtimestamp(int(unix_time)).strftime('%Y-%m-%d %H:%M:%S')

# Main page content
def main_page():
    st.title("World Clock App")

    # Display current UNIX timestamp
    unix_timestamp = int(time.time())
    st.metric("Current UNIX Timestamp", unix_timestamp)

    # Multi-select dropdown for time zones
    selected_zones = st.multiselect("Choose up to 4 time zones", time_zones, default=["UTC"])

    # Placeholder for clocks
    clocks_container = st.empty()

    # Update clocks every second
    while True:
        with clocks_container.container():
            for zone in selected_zones:
                tz = pytz.timezone(zone)
                time_now = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
                st.metric(zone, time_now)
        time.sleep(1)

# Page for converting UNIX timestamp to human-readable time
def timestamp_converter_page():
    st.title("UNIX Timestamp Converter")
    unix_input = st.number_input("Enter UNIX Timestamp", step=1, format="%d")
    if unix_input:
        human_time = unix_to_human(unix_input)
        st.write("Human-readable Time:", human_time)

# Page for fetching and displaying real-time data (placeholder functionality)
def real_time_data_page():
    st.title("Real-time Data Fetching")

    # Placeholder for real-time finance data fetching
    st.subheader("Finance Data (Placeholder)")
    st.write("Finance data will be displayed here. Please integrate with a real finance data API.")

    # Placeholder for real-time weather data fetching
    st.subheader("Weather Data (Placeholder)")
    st.write("Weather data will be displayed here. Please integrate with a real weather data API.")

# Sidebar navigation for multipage app
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a page:", ["World Clock", "UNIX Timestamp Converter", "Real-time Data"])

if page == "World Clock":
    main_page()
elif page == "UNIX Timestamp Converter":
    timestamp_converter_page()
elif page == "Real-time Data":
    real_time_data_page()

