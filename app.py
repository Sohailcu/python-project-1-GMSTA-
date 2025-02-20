import streamlit as st
import pandas as pd
import tempfile
import os
import base64
from pdf2docx import Converter
from docx2pdf import convert
from fpdf import FPDF
from docx import Document
import datetime

# 🌱 Growth Mindset Introduction
st.title("🚀 Growth Mindset App")

# Sidebar Navigation
st.sidebar.title("🔍 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Mindset Quiz", "File Converter", "To-Do List", "Daily Challenges", "Progress Tracker", "Resource Library"])

if page == "Home":
    st.write("""
    ## 🌱 What is a Growth Mindset?  
    A **growth mindset** is the belief that intelligence, talents, and abilities **can be developed** through dedication, learning, and persistence.  
    People with a growth mindset **embrace challenges, learn from failures, and continuously improve** their skills.  

    On the other hand, a **fixed mindset** makes people believe that intelligence and talent are **static** – meaning, they can’t be changed.  

    ### 🔥 Why is a Growth Mindset Important?  
    Having a growth mindset can transform your life. It helps you:  
    ✅ **Embrace challenges** instead of avoiding them  
    ✅ **Learn from criticism** rather than feeling discouraged  
    ✅ **Keep going despite failures** instead of giving up  
    ✅ **See effort as the key to success**  
    ✅ **Develop resilience** and overcome difficulties  

    ---

    ## 🔄 **Fixed Mindset vs. Growth Mindset**  
    Here’s a quick comparison to understand the difference:  

    | 🔴 **Fixed Mindset**  | 🟢 **Growth Mindset**  |
    |----------------------|----------------------|
    | "I am either smart or not." | "I can get smarter by learning!" |
    | "I avoid challenges." | "I love challenges!" |
    | "I give up easily." | "I keep trying until I succeed!" |
    | "Failure means I’m not good enough." | "Failure helps me improve!" |
    | "Effort is useless if I’m not talented." | "Effort makes me stronger!" |

    ---

    ## 🚀 **How Can You Develop a Growth Mindset?**  
    Here are **some powerful strategies** to develop a growth mindset:  

    ### 1️⃣ **Change the Way You Think About Failure**  
    ❌ Instead of: "I failed, I’m not good enough."  
    ✅ Try: "I failed, but I learned something valuable!"  

    ### 2️⃣ **Believe in Continuous Learning**  
    🧠 Intelligence is not fixed; the brain can rewire itself with learning.  
    🎯 Learn new skills, read books, and challenge yourself daily.  

    ### 3️⃣ **Turn Challenges into Opportunities**  
    🔹 Every challenge is a chance to **learn and grow.**  
    🔹 Instead of **avoiding difficulties**, embrace them as learning experiences.  

    ### 4️⃣ **Surround Yourself with Positive & Growth-Oriented People**  
    💡 Being around people who **encourage learning** and **support self-improvement** can boost your mindset.  

    ### 5️⃣ **Take Action – Apply What You Learn!**  
    🚀 Learning is great, but **real growth happens when you apply it.**  
    ✅ Take small steps every day towards self-improvement.  

    ---

    ## 📌 **How This App Helps You?**  
    This app is designed to help you **understand, test, and apply** a growth mindset in daily life through interactive tools:  

    🧠 **Mindset Quiz** – Find out how much of a growth mindset you have!  
    📂 **File Converter** – Boost productivity with easy file conversions  
    📋 **To-Do List** – Stay organized and focused  
    🎯 **Daily Challenges** – Get daily tasks to foster a growth mindset  
    📊 **Progress Tracker** – Monitor your growth over time  
    📚 **Resource Library** – Access curated resources for continuous learning  

    ### **💡 Ready to Develop Your Growth Mindset?**  
    👉 Explore the tools below and start your journey today! 🚀🔥  

    ---
    """)

elif page == "Mindset Quiz":
    st.title("🧠 Mindset Quiz")
    st.write("Answer the following questions to find out how much of a growth mindset you have!")

    questions = [
        "I believe intelligence can be developed.",
        "I enjoy challenges and see them as opportunities to grow.",
        "I learn from criticism and feedback.",
        "I persist in the face of setbacks.",
        "I believe effort is the key to success."
    ]

    answers = []
    for i, question in enumerate(questions):
        answer = st.radio(f"{i+1}. {question}", ("Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"))
        answers.append(answer)

    if st.button("Submit"):
        score = 0
        for answer in answers:
            if answer == "Strongly Disagree":
                score += 1
            elif answer == "Disagree":
                score += 2
            elif answer == "Neutral":
                score += 3
            elif answer == "Agree":
                score += 4
            elif answer == "Strongly Agree":
                score += 5

        st.write(f"Your Growth Mindset Score: {score}/25")
        if score >= 20:
            st.success("You have a strong growth mindset! Keep up the great work!")
        elif score >= 15:
            st.warning("You have a moderate growth mindset. There's room for improvement!")
        else:
            st.error("You may have a fixed mindset. Consider adopting more growth-oriented beliefs!")

elif page == "File Converter":
    st.title("📂 File Converter")
    st.write("Upload a file to convert it to another format.")

    uploaded_file = st.file_uploader("Choose a file", type=["txt", "pdf", "docx", "jpg", "png"])
    if uploaded_file is not None:
        file_details = {"filename": uploaded_file.name, "filetype": uploaded_file.type, "filesize": uploaded_file.size}
        st.write(file_details)

        if uploaded_file.type == "text/plain":
            st.write("Converting .txt to .pdf")
            # Add conversion logic here
        elif uploaded_file.type == "application/pdf":
            st.write("Converting .pdf to .docx")
            # Add conversion logic here
        elif uploaded_file.type == "image/jpeg" or uploaded_file.type == "image/png":
            st.write("Converting image to .pdf")
            # Add conversion logic here

elif page == "To-Do List":
    st.title("📋 To-Do List")
    st.write("Stay organized and focused with your tasks.")

    if 'tasks' not in st.session_state:
        st.session_state.tasks = []

    task = st.text_input("Add a new task")
    if st.button("Add Task"):
        if task:
            st.session_state.tasks.append({"task": task, "completed": False})
            st.success("Task added!")

    for i, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([4, 1])
        with col1:
            st.checkbox(f"{i+1}. {task['task']}", value=task['completed'], key=f"task_{i}")
        with col2:
            if st.button(f"Delete {i+1}"):
                del st.session_state.tasks[i]
                st.experimental_rerun()

elif page == "Daily Challenges":
    st.title("🎯 Daily Challenges")
    st.write("Here’s your daily challenge to foster a growth mindset:")

    challenges = [
        "Learn something new today and share it with a friend.",
        "Take on a task you’ve been avoiding and see it through.",
        "Reflect on a recent failure and write down what you learned.",
        "Ask for feedback on a project and use it to improve.",
        "Spend 30 minutes reading a book or article on a topic you’re curious about."
    ]

    challenge = st.selectbox("Today's Challenge", challenges)
    st.write(f"**Your Challenge:** {challenge}")

    if st.button("Complete Challenge"):
        st.success("Great job! You’re one step closer to developing a growth mindset!")

elif page == "Progress Tracker":
    st.title("📊 Progress Tracker")
    st.write("Track your personal growth over time.")

    if 'progress' not in st.session_state:
        st.session_state.progress = []

    date = st.date_input("Date", datetime.date.today())
    progress = st.text_area("What progress did you make today?")
    if st.button("Add Progress"):
        if progress:
            st.session_state.progress.append({"date": date, "progress": progress})
            st.success("Progress added!")

    for entry in st.session_state.progress:
        st.write(f"**{entry['date']}:** {entry['progress']}")

elif page == "Resource Library":
    st.title("📚 Resource Library")
    st.write("Explore curated resources to foster a growth mindset.")

    resources = {
        "Books": [
            "Mindset: The New Psychology of Success by Carol S. Dweck",
            "Grit: The Power of Passion and Perseverance by Angela Duckworth",
            "The Power of Now by Eckhart Tolle"
        ],
        "Articles": [
            "The Science of Growth Mindset",
            "How to Develop a Growth Mindset",
            "The Benefits of a Growth Mindset"
        ],
        "Videos": [
            "The Power of Believing That You Can Improve - Carol Dweck (TED Talk)",
            "Growth Mindset vs. Fixed Mindset",
            "How to Develop a Growth Mindset"
        ]
    }

    for category, items in resources.items():
        st.subheader(category)
        for item in items:
            st.write(f"- {item}")