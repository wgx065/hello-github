import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io
import zipfile
from utils import apply_custom_css

st.set_page_config(page_title="图片加水印", page_icon="🖼️")
apply_custom_css()

st.title("🖼️ BATCH WATERMARKER")
st.write("***Add text watermarks to multiple images and download as a ZIP.***")
st.write("---")

# 1. 接收用户上传的图片
uploaded_images = st.file_uploader("上传图片 (支持多选，建议 jpg/png)", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if uploaded_images:
    st.write(f"已加载 **{len(uploaded_images)}** 张图片")
    
    # 2. 设置水印参数
    col1, col2 = st.columns(2)
    with col1:
        watermark_text = st.text_input("水印文字", value="© YourName 2026")
        font_size = st.slider("字体大小", min_value=15, max_value=100, value=40)
    with col2:
        opacity = st.slider("透明度 (0=全透, 255=不透明)", min_value=10, max_value=255, value=150)
        position = st.selectbox("水印位置", ["右下角", "左下角", "居中"])

    # 3. 核心绘图函数（抽离出来，预览和批量生成共用）
    def add_watermark(img, text, size, pos, alpha):
        # 确保图片是 RGB 模式（去掉透明通道，直接画字最稳妥）
        img = img.convert("RGB")
        draw = ImageDraw.Draw(img)
        
        try:
            # 使用幼圆字体
            font = ImageFont.truetype("SIMYOU.TTF", size)
        except IOError:
            font = ImageFont.load_default()
            
        # 获取文字长宽
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        img_w, img_h = img.size
        if pos == "右下角":
            x, y = img_w - text_width - 20, img_h - text_height - 30
        elif pos == "左下角":
            x, y = 20, img_h - text_height - 30
        else: # 居中
            x, y = (img_w - text_width) // 2, (img_h - text_height) // 2
            
         # 荧光绿文字 + 黑色描边
        draw.text(
            (x, y), text, font=font, 
            fill=(57, 255, 20, alpha),       # 荧光绿 (R:57, G:255, B:20) 加上透明度
            stroke_width=2,                  # 描边宽度
            stroke_fill=(0, 0, 0, alpha)     # 纯黑描边
        )
        return img

    # 4. 预览功能
    if st.button("👁️ 预览第一张图效果"):
        first_img = Image.open(uploaded_images[0])
        preview_result = add_watermark(first_img, watermark_text, font_size, position, opacity)
        st.image(preview_result, caption="预览效果", use_container_width=True)

    # 5. 批量生成并打包
    if st.button("🚀 批量生成水印并打包"):
        if not watermark_text:
            st.warning("请先输入水印文字！")
        else:
            zip_buffer = io.BytesIO()
            
            with zipfile.ZipFile(zip_buffer, "w") as z:
                for uploaded_img in uploaded_images:
                    img = Image.open(uploaded_img)
                    # 调用核心函数加上水印
                    watermarked_img = add_watermark(img, watermark_text, font_size, position, opacity)
                    
                    # 将处理后的图片存为 JPEG 格式放进 ZIP
                    img_byte_arr = io.BytesIO()
                    watermarked_img.save(img_byte_arr, format='JPEG', quality=90)
                    z.writestr(f"watermarked_{uploaded_img.name}", img_byte_arr.getvalue())
            
            st.success(f"✅ 成功为 {len(uploaded_images)} 张图片添加水印！")
            st.download_button(
                label="📥 下载水印图片 ZIP 压缩包",
                data=zip_buffer.getvalue(),
                file_name="watermarked_images.zip",
                mime="application/zip"
            )