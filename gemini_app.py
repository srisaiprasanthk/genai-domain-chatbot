import streamlit as st
from google import genai

client = genai.Client(
    api_key="AIzaSyDrVB9PAdJDv8HQMOrrYWJnetUIWCoKl2I",
    http_options={"api_version": "v1"}
)

st.set_page_config(page_title="Domain AI Assistant", layout="centered")
st.title("🤖 MYY AI Assistant")

if "history" not in st.session_state:
    st.session_state.history = []

for role, message in st.session_state.history:
    with st.chat_message(role):
        st.markdown(message)

if prompt := st.chat_input("How can I help you today?"):
    st.session_state.history.append(("user", prompt))

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("Thinking..."):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            answer = response.text
            st.session_state.history.append(("assistant", answer))

            with st.chat_message("assistant"):
                st.markdown(answer)

        except Exception as e:
            st.error(f"Error: {e}")