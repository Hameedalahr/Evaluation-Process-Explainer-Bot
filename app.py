import streamlit as st
from gemini_client import get_response

st.set_page_config(
    page_title="Academic Exam Assistant",
    page_icon="🎓",
    layout="wide" # Changed to wide for better sidebar proportion
)

# --- SIDEBAR IMPLEMENTATION ---
with st.sidebar:
    st.image("https://png.pngtree.com/png-clipart/20250415/original/pngtree-graduation-cap-books-and-diploma-on-white-background-representing-education-achievement-png-image_20731920.png", width=80)
    st.title("Resource Center")
    st.markdown("---")
    
    st.subheader("Frequently Asked Questions")
    st.info("""
    - Explain internal and External Evaluation
    - Explain Grading System
    - What is Revaluation Process
    - What are Exam Rules
    """)
    
    st.subheader("⚙️ Settings")
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.caption("v1.2 | Powered by Gemini")

# --- MAIN INTERFACE ---
st.title("🎓 Academic Examination Assistant")
st.write(
    "Ask me about examination patterns, grading rules, "
    "revaluation processes, and academic regulations."
)

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am your Academic Assistant. How can I help you today?"}
    ]

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Type your question here...")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate and display response
    with st.chat_message("assistant"):
        with st.spinner("Consulting academic records..."): # Added a loading spinner
            response = get_response(user_input)
            st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})