import streamlit as st

st.title("📝 Prompt Quality Checker")
st.write("Score your prompt for clarity, completeness, and specificity — offline, no API needed!")

def score_prompt(prompt):
    prompt = prompt.strip()
    score = 5  # Start with neutral score
    tips = []

    # Check length
    if len(prompt.split()) < 5:
        score -= 2
        tips.append("Add more context or detail.")

    # Check vague words
    vague_words = ["thing", "stuff", "something"]
    if any(word in prompt.lower() for word in vague_words):
        score -= 1
        tips.append("Avoid vague words like 'thing' or 'stuff'.")

    # Check for action words
    action_words = ["explain", "generate", "summarize", "write", "create"]
    if any(word in prompt.lower() for word in action_words):
        score += 2
        tips.append("Good! Action words make your prompt clearer.")

    # Check for audience/format
    if any(word in prompt.lower() for word in ["for", "in one line", "example", "step-by-step"]):
        score += 2
        tips.append("Nice! Specifying audience or format improves clarity.")

    # Limit score between 0 and 10
    score = max(0, min(10, score))

    return score, tips

user_prompt = st.text_area("Enter your prompt:")
if st.button("Check Quality"):
    if user_prompt.strip():
        score, tips = score_prompt(user_prompt)
        st.success(f"✅ Prompt Score: {score}/10")
        if tips:
            st.markdown("💡 Suggestions:")
            for tip in tips:
                st.markdown(f"- {tip}")
    else:
        st.warning("Please enter a prompt to evaluate.")

st.markdown("---")
st.caption("Built by [Your Name] | Prompt Engineer Mini Project #9")
