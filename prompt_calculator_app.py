import re
import streamlit as st

# 🎨 App title
st.title("🧮 Prompt-Based Calculator")
st.write("Type your math in plain English — no symbols needed!")

# 🧾 Get user input
user_input = st.text_input("Example: 'Add 12 and 9' or 'Divide 20 by 5'")

def prompt_calculator(prompt):
    prompt = prompt.lower()
    numbers = [int(num) for num in re.findall(r'\d+', prompt)]

    if len(numbers) < 2:
        return "⚠️ Please give me two numbers to work with!"

    # Identify operation
    if "add" in prompt or "plus" in prompt or "sum" in prompt:
        return f"The answer is {numbers[0] + numbers[1]}"
    elif "subtract" in prompt or "minus" in prompt or "difference" in prompt:
        return f"The answer is {numbers[0] - numbers[1]}"
    elif "multiply" in prompt or "times" in prompt or "product" in prompt:
        return f"The answer is {numbers[0] * numbers[1]}"
    elif "divide" in prompt or "by" in prompt or "over" in prompt:
        if numbers[1] == 0:
            return "❌ Can't divide by zero!"
        return f"The answer is {numbers[0] / numbers[1]}"
    else:
        return "🤔 Sorry, I don't understand that math operation."

# 🧮 Display result
if user_input:
    result = prompt_calculator(user_input)
    st.success(result)

# 👇 Add footer for LinkedIn
st.markdown("---")
st.caption("Built by [Your Name] | Prompt Engineer Mini Project #1")
