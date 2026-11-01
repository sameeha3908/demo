
import streamlit as st
from google import genai
from google.genai import types

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="GenZ AI",
    page_icon="💬",
    layout="centered"
)

# ---------------- CHATBOT PERSONALITY ----------------

SYSTEM_PROMPT = """
You are GenZ AI, a smart, funny and friendly AI chatbot.

Your personality:
- Talk naturally and casually.
- Use Gen Z slang occasionally.
- Be witty and funny when appropriate.
- Give meaningful and relevant answers.
- Never give random or unrelated replies.
- Remember the conversation context.
- Explain difficult topics simply.
- Help with studies, coding, college life and everyday questions.
- Be respectful and engaging.
- Avoid sounding robotic.

Your goal is to make every conversation helpful and fun.
"""

# ---------------- TITLE ----------------

st.title("💬 GenZ AI")
st.caption("Your AI-powered internet companion ✨")

# ---------------- API CONNECTION ----------------

try:
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    st.error("API key missing! Please check Streamlit Secrets.")
    st.stop()

client = genai.Client(api_key=api_key)

# ---------------- CHAT HISTORY ----------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# Clear conversation button

if st.button("🗑️ Clear conversation"):
    st.session_state.messages = []
    st.rerun()

# Display previous messages

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------- USER INPUT ----------------

prompt = st.chat_input("Ask me anything...")

if prompt:

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    try:
        # Prepare conversation history
        history = []

        for msg in st.session_state.messages[:-1]:

            role = "user" if msg["role"] == "user" else "model"

            history.append(
                types.Content(
                    role=role,
                    parts=[
                        types.Part(text=msg["content"])
                    ]
                )
            )

        # Create Gemini chat
        chat = client.chats.create(
            model="gemini-3.8-flash",
            history=history,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT
            )
        )

        # Generate AI response
        with st.chat_message("assistant"):

            with st.spinner("GenZ AI is thinking... 💭"):

                response = chat.send_message(prompt)

                answer = response.text

                if not answer:
                    answer = "I couldn't generate a response. Try again!"

                st.markdown(answer)

        # Save AI response
        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

    except Exception as e:

        st.error("Oops! Something went wrong.")

        st.write("Error type:", type(e).__name__)
        st.write("Details:", str(e))
