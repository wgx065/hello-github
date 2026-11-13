import streamlit as st
import time

# 1. 页面基础配置
st.set_page_config(page_title="Next-Gen Engine", page_icon="⚡", layout="centered")

# 2. 注入暗黑科技风 CSS (视觉装x核心)
st.markdown("""
<style>
/* 强制修改整个应用的背景 */
[data-testid="stAppViewContainer"] {
    background-color: #0E1117;
    color: #FAFAFA;
}

/* 修改标题的特效 */
h1 {
    color: #00FFAA !important; /* 强制生效 */
    text-align: center;
    font-family: 'Courier New', monospace;
    text-shadow: 0 0 15px #00FFAA, 0 0 30px #00FFAA; /* 增强发光效果 */
}

/* 修改按钮的特效 */
.stButton>button {
    background-color: #00FFAA !important;
    color: #0E1117 !important;
    font-weight: bold;
    border-radius: 10px;
    width: 100%;
    border: none;
    box-shadow: 0 0 10px #00FFAA; /* 给按钮加个外发光 */
    transition: all 0.3s ease;
}

/* 按钮悬浮时的效果 */
.stButton>button:hover {
    box-shadow: 0 0 20px #00FFAA, 0 0 40px #00FFAA;
    transform: scale(1.02);
}
</style>
""", unsafe_allow_html=True)

# 3. 网页内容展示
st.title("⚡ NEXT-GEN ENGINE")
st.write("***An advanced Python-powered solution for next-level automation.***")
st.write("---")

# 4. 交互体验区
user_input = st.text_input("【 输入测试数据 Input Data 】", placeholder="随便打几个字试试...")

if st.button("🚀 INITIALIZE ENGINE (启动引擎)"):
    if user_input:
        # 假装在算力
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i + 1)
        
        # 下面开始做真正的分析！
        st.success("✅ 分析完成！以下是结果：")
        
        # 统计字数
        char_count = len(user_input)
        st.write(f"📝 **你输入的文字长度**：{char_count} 个字符")
        
        # 判断是否包含特定词汇
        if "hello" in user_input.lower():
            st.write("👋 **系统提示**：检测到你输入了问候语 (hello)！")
        else:
            st.write("🔍 **系统提示**：这是一段普通文本。")
            
        # 反转文字（展示点魔术）
        st.write(f"🔃 **文字反转**：{user_input[::-1]}")
        
    else:
        st.warning("⚠️ 请输入数据后再启动！")