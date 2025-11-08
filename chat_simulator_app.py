import streamlit as st

st.title("💬 Offline Chat Simulator")
st.write("A simple chatbot that replies using prompt rules — no API needed!")

def chat_bot(prompt):
    prompt = prompt.lower().strip()

    if "hi" in prompt or "hello" in prompt:
        return "Hello! How can I help you today?"
    elif "your name" in prompt:
        return "I'm a mini chat assistant built by Sorna!"
    elif "how are you" in prompt:
        return "I'm doing great! Thanks for asking 😊"
    elif "bye" in prompt:
        return "Goodbye! Have a wonderful day!"
    else:
        return "Hmm... I’m not sure how to answer that yet."

user_input = st.text_input("You:", placeholder="Type your message here...")

if user_input:
    response = chat_bot(user_input)
    st.chat_message("user").write(user_input)
    st.chat_message("assistant").write(response)

st.markdown("---")
st.caption("Built by [Your Name] | Prompt Engineer Mini Project #2")
