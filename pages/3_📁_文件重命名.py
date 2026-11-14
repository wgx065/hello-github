import streamlit as st
import zipfile
import io
from utils import apply_custom_css

st.set_page_config(page_title="文件重命名", page_icon="📁")
apply_custom_css()

st.title("📁 FILE RENAMER")
# --- 下面粘贴你原来写的文件重命名逻辑 ---
uploaded_files = st.file_uploader("上传你的文件 (支持多选)", accept_multiple_files=True)
prefix = st.text_input("输入统一前缀", placeholder="例如: 2026_项目_")
if st.button("执行重命名并打包"):
    if uploaded_files:
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "w") as z:
            for file in uploaded_files:
                new_name = prefix + file.name
                z.writestr(new_name, file.getvalue())
        st.success(f"✅ 成功处理了 {len(uploaded_files)} 个文件！")
        st.download_button("📥 点击下载 ZIP 压缩包", data=zip_buffer.getvalue(), file_name="renamed_files.zip", mime="application/zip")
    else:
        st.warning("⚠️ 请先上传文件哦！")