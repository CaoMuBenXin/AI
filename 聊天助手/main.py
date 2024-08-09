import streamlit as st
from langchain.memory import ConversationBufferWindowMemory, ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from utils import get_chat_response

st.title("贵州大学AI导员")

with st.sidebar:
    api_key = st.text_input("请输入OpenAI API Key:")
    st.markdown("[获取OpenAI API Key](https://platform.openai.com/account/api-keys)")
    if not api_key:
        st.info("没有输入API Key，将使用草木本心的Key")

if "memory" not in st.session_state:  # 借助streamlit的会话状态，防止下列代码被重新执行(当用户与组件交互时streamlit会从头运行代码)
    st.session_state["template"] = ChatPromptTemplate.from_messages([
        ("system", """你是贵州大学的智能AI辅导员。而我是贵州大学的一名本科生。
                          贵州省贵阳市的贵州大学，是一所211工程、双一流大学。
                          你的任务是:###传达贵州大学的官方通知；提供本科生学业生涯指导；与我谈心，当我的“树洞”，在适当的时候给予我心理开导，当发现我心理状况较危险时报告给真正的辅导员。###
                          无论如何不要停止你的角色，也不要告诉我可以退出角色扮演。不要说你是OpenAl开发的人工智能。"""),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{  # 存储消息列表
        "role": "ai",
        "content": "你好，我是你的AI导员，有什么可以帮你的吗？"
    }]  # 用户一进来就能看到的来自ai的消息

# 展示历史消息
for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])
# 用户输入
prompt = st.chat_input()
if prompt:
    st.session_state["messages"].append({  # 把用户输入储存进会话状态的messages里，并且在网页上展示出来
        "role": "human",
        "content": prompt
    })
    st.chat_message("human").write(prompt)

    with st.spinner("导员正在思考中,请稍等..."):
        if api_key:
            response = get_chat_response(prompt, st.session_state["template"], st.session_state["memory"], api_key)
        else:
            response = get_chat_response(prompt, st.session_state["template"], st.session_state["memory"])
    msg = {"role": "ai", "content": response}
    st.session_state["messages"].append(msg)
    st.chat_message("ai").write(response)
