import streamlit as st
import random
import string

def generate_password(length, use_digits, use_special_chars):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_special_chars:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))

def main():
    st.title("Password Generator")

    length = st.number_input("Password Length", min_value=4, value=12)
    use_digits = st.checkbox("Include Digits")

        
st.title("Password Generator")

length = st.slider("Select Password Length", min_value=4, max_value=32, value=12)
use_digits = st.checkbox("Include Digits")
use_special_chars = st.checkbox("Include Special Characters")

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special_chars)
    st.write(f"Generated Password: {password}")

st.write("---")

st.write("Made with ❤️ by [Musfirah Tabassum](https://github.com/Musfirah911)")


