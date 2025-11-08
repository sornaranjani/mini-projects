import streamlit as st

st.title("🗂️ Prompt Categorizer")
st.write("Detect what type of prompt this is — educational, creative, coding, etc. (no API needed!)")

def categorize_prompt(prompt):
    prompt = prompt.lower()

    if any(word in prompt for word in ["explain", "define", "describe", "what is"]):
        return "🧠 Educational / Explain"
    elif any(word in prompt for word in ["summarize", "shorten", "in one line"]):
        return "📝 Summarization"
    elif any(word in prompt for word in ["write a poem", "story", "creative", "imagine"]):
        return "🎨 Creative Writing"
    elif any(word in prompt for word in ["generate code", "python", "program", "script"]):
        return "💻 Coding / Technical"
    elif any(word in prompt for word in ["compare", "analyze", "difference", "advantages"]):
        return "📊 Analytical / Comparison"
    else:
        return "🤔 Unknown / General"

user_prompt = st.text_input("Enter your prompt:")

if st.button("Categorize"):
    if user_prompt.strip():
        result = categorize_prompt(user_prompt)
        st.success(f"**Category:** {result}")
    else:
        st.warning("Please enter a prompt to categorize.")

st.markdown("---")
st.caption("Built by [Your Name] | Prompt Engineer Mini Project #6")
