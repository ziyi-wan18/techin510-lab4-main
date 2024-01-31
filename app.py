import time
import datetime
import pytz
import streamlit as st

# Define a list of time zones you want to allow the user to choose from
# For simplicity, we're using a few well-known time zones, but you can expand this list
time_zones = {
    "New York": "America/New_York",
    "London": "Europe/London",
    "Tokyo": "Asia/Tokyo",
    "Sydney": "Australia/Sydney",
    "UTC": "UTC"
}

st.title("World Clock App")

# Dropdown for selecting locations with multi-select enabled
selected_zones = st.multiselect("Select up to 4 locations", list(time_zones.keys()), default=["UTC"])

placeholder = st.empty()

while True:
    with placeholder.container():
        # Display current time for each selected location
        for zone in selected_zones:
            # Convert current time to the selected time zone
            now = datetime.datetime.now(pytz.timezone(time_zones[zone]))
            # Format the time to be more readable
            time_str = now.strftime("%Y-%m-%d %H:%M:%S")
            st.metric(zone, time_str)

    # Update time every second
    time.sleep(1)
