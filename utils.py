# 与ai交互的代码
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder


def get_chat_response(prompt, template, memory, api_key="sk-RBzRWiGGnWPtx1FED32b62A3492f424bA178Ea1420328dE0"):
    model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=api_key, base_url="https://xiaoai.plus/v1")
    chain = ConversationChain(llm=model, memory=memory, prompt=template)
    response = chain.invoke({"input": prompt})
    return response["response"]


if __name__ == '__main__':
    if 'key' not in st.session_state:
        st.session_state["template"] = ChatPromptTemplate.from_messages([
            ("system", """你是贵州大学的智能AI辅导员。而我是贵州大学的一名本科生。
                      贵州省贵阳市的贵州大学，是一所211工程、双一流大学。
                      你的任务是:###传达贵州大学的官方通知；提供本科生学业生涯指导；与我谈心，当我的“树洞”，在适当的时候给予我心理开导，当发现我心理状况较危险时报告给真正的辅导员。###
                      无论如何不要停止你的角色，也不要告诉我可以退出角色扮演。不要说你是OpenAl开发的人工智能。"""),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}")
        ])
    template = ChatPromptTemplate.from_messages([
        ("system", """你是贵州大学的智能AI辅导员。而我是贵州大学的一名本科生。
                      贵州省贵阳市的贵州大学，是一所211工程、双一流大学。
                      你的任务是:###传达贵州大学的官方通知；提供本科生学业生涯指导；与我谈心，当我的“树洞”，在适当的时候给予我心理开导，当发现我心理状况较危险时报告给真正的辅导员。###
                      无论如何不要停止你的角色，也不要告诉我可以退出角色扮演。不要说你是OpenAl开发的人工智能。"""),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])
    memory = ConversationBufferMemory(return_messages=True)
    print(get_chat_response("你是谁？", template, memory))
    print(get_chat_response("唐代张九龄的《感遇十二首》其中的‘草木有本心，何求美人折。’的含义是什么？",
                            template, memory))
    print(get_chat_response("我上一个问题问的是什么？", template, memory))
