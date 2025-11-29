import streamlit as st

st.title("Simple Streamlit App")

user_input = st.text_input("Enter your text:")

if st.button("Show text"):
    st.write("You entered: " + user_input)