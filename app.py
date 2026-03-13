import streamlit as st
from chatbot import ask_question
import os

st.set_page_config(page_title="BMSCE Chatbot", page_icon="🎓")

# Chat history
if "history" not in st.session_state:
    st.session_state.history = []

# SIDEBAR
with st.sidebar:
    st.title("BMSCE AI Assistant")

    st.markdown("### Quick Questions")

    if st.button("When was BMSCE established?"):
        answer = ask_question("When was BMSCE established?")
        st.session_state.history.append(("When was BMSCE established?", answer))

    if st.button("What courses are offered?"):
        answer = ask_question("What courses are offered?")
        st.session_state.history.append(("What courses are offered?", answer))

    if st.button("Is hostel available?"):
        answer = ask_question("Is hostel available?")
        st.session_state.history.append(("Is hostel available?", answer))

    if st.button("Library timings"):
        answer = ask_question("What are the library timings?")
        st.session_state.history.append(("What are the library timings?", answer))

    st.markdown("---")
    st.markdown("Developed for **XCEL CORP Hackathon**")

# Logo
col1, col2, col3 = st.columns([1,2,1])

with col2:
    logo_path = os.path.join(os.path.dirname(__file__), "bmscelogo.png")
    st.image(logo_path, width=250)

# Title
st.markdown(
    """
    <h1 style='text-align: center; font-size: 60px; color:#4DA3FF;'>
    BMSCE AI Chatbot
    </h1>
    """,
    unsafe_allow_html=True
)

# Chat form
with st.form("chat_form"):
    query = st.text_input("Ask a question about the college")
    submit = st.form_submit_button("Ask")

if submit and query:
    answer = ask_question(query)
    st.session_state.history.append((query, answer))

# Show chat history
for q, a in reversed(st.session_state.history):
    st.markdown(f"**You:** {q}")
    st.success(a)

# Footer
st.markdown(
    """
    <hr>
    <p style='text-align: center; font-size:14px; color:gray;'>
    Created by Ayush Godara & Aviral Singh
    </p>
    """,
    unsafe_allow_html=True
)

# Bottom label
st.markdown(
    """
    <style>
    .bottom-right {
        position: fixed;
        bottom: 10px;
        right: 15px;
        font-size: 14px;
        color: gray;
    }
    </style>

    <div class="bottom-right">
        XCEL CORP HACKATHON
    </div>
    """,
    unsafe_allow_html=True
)

# Styling
st.markdown("""
<style>
.stApp {
    background-color: #0b132b;
}

h1 {
    font-weight: 700;
}

.stButton button {
    background-color: #4DA3FF;
    color: white;
}
</style>
""", unsafe_allow_html=True)