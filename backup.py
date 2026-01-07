import streamlit as st
from gemini_client import get_response

st.set_page_config(
    page_title="Academic Exam Assistant",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Academic Examination Assistant")
st.write(
    "This chatbot explains examination patterns, grading rules, "
    "revaluation processes, and academic regulations."
)


if "messages" not in st.session_state:
    st.session_state.messages = []


for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


user_input = st.chat_input("Ask about exams, grading, or regulations")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    response = get_response(user_input)

    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
