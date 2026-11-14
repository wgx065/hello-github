import streamlit as st
from utils import apply_custom_css

# 1. 页面基础配置
st.set_page_config(page_title="Next-Gen Toolbox", page_icon="⚡", layout="centered")

# 2. 应用全局暗黑特效
apply_custom_css()

# 3. 主页内容
st.title("⚡ NEXT-GEN TOOLBOX")
st.write("***An advanced Python-powered solution for next-level automation.***")
st.write("---")

st.info("👈 请从左侧导航栏选择你需要使用的工具。")
st.write("### 欢迎使用！")
st.write("这是一个基于 Python 和 Streamlit 构建的多功能工具箱。所有的工具都在左侧的独立页面中运行，代码结构更加清晰、专业。")