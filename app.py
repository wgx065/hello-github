import streamlit as st
import time
import random
import string
import zipfile
import io
import pandas as pd
# ==========================================
# 1. 页面基础配置 & 全局 CSS 特效 (暗黑科技风)
# ==========================================
st.set_page_config(page_title="Next-Gen Toolbox", page_icon="⚡", layout="centered")

st.markdown("""
<style>
/* 强制修改整个应用的背景 */
[data-testid="stAppViewContainer"] {
    background-color: #0E1117;
    color: #FAFAFA;
}
/* 标题特效 */
h1 {
    color: #00FFAA !important; 
    text-align: center;
    font-family: 'Courier New', monospace;
    text-shadow: 0 0 15px #00FFAA, 0 0 30px #00FFAA; 
}
/* 按钮特效 */
.stButton>button {
    background-color: #00FFAA !important;
    color: #0E1117 !important;
    font-weight: bold;
    border-radius: 10px;
    width: 100%;
    border: none;
    box-shadow: 0 0 10px #00FFAA;
    transition: all 0.3s ease;
}
.stButton>button:hover {
    box-shadow: 0 0 20px #00FFAA, 0 0 40px #00FFAA;
    transform: scale(1.02);
}
/* ==========================================
   全局背景与组件样式
   ========================================== */
[data-testid="stAppViewContainer"] {
    background-color: #0E1117;
    color: #FAFAFA;
}

/* 主标题特效 */
h1 {
    color: #00FFAA !important; 
    text-align: center;
    font-family: 'Courier New', monospace;
    text-shadow: 0 0 15px #00FFAA, 0 0 30px #00FFAA; 
}

/* 按钮特效 */
.stButton>button {
    background-color: #00FFAA !important;
    color: #0E1117 !important;
    font-weight: bold;
    border-radius: 10px;
    width: 100%;
    border: none;
    box-shadow: 0 0 10px #00FFAA;
    transition: all 0.3s ease;
}

.stButton>button:hover {
    box-shadow: 0 0 20px #00FFAA, 0 0 40px #00FFAA;
    transform: scale(1.02);
}

/* ==========================================
   终极对齐魔法：主页面与侧边栏布局
   ========================================== */
/* 1. 右侧主内容区：留出合适的顶部空间 */
[data-testid="stAppViewContainer"] > .main > div:first-child {
    padding-top: 2rem !important; 
}

/* 2. 左侧边栏：强制恢复黑底绿边，并去掉原生留白 */
[data-testid="stSidebar"], [data-testid="stSidebar"] > div:first-child {
    background-color: #1A1F2B !important;
    border-right: 2px solid #00FFAA;
    padding-top: 0rem !important; /* 清零顶部留白 */
}

/* 3. 左侧“导航菜单”标题：居中发光，并精准下移到与右侧对齐 */
[data-testid="stSidebar"] h1 {
    text-align: center !important;
    color: #00FFAA !important;
    text-shadow: 0 0 10px #00FFAA;
    margin-top: 3.2rem !important; /* 这个数字决定了左右是否水平对齐 */
    margin-bottom: 20px !important;
}

/* 4. 侧边栏文字和提示框美化 */
[data-testid="stSidebar"] label p {
    color: #FAFAFA !important; 
    font-size: 16px !important;
    font-weight: bold;
}

[data-testid="stSidebar"] div[data-testid="stAlert"] {
    background-color: #0E1117 !important; 
    border: 1px solid #00FFAA !important;
}

[data-testid="stSidebar"] div[data-testid="stAlert"] p {
    color: #00FFAA !important; 
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. 侧边栏导航 (多页面核心)
# ==========================================
st.sidebar.title("🛠️ 导航菜单")
# 使用 radio 单选框来做导航
app_mode = st.sidebar.radio(
    "请选择一个工具：",
     ["⚡ 文本分析器", "🔐 随机密码生成器", "📁 批量文件重命名", "📊 Excel 数据清洗器"]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 这是一个基于 Streamlit 开发的多功能工具集。")

# ==========================================
# 3. 页面路由 (根据选择显示不同内容)
# ==========================================

# --- 页面 A：文本分析器 (你原来的代码) ---
if app_mode == "⚡ 文本分析器":
    st.title("⚡ NEXT-GEN TEXT ANALYZER")
    st.write("***An advanced Python-powered text analysis tool.***")
    st.write("---")
    
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


# --- 页面 B：随机密码生成器 ---
elif app_mode == "🔐 随机密码生成器":
    st.title("🔐 PASSWORD GENERATOR")
    st.write("***Generate ultra-secure passwords for your accounts.***")
    st.write("---")
    
    password_length = st.slider("选择密码长度", min_value=8, max_value=32, value=16)
    
    col1, col2 = st.columns(2)
    with col1:
        include_numbers = st.checkbox("包含数字")
    with col2:
        include_symbols = st.checkbox("包含符号")
        
    if st.button("生成密码"):
        characters = string.ascii_letters
        if include_numbers:
            characters += string.digits
        if include_symbols:
            characters += string.punctuation
            
        password = ''.join(random.choice(characters) for _ in range(password_length))
        
        st.success("你的专属密码已生成：")
        st.code(password, language="text")


# --- 页面 C：批量文件重命名 ---
elif app_mode == "📁 批量文件重命名":
    st.title("📁 FILE RENAMER")
    st.write("***Batch rename your files and package them into a ZIP.***")
    st.write("---")
    
    uploaded_files = st.file_uploader("上传你的文件 (支持多选)", accept_multiple_files=True)
    prefix = st.text_input("输入统一前缀", placeholder="例如: 2026_项目_")
    
    if st.button("执行重命名并打包"):
        if uploaded_files:
            # 在内存中创建 ZIP 文件，避免服务器存留垃圾文件
            zip_buffer = io.BytesIO()
            
            with zipfile.ZipFile(zip_buffer, "w") as z:
                for file in uploaded_files:
                    new_name = prefix + file.name
                    z.writestr(new_name, file.getvalue())
            
            st.success(f"✅ 成功处理了 {len(uploaded_files)} 个文件！")
            
            # 提供下载按钮
            st.download_button(
                label="📥 点击下载 ZIP 压缩包",
                data=zip_buffer.getvalue(),
                file_name="renamed_files.zip",
                mime="application/zip"
            )
        else:
            st.warning("⚠️ 请先上传文件哦！")


# --- 页面 D：Excel 数据清洗器 ---
elif app_mode == "📊 Excel 数据清洗器":
    st.title("📊 EXCEL DATA CLEANER")
    st.write("***Upload an Excel file to remove empty rows and duplicates.***")
    st.write("---")
    
    excel_file = st.file_uploader("上传 Excel 文件", type=["xlsx"])
    
    if excel_file:
        try:
            df = pd.read_excel(excel_file)
            st.write("📋 **原始数据预览：**")
            st.dataframe(df.head(10))
            st.write(f"原始数据共 **{len(df)}** 行。")
            
            if st.button("🚀 开始一键清洗"):
                df_cleaned = df.dropna().drop_duplicates()
                rows_deleted = len(df) - len(df_cleaned)
                
                if rows_deleted > 0:
                    st.success(f"✅ 清洗完成！共清理了 {rows_deleted} 行无效或重复数据。")
                    st.write(f"清洗后剩余 **{len(df_cleaned)}** 行数据。")
                    
                    import io
                    output = io.BytesIO()
                    with pd.ExcelWriter(output, engine='openpyxl') as writer:
                        df_cleaned.to_excel(writer, index=False)
                    
                    st.download_button(
                        label="📥 下载清洗后的 Excel 文件",
                        data=output.getvalue(),
                        file_name="cleaned_data.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )
                else:
                    st.info("✨ 你的数据非常干净，没有发现空行或重复行！")
        except Exception as e:
            st.error(f"读取文件失败，请确保上传的是标准的 .xlsx 文件。错误信息：{e}")           