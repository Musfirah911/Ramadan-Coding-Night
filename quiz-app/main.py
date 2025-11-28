import streamlit as st
import random
import time

st.title("Quiz Application")

questions = [
    {
    "question": "What is the capital of Pakistan?",
    "option": ["Karachi", "Lahore", "Islamabad"],
    "answer": "Islamabad"
    },
    {
    "question": "What is the national language of Pakistan?",
    "option": ["Urdu", "Punjabi", "Pashto"],
    "answer": "Urdu"
    },
    
    {
    "question": "Who is the founder of Pakistan?",
    "option": ["Allama Iqbal", "Quaid-e-Azam Muhammad Ali Jinnah", "Liaquat Ali Khan"],
    "answer": "Quaid-e-Azam Muhammad Ali Jinnah"
    },
    {
    "question": "What is the national sport of Pakistan?",
    "option": ["Cricket", "Hockey", "Football"],
    "answer": "Hockey"
    },
    {
    "question": "Which city is called the City of Lights?",
    "option": ["Karachi", "Lahore", "Islamabad"],
    "answer": "Karachi"
    },
    {
    "question": "Which river is the longest in Pakistan?",
    "option": ["Jhelum River", "Chenab River", "Indus River"],
    "answer": "Indus River"
    },
    {
    "question": "What is the largest province of Pakistan by area?",
    "option": ["Punjab", "Sindh", "Balochistan"],
    "answer": "Balochistan"
    },
    {
    "question": "What is the national flower of Pakistan?",
    "option": ["Rose", "Jasmine", "Sunflower"],
    "answer": "Jasmine"
    },
    {
    "question": "Which is the highest mountain peak in Pakistan?",
    "option": ["Nanga Parbat", "K2", "Broad Peak"],
    "answer": "K2"
    },
    {
    "question": "In which year did Pakistan become a nuclear power?",
    "option": ["1998", "1996", "2001"],
    "answer": "1998"
    },
    {
    "question": "What is the official currency of Pakistan?",
    "option": ["Pakistani Rupee", "Afghani", "Taka"],
    "answer": "Pakistani Rupee"
    },
    {
    "question": "Which city is known as the heart of Pakistan?",
    "option": ["Karachi", "Lahore", "Islamabad"],
    "answer": "Lahore"
    },
    {
    "question": "Who wrote Pakistan’s national anthem?",
    "option": ["Hafeez Jalandhari", "Faiz Ahmed Faiz", "Josh Malihabadi"],
    "answer": "Hafeez Jalandhari"
    },
    {
    "question": "What is the national animal of Pakistan?",
    "option": ["Markhor", "Snow Leopard", "Chinkara"],
    "answer": "Markhor"
    },
    {
    "question": "Which sea borders Pakistan?",
    "option": ["Arabian Sea", "Red Sea", "Caspian Sea"],
    "answer": "Arabian Sea"
    },
    {
    "question": "Which city is known as the Switzerland of Pakistan?",
    "option": ["Skardu", "Swat", "Hunza"],
    "answer": "Swat"
    }
]

if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

question = st.session_state.current_question

st.subheader(question["question"])
selected_option = st.radio("Choose your answer", question["option"], key=["answer"])

if st.button("Submit Answer"):
    if selected_option == question["answer"]:
        st.success("✅Correct!")
        st.balloons()
    else:
        st.error("❌Incorrect! The correct answer is " + question["answer"])

    time.sleep(3)

    st.session_state.current_question = random.choice(questions)

    st.rerun()