import requests
import streamlit as st

# FastAPI server URL
API_URL = "http://127.0.0.1:8000/predict/"

# Title for the web app
st.title("🤖 Your Virtual Assistant")

# Add custom CSS for chatbot styling
st.markdown(
    """
    <style>
    .chat-window {
        position: fixed;
        bottom: 16px;
        right: 16px;
        background-color: #fff;
        border: 1px solid #e5e7eb;
        border-radius: 16px;
        width: 440px;
        height: 634px;
        display: flex;
        flex-direction: column;
        box-shadow: 0 1px 4px rgba(0, 0, 0, 0.1);
        padding: 16px;
        animation: slideIn 0.5s ease-out;
    }
    @keyframes slideIn {
        from {
            transform: translateY(100%);
        }
        to {
            transform: translateY(0);
        }
    }
    .chat-header {
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 8px;
        display: flex;
        align-items: center;
    }
    .chat-header img {
        vertical-align: middle;
        margin-right: 8px;
        height: 30px;
        width: 30px;
    }
    .chat-subheader {
        font-size: 12px;
        color: #776b80;
        margin-bottom: 16px;
    }
    .chat-messages {
        flex: 1;
        overflow-y: auto;
        margin-bottom: 16px;
        display: flex;
        flex-direction: column;
        gap: 10px;
    }
    .chat-message.user {
        text-align: right;
        background-color: #aa78cf;
        padding: 10px;
        border-radius: 16px 0 16px 16px;
        max-width: 60%;
        margin-left: auto;
        margin-bottom: 10px;
        margin-top: 10px;
        color: #12412e;
    }
    .chat-message.bot {
        text-align: left;
        background-color: #0bc6e3;
        color: white;
        padding: 10px;
        border-radius: 0 16px 16px 16px;
        max-width: 60%;
    }
    .chat-input-container {
        display: flex;
        gap: 8px;
    }
    .chat-input {
        flex: 1;
        padding: 10px;
        border-radius: 8px;
        border: 1px solid #ccc;
    }
    .chat-send-button {
        background-color: #0078D7;
        color: white;
        border-radius: 8px;
        padding: 10px 20px;
        border: none;
        font-size: 14px;
        font-weight: bold;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .chat-send-button:hover {
        background-color: #005bb5;
    }
    .clear-button {
        background-color: #f44336;
        color: white;
        border-radius: 8px;
        padding: 8px 16px;
        border: none;
        font-size: 12px;
        cursor: pointer;
    }
    .clear-button:hover {
        background-color: #d32f2f;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Session state to store conversation history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Chat window structure
st.markdown('<div class="chat-window">', unsafe_allow_html=True)

st.markdown(
    '''
    <div class="chat-header">
        <img src="data:image/png;base64,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" alt="Chatbot Logo">
        Chatbot
    </div>
    ''',
    unsafe_allow_html=True,
)
st.markdown('<div class="chat-subheader">Powered by AI Intent Prediction Bot</div>', unsafe_allow_html=True)
st.markdown('<div class="chat-messages">', unsafe_allow_html=True)

# Display chat history
for message in st.session_state["messages"]:
    if message["user"]:
        st.markdown(f'<div class="chat-message user">{message["user"]}</div>', unsafe_allow_html=True)
    if message["bot"]:
        st.markdown(f'<div class="chat-message bot">{message["bot"]}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # End of chat-messages div

# Chat input and send button
with st.form(key='chat_form', clear_on_submit=True):
    user_input = st.text_input(
        "", key="user_input", placeholder="Ask me anything about banking...", label_visibility="collapsed"
    )
    submit_button = st.form_submit_button("Send")

# Clear chat history button
if st.button("Clear Chat", key="clear"):
    st.session_state["messages"] = []
    st.rerun()

# Process the user's message
if submit_button and user_input:
    # Append user message
    st.session_state["messages"].append({"user": user_input, "bot": ""})

    # Send request to API
    response = requests.post(API_URL, json={"text": user_input})
    if response.status_code == 200:
        prediction = response.json()
        bot_reply = (
            f"Intent: {prediction['prediction']}<br>"
            f"Confidence: {prediction['confidence']:.2f}%"
        )
    else:
        bot_reply = "Error: Unable to process the request. Try again later."

    # Append bot reply
    st.session_state["messages"][-1]["bot"] = bot_reply
    st.rerun()  # Refresh the chat window

st.markdown('</div>', unsafe_allow_html=True)  # End of chat-window 