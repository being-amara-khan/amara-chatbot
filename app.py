import streamlit as st
import time
import random

# Set page config
st.set_page_config(
    page_title="Amara's AI Assistant",
    page_icon="👩‍💻",
    layout="centered"
)

# Custom CSS for better UI
st.markdown("""
<style>
    .stTextInput>div>div>input {
        border-radius: 20px;
    }
    .chat-message {
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        flex-direction: column;
    }
    .chat-message.user {
        background-color: #2b313e;
    }
    .chat-message.assistant {
        background-color: #475063;
    }
    .chat-message .avatar {
        width: 20px;
        height: 20px;
        border-radius: 50%;
        margin-right: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Simple responses for the chatbot
RESPONSES = {
    "hello": "Hi there! 👋 How can I help you today?",
    "how are you": "I'm doing great, thanks for asking! How about you? 😊",
    "bye": "Goodbye! Have a wonderful day! 👋",
    "thanks": "You're welcome! Is there anything else I can help you with? 😊",
    "default": "I'm Amara's AI assistant! I'm still learning, but I'm here to help. Could you rephrase that? 🤔"
}

def get_response(user_input):
    """Get a response based on user input"""
    user_input = user_input.lower()
    
    # Check for matching keywords
    for key in RESPONSES:
        if key in user_input:
            return RESPONSES[key]
    
    return RESPONSES["default"]

def simulate_typing(text):
    """Simulate typing effect"""
    message_placeholder = st.empty()
    full_response = ""
    
    for chunk in text.split():
        full_response += chunk + " "
        time.sleep(0.1)
        message_placeholder.markdown(full_response + "▌")
    
    message_placeholder.markdown(full_response)

# App title and description
st.title("👩‍💻 Amara's AI Assistant")
st.markdown("Hi! I'm your AI assistant powered by Amara Khan's logic. How can I help you today?")

# Display chat history
for message in st.session_state.messages:
    with st.container():
        st.markdown(f"""
        <div class="chat-message {message['role']}">
            <div style="display: flex; align-items: center;">
                <span class="avatar">{"👤" if message['role'] == 'user' else "👩‍💻"}</span>
                <strong>{message['role'].title()}</strong>
            </div>
            <div>{message['content']}</div>
        </div>
        """, unsafe_allow_html=True)

# Chat input
user_input = st.text_input("Type your message here...", key="user_input")

if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Get and display assistant response
    response = get_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Rerun to update chat history
    st.experimental_rerun() 