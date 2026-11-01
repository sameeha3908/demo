
import streamlit as st
import random

# Page settings
st.set_page_config(
    page_title="Gen Z Chatbot",
    page_icon="💬",
    layout="centered"
)

# App heading
st.title("💬 Gen Z Chatbot")
st.caption("Your internet bestie, but make it AI.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chatbot responses
def chatbot_reply(user_input):

    message = user_input.lower()

    if "hello" in message or "hi" in message:
        return random.choice([
            "Heyyy! What's the tea? ☕",
            "Hiii! What's happening?",
            "Yo! How are you doing?"
        ])

    elif "how are you" in message:
        return "I'm doing amazing. Just existing in the cloud 😭"

    elif "sad" in message or "upset" in message:
        return "Aww, what's wrong? Want to talk about it? 🫶"

    elif "bored" in message:
        return "Same energy 😭 Go do something chaotic. Or tell me what's up!"

    elif "college" in message:
        return "College is basically assignments, caffeine and survival mode 💀"

    elif "love" in message:
        return "Oooo someone's got a story to tell 👀"

    elif "hackathon" in message:
        return "Time to cook something innovative! Let's build something cool 🚀"

    elif "bye" in message:
        return "Byeeee! Don't forget to touch grass 🌱"

    elif "joke" in message:
        return "Why did the programmer quit? Because they didn't get arrays! 😂"

    else:
        return random.choice([
            "Waittt, tell me more 👀",
            "That's actually interesting!",
            "No because I need more context 😭",
            "Okay, I'm listening. Spill the tea ☕",
            "Interesting plot twist!"
        ])


# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


# User input
user_input = st.chat_input("Type something...")

if user_input:

    # Display user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    # Generate chatbot reply
    reply = chatbot_reply(user_input)

    # Display bot reply
    with st.chat_message("assistant"):
        st.write(reply)

    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })


# Clear chat button
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()
