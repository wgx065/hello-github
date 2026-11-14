import streamlit as st
import pandas as pd
import io
from utils import apply_custom_css

st.set_page_config(page_title="Excel清洗器", page_icon="📊")
apply_custom_css()

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
            # 清洗逻辑：删除空值并去重
            df_cleaned = df.dropna().drop_duplicates()
            rows_deleted = len(df) - len(df_cleaned)
            
            if rows_deleted > 0:
                st.success(f"✅ 清洗完成！共清理了 {rows_deleted} 行无效或重复数据。")
                st.write(f"清洗后剩余 **{len(df_cleaned)}** 行数据。")
            else:
                st.info("✨ 你的数据非常干净，没有发现空行或重复行！")
            
            # 将清洗后的数据转为 Excel 并提供下载
            output = io.BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df_cleaned.to_excel(writer, index=False)
            
            st.download_button(
                label="📥 下载清洗后的 Excel 文件",
                data=output.getvalue(),
                file_name="cleaned_data.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
            
    except Exception as e:
        st.error(f"读取文件失败，请确保上传的是标准的 .xlsx 文件。错误信息：{e}")