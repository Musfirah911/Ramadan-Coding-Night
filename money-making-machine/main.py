import streamlit as st
import random
import time
import requests

st.title("Money Making Machine")

def generate_money():
    return random.randint(1, 1000)

st.subheader("Instant Cash Generator")
if st.button("Generate Money"):
    st.write("Counting your money...")
    time.sleep(1)
    amount = generate_money()
    st.success(f"You generated ${amount}!")

def fetch_side_hustles():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustles")
        if response.status_code == 200:
            hustles = response.json()
            return hustles["side_hustles"]
        else:
            return("Freelancing")
    except:
        return ("Something went wrong.")
    
st.subheader("Side Hustle Idea")
if st.button("Generate side hustle"):
    idea = fetch_side_hustles()
    st.success(idea)

def fetch_money_quote():
    try:
        response = requests.get("http://127.0.0.1:8000/money_quotes")
        if response.status_code == 200: 
            quotes = response.json()
            return quotes["money_quotes"]
        else:
            return ("Keep hustling!")
    except:
        return ("Something went wrong.")
    
st.subheader("Money Making Motivation")
if st.button("Get Motivational Quote"):
    quote = fetch_money_quote()
    st.info(quote)