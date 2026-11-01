
import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(
    page_title="GenZ AI",
    page_icon="💬",
    layout="centered"
)

st.title("💬 GenZ AI")
st.caption("Your AI-powered internet companion ✨")

SYSTEM_PROMPT = """
You are GenZ AI, a smart, funny and friendly chatbot.

Your personality:
- Talk naturally and casually.
- Use Gen Z slang occasionally.
- Be witty and funny when appropriate.
- Give meaningful and relevant answers.
- Never give random or unrelated replies.
- Remember the conversation context.
- Explain difficult topics simply.
- Be helpful, respectful and engaging.
"""

try:
    api_key = st.secrets["GEMINI_API_KEY"]
    client = genai.Client(api_key=api_key)
except Exception:
    st.error("API key setup issue. Please check Streamlit Secrets.")
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

if st.button("🗑️ Clear conversation"):
    st.session_state.messages = []
    st.rerun()

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Ask me anything...")

if prompt:
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        history = []

        for msg in st.session_state.messages[:-1]:
            role = "user" if msg["role"] == "user" else "model"

            history.append(
                types.Content(
                    role=role,
                    parts=[types.Part(text=msg["content"])]
                )
            )

        chat = client.chats.create(
            model="gemini-3.8-flash",
            history=history,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT
            )
        )

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = chat.send_message(prompt)
                answer = response.text or "I couldn't generate a reply."
                st.markdown(answer)

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )

    except Exception:
        st.error(
            "Couldn't generate a reply. Check your API key, "
            "model availability and usage limits."
        )
