import streamlit as st
import time
from utils import apply_custom_css

st.set_page_config(page_title="文本分析", page_icon="📝")
apply_custom_css()

st.title("📝 NEXT-GEN TEXT ANALYZER")
# --- 下面粘贴你原来写的那段：输入框、启动引擎按钮、进度条、分析逻辑 ---
user_input = st.text_input("【 输入测试数据 Input Data 】", placeholder="随便打几个字试试...")
if st.button("🚀 INITIALIZE ENGINE (启动引擎)"):
    if user_input:
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i + 1)
        st.success("✅ 分析完成！以下是结果：")
        st.write(f"📝 **你输入的文字长度**：{len(user_input)} 个字符")
        if "hello" in user_input.lower():
            st.write("👋 **系统提示**：检测到你输入了问候语 (hello)！")
        else:
            st.write("🔍 **系统提示**：这是一段普通文本。")
        st.write(f"🔃 **文字反转**：{user_input[::-1]}")
    else:
        st.warning("⚠️ 请输入数据后再启动！")