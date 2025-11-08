import streamlit as st
import os

# File to store prompts
FILE_NAME = "prompt_library.txt"

# Load prompts from file
def load_prompts():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]

# Save prompts to file
def save_prompts(prompts):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        f.write("\n".join(prompts))

# Streamlit UI
st.title("📚 Prompt Library Builder")
st.write("Create and manage your personal collection of AI prompts — no API needed!")

prompts = load_prompts()

# Add a new prompt
new_prompt = st.text_area("✨ Add a new prompt:")
if st.button("Save Prompt"):
    if new_prompt.strip():
        prompts.append(new_prompt.strip())
        save_prompts(prompts)
        st.success("✅ Prompt saved!")
    else:
        st.warning("Please enter a prompt before saving.")

# Show saved prompts
st.markdown("### 📖 Your Saved Prompts:")
if prompts:
    for i, p in enumerate(prompts, start=1):
        st.markdown(f"**{i}.** {p}")
else:
    st.info("No prompts saved yet — start by adding one above!")

# Delete option
delete_index = st.number_input("Enter prompt number to delete", min_value=1, max_value=len(prompts) if prompts else 1, step=1)
if st.button("Delete Prompt"):
    if prompts:
        deleted = prompts.pop(delete_index - 1)
        save_prompts(prompts)
        st.error(f"🗑️ Deleted: {deleted}")
    else:
        st.warning("No prompts to delete!")

st.markdown("---")
st.caption("Built by [Your Name] | Prompt Engineer Mini Project #7")
