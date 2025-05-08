

import os
import httpx
from openai import OpenAI
import streamlit as st
from dashscope import Application
from http import HTTPStatus

with st.sidebar:
    openai_api_key = st.text_input("LLM API Key", key="chatbot_api_key", type="password")
    "[Get an API key](https://bailian.console.aliyun.com/?tab=home#/home)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"
    
    # Add preset prompts section in sidebar
    st.markdown("### 预设问题")
    
    # Create buttons for preset prompts
    if st.button("Suggest OFET device configurations", key="preset_configurations"):
        st.session_state["preset_prompt"] = "我的有机半导体分子的SMILES是CCCCCCN1C(=O)c2ccc3c4c(ccc(c24)C1=O)-c1c-3c(C#N)c2cc3c(C#N)c4c(c(C#N)c3cc2c1C#N)-c1ccc2c3c(ccc-4c13)C(=O)N(CCCCCC)C2=O，请你帮我推荐一套配置及出处"
    
    if st.button("Cases in the literature", key="preset_mobility"):
        st.session_state["preset_prompt"] = "Currently, l am using the DP-DTT as the semiconductor layer for OFET. Themobility of the OFETs obtained through the vacuum deposition method is0.42.l am looking to improve the mobility of this OFET. Please recommendother suitable fabrication methods."

st.title("💬 OFET Lab Advisor")
st.caption("🚀 A streamlit chatbot powered by Qwen LLM")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# Initialize preset_prompt in session state if it doesn't exist
if "preset_prompt" not in st.session_state:
    st.session_state["preset_prompt"] = None

# Display chat messages from history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Define the streaming response generator
def dashscope_response_generator(api_key, app_id, prompt):
    responses = Application.call(
        api_key=api_key,
        app_id=app_id,
        prompt=prompt,
        stream=True,
        incremental_output=True
    )
    
    for response in responses:
        if response.status_code != HTTPStatus.OK:
            yield f"Error: {response.message} (Code: {response.status_code})"
            break
        else:
            yield response.output.text

# Get user input or use preset prompt
user_input = st.chat_input("请输入您的问题...")
prompt_to_process = st.session_state["preset_prompt"] or user_input

# Process the prompt
if prompt_to_process:
    if not openai_api_key:
        st.info("Please add your API key to continue.")
        st.stop()

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt_to_process})
    st.chat_message("user").write(prompt_to_process)
    
    # Display assistant response with streaming
    with st.chat_message("assistant"):
        full_response = st.write_stream(
            dashscope_response_generator(
                api_key=openai_api_key,
                app_id='e13d1f3c382b489fa8e40b45f55a474d',
                prompt=prompt_to_process
            )
        )
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    
    # Clear the preset prompt after processing
    st.session_state["preset_prompt"] = None
