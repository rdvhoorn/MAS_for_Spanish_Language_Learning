import streamlit as st
from dotenv import load_dotenv

from src.mas.system import get_system_response

load_dotenv()

# Initial system message
INIT_MESSAGE = {
    "role": "system",
    "content": "👋 Hey! What do you want to learn today?"
}

# Session state setup
if "chat" not in st.session_state:
    st.session_state.chat = [INIT_MESSAGE]
if "awaiting_user" not in st.session_state:
    st.session_state.awaiting_user = True
if "agent_logic_active" not in st.session_state:
    st.session_state.agent_logic_active = False


st.title("🗣️ Spanish Language Assistant")

# Chat display
for msg in st.session_state.chat:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input for user
if st.session_state.awaiting_user:
    user_input = st.chat_input("Type your message here...")
    if user_input:
        # Add user's message
        st.session_state.chat.append({"role": "user", "content": user_input})
        st.session_state.awaiting_user = False
        st.session_state.agent_logic_active = True
        st.rerun()

# Simulated agent response (replace this block with your agent logic)
if st.session_state.agent_logic_active:
    user_message = st.session_state.chat[-1]["content"]

    # 🔁 Your agent chain should process `user_msg` and return:
    # - response text
    # - goto: 'user' or next agent
    # For now, simulate:
    agent_response, history = get_system_response(user_message)

    # Append agent message
    st.session_state.chat.append({"role": "assistant", "content": agent_response})
    
    st.session_state.awaiting_user = True
    st.session_state.agent_logic_active = False

    st.rerun()