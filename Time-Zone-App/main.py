import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "America/Los_Angeles",
    "Europe/London",
    "Europe/Berlin",
    "Asia/Tokyo",
    "Australia/Sydney",
    "Asia/Kolkata",
    "Asia/Dubai",
]

st.title("Time Zone App")

selected_timezone = st.multiselect("Select a time zone:", TIME_ZONES, default=["UTC","Asia/Karachi"])

st.subheader("Current Time in Selected Time Zones")
for tz in selected_timezone:
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S")

    st.write(f"**{tz}**: {current_time}")

st.subheader("Converter Time Between Time Zones")

current_time = st.time_input("Current Time", value=datetime.now().time())

from_tz = st.selectbox("From Time Zone", TIME_ZONES, index=0)
to_tz = st.selectbox("To Time Zone", TIME_ZONES, index=1)

if st.button("Convert Time"):
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S")

    st.success(f"Converted Time from **{from_tz}** to **{to_tz}**: {converted_time}")