import streamlit as st

st.title("🧠 Prompt Logic Quiz App")
st.write("Select the better prompt for each question and click 'Submit Quiz' at the bottom.")

# -------------------------
# Quiz Questions
# -------------------------
quiz_questions = [
    {
        "question": "Which prompt is clearer?",
        "option_a": "Explain AI.",
        "option_b": "Explain AI in simple terms for a 10-year-old.",
        "answer": "B",
        "reason": "Prompt B is specific and sets context for tone and audience."
    },
    {
        "question": "Which prompt will likely give a better code example?",
        "option_a": "Write a Python program.",
        "option_b": "Write a Python program to reverse a string with comments.",
        "answer": "B",
        "reason": "Prompt B defines the exact task, making it more effective."
    },
    {
        "question": "Which is a better prompt for summarizing text?",
        "option_a": "Summarize this.",
        "option_b": "Summarize this paragraph in one short sentence.",
        "answer": "B",
        "reason": "Prompt B gives clear instructions about length and format."
    }
]

# -------------------------
# Initialize session state
# -------------------------
if "answers" not in st.session_state:
    st.session_state.answers = [None] * len(quiz_questions)
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# -------------------------
# Display Questions
# -------------------------
for i, q in enumerate(quiz_questions):
    st.subheader(f"Question {i+1}: {q['question']}")
    st.session_state.answers[i] = st.radio(
        "Choose the better prompt:",
        ("A: " + q["option_a"], "B: " + q["option_b"]),
        index=0 if st.session_state.answers[i] is None else 0 if st.session_state.answers[i].startswith("A") else 1,
        key=f"q{i}"
    )

# -------------------------
# Submit Quiz Button
# -------------------------
if st.button("Submit Quiz") or st.session_state.submitted:
    st.session_state.submitted = True
    score = 0
    st.markdown("---")
    for i, q in enumerate(quiz_questions):
        selected = st.session_state.answers[i]
        st.write(f"**Question {i+1}: {q['question']}**")
        st.write(f"Your Answer: {selected}")
        if selected.startswith(q["answer"]):
            st.success(f"✅ Correct! {q['reason']}")
            score += 1
        else:
            st.error(f"❌ Incorrect. {q['reason']}")
    st.subheader(f"Your Final Score: {score}/{len(quiz_questions)}")
    st.caption("Built by [Your Name] | Mini Project 5: Prompt Logic Quiz App")
