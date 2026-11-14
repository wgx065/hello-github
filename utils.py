import streamlit as st

def apply_custom_css():
    st.markdown("""
    <style>
    /* ==========================================
       1. 全局暖色调背景与文字颜色
       ========================================== */
    [data-testid="stAppViewContainer"] { 
        background-color: #FDFBF7 !important; /* 温暖的米白/奶油色背景 */
        color: #333333 !important; /* 深灰/黑色文字，保护眼睛 */
    }

    /* ==========================================
       2. 大标题样式（暖色系强调色）
       ========================================== */
    h1 { 
        color: #D97736 !important; /* 温暖的赤陶土色 */
        text-align: center; 
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        font-weight: 800 !important;
    }

    /* ==========================================
       3. 按钮样式（圆润、有质感）
       ========================================== */
    .stButton>button { 
        background-color: #D97736 !important; /* 暖橙色按钮 */
        color: #FFFFFF !important; 
        font-weight: bold; 
        border-radius: 8px; 
        border: none; 
        box-shadow: 0 4px 6px rgba(217, 119, 54, 0.2); /* 柔和的阴影 */
        transition: all 0.2s ease; 
    }
    .stButton>button:hover { 
        background-color: #C26527 !important; /* 悬停时变深 */
        transform: translateY(-2px); /* 微微上浮 */
        box-shadow: 0 6px 12px rgba(217, 119, 54, 0.3);
    }

    /* ==========================================
       4. 左侧边栏（浅色，带细腻边框）
       ========================================== */
    [data-testid="stSidebar"] { 
        background-color: #F5EFE6 !important; /* 稍深一点的暖灰/卡其色 */
        border-right: 1px solid #E5DDD0 !important; 
    }

    /* 左侧导航菜单文字（确保是深色，清晰可见） */
    [data-testid="stSidebarNav"] a, 
    [data-testid="stSidebarNav"] a span, 
    [data-testid="stSidebarNav"] li {
        color: #4A4A4A !important; /* 深灰色文字 */
        font-weight: 600 !important;
        font-size: 16px !important;
    }
    [data-testid="stSidebarNav"] a:hover, 
    [data-testid="stSidebarNav"] a:hover span {
        color: #D97736 !important; /* 悬停时变成主题橙色 */
    }
    
    /* ==========================================
       5. 提示框 (Info Box) 和 表单文字
       ========================================== */
    [data-testid="stSidebar"] div[data-testid="stAlert"] { 
        background-color: #FFFFFF !important; 
        border: 1px solid #E5DDD0 !important; 
    }
    [data-testid="stSidebar"] div[data-testid="stAlert"] p { 
        color: #666666 !important; 
    }

    [data-testid="stWidgetLabel"] p {
        color: #333333 !important; 
        font-weight: bold !important;
    }
    </style>
    """, unsafe_allow_html=True)