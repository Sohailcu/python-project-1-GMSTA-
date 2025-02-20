import streamlit as st

# Page Title
st.title("🧠 Mindset Growth Quiz")

# Introduction
st.markdown("""
Welcome to the **Mindset Growth Quiz!** 🚀  
This quiz will help you understand your mindset and provide insights on areas for improvement.  
Choose the best option for each question. Let's get started! 🎯
""")

# Questions and Answers
questions = [
    {
        "question": "What is a **Growth Mindset**?",
        "options": [
            "Believing that abilities and intelligence can develop over time.",
            "Thinking intelligence is fixed and cannot change.",
            "Avoiding challenges to prevent failure.",
            "Success depends only on talent, not effort."
        ],
        "answer": "Believing that abilities and intelligence can develop over time."
    },
    {
        "question": "When faced with a difficult challenge, a person with a growth mindset will:",
        "options": [
            "Give up quickly.",
            "Look for new strategies and keep trying.",
            "Avoid the challenge altogether.",
            "Blame others for the difficulty."
        ],
        "answer": "Look for new strategies and keep trying."
    },
    {
        "question": "Which statement aligns with a **Fixed Mindset**?",
        "options": [
            "Mistakes help me learn and improve.",
            "I am either naturally good at something or not.",
            "With effort, I can master any skill.",
            "Failure is a part of learning."
        ],
        "answer": "I am either naturally good at something or not."
    },
    {
        "question": "How should you respond to constructive criticism?",
        "options": [
            "Ignore it because I know best.",
            "Feel discouraged and stop trying.",
            "Use it as feedback to improve and grow.",
            "Take it personally and get upset."
        ],
        "answer": "Use it as feedback to improve and grow."
    },
    {
        "question": "What is a key characteristic of someone with a **growth mindset**?",
        "options": [
            "Avoids feedback and criticism.",
            "Seeks challenges and enjoys learning.",
            "Only does things they are already good at.",
            "Believes success comes without effort."
        ],
        "answer": "Seeks challenges and enjoys learning."
    },
    {
        "question": "Which statement reflects **a positive attitude toward failure**?",
        "options": [
            "Failure is proof that I am not good enough.",
            "Failure means I should give up.",
            "Failure is an opportunity to learn and improve.",
            "I should avoid failure at all costs."
        ],
        "answer": "Failure is an opportunity to learn and improve."
    },
    {
        "question": "How do people with a **growth mindset** view effort?",
        "options": [
            "Effort is useless if you're not naturally talented.",
            "Effort is the path to mastery and success.",
            "Only weak people need to put in effort.",
            "Talent is all that matters; effort is secondary."
        ],
        "answer": "Effort is the path to mastery and success."
    },
    {
        "question": "A growth mindset helps in:",
        "options": [
            "Improving skills through continuous learning.",
            "Avoiding new challenges.",
            "Only focusing on strengths and ignoring weaknesses.",
            "Believing intelligence is fixed."
        ],
        "answer": "Improving skills through continuous learning."
    },
    {
        "question": "Why is persistence important in a growth mindset?",
        "options": [
            "It helps overcome obstacles and develop skills.",
            "It doesn’t make any difference.",
            "It is only useful for naturally talented people.",
            "Only weak individuals persist in challenges."
        ],
        "answer": "It helps overcome obstacles and develop skills."
    },
    {
        "question": "What is the best way to **develop a growth mindset**?",
        "options": [
            "Avoiding failure at all costs.",
            "Seeking feedback and learning from mistakes.",
            "Only working on things I am naturally good at.",
            "Believing that talent alone determines success."
        ],
        "answer": "Seeking feedback and learning from mistakes."
    }
]

# Initialize Session State for Score
if "score" not in st.session_state:
    st.session_state.score = 0
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False

# Display Questions
user_answers = []
for idx, q in enumerate(questions):
    st.subheader(f"**Q{idx + 1}: {q['question']}**")
    answer = st.radio("", q["options"], key=f"q{idx}")
    user_answers.append({"question": q["question"], "selected": answer, "correct": q["answer"]})

# Submit Button
if st.button("✅ Submit Answers"):
    score = sum(1 for ans in user_answers if ans["selected"] == ans["correct"])
    st.session_state.score = score
    st.session_state.quiz_submitted = True

# Show Results
if st.session_state.quiz_submitted:
    st.success(f"🎉 Your Score: **{st.session_state.score} / {len(questions)}**")
    
    # Show Correct Answers
    st.subheader("📜 Correct Answers")
    for ans in user_answers:
        st.write(f"**{ans['question']}**")
        st.write(f"✅ Correct Answer: `{ans['correct']}`")
        st.write(f"📝 Your Answer: `{ans['selected']}`")
        st.markdown("---")

# Restart Quiz
if st.session_state.quiz_submitted and st.button("🔄 Try Again"):
    st.session_state.quiz_submitted = False
    st.session_state.score = 0
    st.experimental_rerun()

# Footer
st.markdown("---")
st.caption("🚀 Keep challenging yourself and keep growing! 💡")