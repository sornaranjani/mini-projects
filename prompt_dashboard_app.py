import streamlit as st
import pandas as pd
import os
from datetime import datetime

FILE_NAME = "prompt_history.csv"

# Load prompt history
def load_history():
    if os.path.exists(FILE_NAME):
        return pd.read_csv(FILE_NAME)
    else:
        return pd.DataFrame(columns=["Date", "Prompt", "Category", "Score"])

# Save prompt history
def save_history(df):
    df.to_csv(FILE_NAME, index=False)

st.title("📊 Prompt History Tracker / Dashboard")
st.write("Track all your prompts, categories, and scores — offline, no API needed!")

# Load existing history
history = load_history()

# Input new prompt
st.subheader("Add a New Prompt")
prompt_text = st.text_area("Prompt text:")
category = st.selectbox("Category:", ["General", "Educational", "Creative", "Coding", "Summarization", "Analytical"])
score = st.slider("Optional Score (0-10):", 0, 10, 5)

if st.button("Add Prompt"):
    if prompt_text.strip():
        new_entry = pd.DataFrame([[datetime.now().strftime("%Y-%m-%d %H:%M:%S"), prompt_text.strip(), category, score]],
                                 columns=["Date", "Prompt", "Category", "Score"])
        history = pd.concat([history, new_entry], ignore_index=True)
        save_history(history)
        st.success("✅ Prompt added to history!")
    else:
        st.warning("Please enter a prompt.")

# Show dashboard
st.subheader("📋 Prompt Dashboard")
if not history.empty:
    st.dataframe(history)
else:
    st.info("No prompts saved yet.")

# Optional: filter by category
st.subheader("Filter by Category")
selected_category = st.selectbox("Choose category:", ["All"] + history["Category"].unique().tolist())
if selected_category != "All":
    st.dataframe(history[history["Category"] == selected_category])

st.markdown("---")
st.caption("Built by [Your Name] | Prompt Engineer Mini Project #10")
