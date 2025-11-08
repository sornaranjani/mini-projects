import streamlit as st

st.title("🧩 Prompt Pattern Tester")
st.write("Test how your prompt templates look with different texts — no API key needed!")

template = st.text_input("Enter your prompt pattern:", "Summarize this in one line: {text}")
text = st.text_area("Enter sample text:", "Artificial intelligence helps computers learn like humans.")

if st.button("Generate Prompt"):
    result = template.replace("{text}", text)
    st.success(result)

st.markdown("---")
st.caption("Built by [Your Name] | Prompt Engineer Mini Project #3")
