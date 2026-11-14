import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io
import zipfile
from utils import apply_custom_css

st.set_page_config(page_title="图片加水印", page_icon="🖼️")
apply_custom_css()

st.title("🖼️ BATCH WATERMARKER")
st.write("***Add professional text watermarks to multiple images.***")
st.write("---")

# 1. 接收用户上传的图片
uploaded_images = st.file_uploader("上传图片 (支持多选，建议 jpg/png)", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

if uploaded_images:
    st.write(f"已加载 **{len(uploaded_images)}** 张图片")
    
    # 2. 设置水印参数（默认专业配置）
    col1, col2 = st.columns(2)
    with col1:
        watermark_text = st.text_input("水印文字", value="© 仅供预览，禁止商用")
        font_size = st.slider("字体大小", min_value=15, max_value=100, value=35)
    with col2:
        opacity = st.slider("透明度 (0=全透, 255=不透明)", min_value=10, max_value=255, value=180)
        position = st.selectbox("水印位置", ["右下角", "左下角", "居中"], index=0)

    # 3. 核心绘图函数（包含字体智能匹配）
    def add_watermark(img, text, size, pos, alpha):
        img = img.convert("RGB")
        draw = ImageDraw.Draw(img)
        
        # 智能匹配字体（优先本地 Windows，其次云端 Linux）
                # 读取项目文件夹里的自定义字体
        try:
            font = ImageFont.truetype("myfont.ttf", size)
        except IOError:
            # 如果没找到，就用默认字体保底（会变方块，但不会崩溃）
            font = ImageFont.load_default()
            
        # 获取文字长宽
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        img_w, img_h = img.size
        # 留出稍微宽一点的边距（30px），显得更专业
        if pos == "右下角":
            x, y = img_w - text_width - 30, img_h - text_height - 40
        elif pos == "左下角":
            x, y = 30, img_h - text_height - 40
        else: # 居中
            x, y = (img_w - text_width) // 2, (img_h - text_height) // 2
            
        # 专业画法：白色文字 + 黑色微透明描边（无论深浅背景都清晰）
        draw.text(
            (x, y), text, font=font, 
            fill=(255, 255, 255, alpha),       # 白色文字
            stroke_width=5,                    # 描边加粗
            stroke_fill=(0, 0, 0, int(alpha * 0.7)) # 黑色半透明描边
        )
        return img

    # 4. 预览功能
    if st.button("👁️ 预览第一张图效果"):
        first_img = Image.open(uploaded_images[0])
        preview_result = add_watermark(first_img, watermark_text, font_size, position, opacity)
        st.image(preview_result, caption="预览效果 (专业白字黑边)", use_container_width=True)

    # 5. 批量生成并打包
    if st.button("🚀 批量生成水印并打包"):
        if not watermark_text:
            st.warning("请先输入水印文字！")
        else:
            zip_buffer = io.BytesIO()
            
            with zipfile.ZipFile(zip_buffer, "w") as z:
                for uploaded_img in uploaded_images:
                    img = Image.open(uploaded_img)
                    watermarked_img = add_watermark(img, watermark_text, font_size, position, opacity)
                    
                    img_byte_arr = io.BytesIO()
                    watermarked_img.save(img_byte_arr, format='JPEG', quality=95) # 提高保存质量
                    z.writestr(f"watermarked_{uploaded_img.name}", img_byte_arr.getvalue())
            
            st.success(f"✅ 成功为 {len(uploaded_images)} 张图片添加专业水印！")
            st.download_button(
                label="📥 下载水印图片 ZIP 压缩包",
                data=zip_buffer.getvalue(),
                file_name="watermarked_images.zip",
                mime="application/zip"
            )