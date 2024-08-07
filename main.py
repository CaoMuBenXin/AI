import streamlit as st
from utils import generate_xiaohongshu

st.header("爆款小红书AI写作助手")
with st.sidebar:
    api_key = st.text_input("输入你的OpenAI密钥:", type="password")
    st.markdown("[获取OpenAI API密钥](https://platform.openai.com/account/api-keys)")

subject = st.text_input("主题")
submit = st.button("开始写作")
if submit and not subject:
    st.info("请输入生成内容的主题")
    st.stop()
if submit:
    with st.spinner("AI正在努力创作中，请稍等"):
        if api_key:
            result = generate_xiaohongshu(subject=subject, api_key=api_key)
        else
            st.info("没有输入api密钥，将使用草木本心的密钥")
            result = generate_xiaohongshu(subject=subject)
    st.divider()
    #分成左右两列
    left, right = st.columns(2)
    with left:
        st.markdown("### 标题:\n")
        st.write(result.titles[0])
        st.write(result.titles[1])
        st.write(result.titles[2])
        st.write(result.titles[3])
        st.write(result.titles[4])
    with right:
        st.markdown("### 正文:\n")
        st.write(result.content)
