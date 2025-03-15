from openai import OpenAI
import streamlit as st

with st.sidebar:
    # openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    st.image('TOC.tif', caption='Intelligent OFET Assistant')
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/YajingSun-Group/ofet_agent)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/YajingSun-Group/ofet_agent?quickstart=1)"

st.title(" 🏠 LLM-Based AI Agent for Organic Semiconductor Devices Research")
st.caption("🚀 Powered by advanced LLMs and machine learning algorithms, like ChatGPT")

    


st.markdown(
"""
## Introduction
 
An artificial intelligence agent for enhancing organic field-effect transistors (OFETs) performance by combining GPT-4 with advanced machine learning algorithms is presented. It efficiently extracts OFET experimental data from extensive literature and gives intelligent suggestions for OFET fabrication. This work showcases the application of large language models in organic optoelectronics, enhancing the development process in this field.

"""
)
st.image('Fig1.jpg', caption='Overview of the AI Agent for OFETs')

st.markdown(
"""

## Getting Started
- Step 1. Select a corresponding app from the sidebar
- Step 2. Meet the requirements of the sidebar of each App

""")

# if "messages" not in st.session_state:
#     st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

# for msg in st.session_state.messages:
#     st.chat_message(msg["role"]).write(msg["content"])

# if prompt := st.chat_input():
#     if not openai_api_key:
#         st.info("Please add your OpenAI API key to continue.")
#         st.stop()

#     client = OpenAI(api_key=openai_api_key)
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     st.chat_message("user").write(prompt)
#     response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
#     msg = response.choices[0].message.content
#     st.session_state.messages.append({"role": "assistant", "content": msg})
#     st.chat_message("assistant").write(msg)
