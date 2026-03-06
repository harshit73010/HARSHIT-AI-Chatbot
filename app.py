import streamlit as st
from openai import OpenAI
from huggingface_hub import InferenceClient

st.set_page_config(page_title="HARSHIT AI Chatbot", page_icon="🤖")

st.title("🤖 HARSHIT AI Chatbot")
st.write("Powered by Harshit 🚀")


client = InferenceClient( api_key="YOUR_HF_API_KEY_XXXXXXXXXXXXXXXX")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Type your message..."):
    
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)


    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="meta-llama/Llama-3.1-8B-Instruct:novita",  # Your loaded model name in LM Studio
                messages=st.session_state.messages,
                temperature=0.7
            )

            reply = response.choices[0].message.content
            st.markdown(reply)

    
    st.session_state.messages.append({"role": "assistant", "content": reply})
