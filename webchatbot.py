import streamlit as st
import os
from google import genai

GEMINI_API_KEY="api-key"

st.title("Gemini AI Chatbot")
st.caption("Chatbot sederhana menggunakan Streamlit")

if ("genai_client" not in st.session_state) or (
    getattr(st.session_state, "_last_key", None) != GEMINI_API_KEY
):
    try:
        st.session_state.genai_client = genai.Client(api_key=GEMINI_API_KEY)
        st.session_state._last_key = GEMINI_API_KEY
        st.session_state.pop("chat", None)
        st.session_state.pop("messages", None)

    except Exception as e:
        st.error(f"API Key tidak valid: {e}")
        st.stop()

if "chat" not in st.session_state:
    st.session_state.chat = st.session_state.genai_client.chats.create(
        model="gemini-3-flash-preview"
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Ketik pesanmu di sini...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    try:
        with st.chat_message("assistant"):
            with st.spinner("Sedang mengetik ..."):
                response = st.session_state.chat.send_message(prompt)
                if hasattr(response, "text"):
                    answer = response.text
                else:
                    answer = str(response)
                st.markdown(answer)

    except Exception as e:
        answer = f"Terjadi error: {e}"

    st.session_state.messages.append({"role": "assistant", "content": answer})