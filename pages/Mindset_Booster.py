import streamlit as st
import random

# Motivational Quotes List
quotes = [
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Your only limit is your mind.",
    "Don’t let yesterday take up too much of today.",
    "Mistakes are proof that you are trying.",
    "A journey of a thousand miles begins with a single step."
]

# Growth Mindset Advice List
advice_list = [
    "Try something new today!",
    "Don't fear failure, learn from it!",
    "Take a break and reflect on your progress.",
    "Talk to someone who inspires you.",
    "Set a small goal and achieve it today!"
]

# App Title
st.title("🌱 Growth Mindset Booster")

# Motivational Quotes Section
st.header("🌟 Daily Motivation")
st.write("Start your day with an inspiring thought!")
if st.button("Get a Motivational Quote"):
    st.success(random.choice(quotes))

# Spinning Advice Wheel Section
st.header("🎡 Growth Mindset Advice Wheel")
st.write("Click the button to receive a random piece of advice!")
if st.button("Spin the Wheel"):
    st.info(random.choice(advice_list))