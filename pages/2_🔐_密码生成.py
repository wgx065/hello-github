import streamlit as st
import random
import string
from utils import apply_custom_css

st.set_page_config(page_title="密码生成器", page_icon="🔐")
apply_custom_css()

st.title("🔐 PASSWORD GENERATOR")
# --- 下面粘贴你原来写的密码生成逻辑 ---
password_length = st.slider("选择密码长度", min_value=8, max_value=32, value=16)
col1, col2 = st.columns(2)
with col1:
    include_numbers = st.checkbox("包含数字")
with col2:
    include_symbols = st.checkbox("包含符号")
if st.button("生成密码"):
    characters = string.ascii_letters
    if include_numbers: characters += string.digits
    if include_symbols: characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    st.success("你的专属密码已生成：")
    st.code(password, language="text")