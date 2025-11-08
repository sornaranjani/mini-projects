import streamlit as st

st.title("✨ Prompt Enhancer")
st.write("Upgrade your prompts automatically — no API needed!")

def enhance_prompt(prompt):
    prompt = prompt.strip()
    lower = prompt.lower()

    # Add improvements based on keyword detection
    if "story" in lower:
        prompt += " Include characters, emotions, and a meaningful moral at the end."
    if "explain" in lower:
        prompt += " Explain it step-by-step in simple, clear language with examples."
    if "summarize" in lower:
        prompt += " Summarize it concisely in one short, clear paragraph."
    if "generate" in lower or "code" in lower:
        prompt += " Add helpful code comments explaining each line."
    if "write" in lower and "post" in lower:
        prompt += " Make it engaging, positive, and suitable for social media."

    # General enhancement
    if not prompt.endswith("."):
        prompt += "."

    return f"💡 Enhanced Prompt:\n\n{prompt}"

user_prompt = st.text_area("Enter your prompt (e.g. 'Write story about dog'):")

if st.button("Enhance"):
    if user_prompt.strip():
        st.success(enhance_prompt(user_prompt))
    else:
        st.warning("Please type a prompt to enhance.")

st.markdown("---")
st.caption("Built by [Your Name] | Prompt Engineer Mini Project #8")
