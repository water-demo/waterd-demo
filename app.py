import streamlit as st

st.set_page_config(page_title="给水设计AI辅助工具", layout="wide")
st.title("给水工程设计AI辅助工具（原型Demo）")

# ===== 左侧：参数初算 =====
col1, col2 = st.columns(2)

with col1:
    st.subheader("📐 输水管线水头损失计算")
    
    管径 = st.number_input("管径 (mm)", value=500, min_value=100, max_value=2000)
    管长 = st.number_input("管线长度 (m)", value=1000, min_value=100)
    流量 = st.number_input("设计流量 (m³/h)", value=500, min_value=10)
    
    if st.button("开始计算", type="primary"):
        # 海曾-威廉姆斯公式简化版（仅供演示）
        流速 = 流量 / (3.14 * (管径/1000/2)**2) / 3600
        水头损失 = 10.67 * 管长 * (流量/3600)**1.852 / (120**1.852 * (管径/1000)**4.87)
        
        st.success(f"计算结果：")
        st.metric("流速", f"{流速:.2f} m/s")
        st.metric("沿程水头损失", f"{水头损失:.2f} m")
        st.caption("计算依据：《给水排水设计手册》海曾-威廉姆斯公式")

# ===== 右侧：规范检索 =====
with col2:
    st.subheader("🔍 规范条文检索")
    
    关键词 = st.text_input("输入关键词", placeholder="例如：水头损失")
    
    if 关键词:
        # 模拟规范库查询（实际接SQLite）
        规范库 = {
            "水头损失": "《室外给水设计标准》GB 50013-2018 第7.3.2条：管道沿程水头损失可采用海曾-威廉姆斯公式计算...",
            "管径": "《室外给水设计标准》GB 50013-2018 第7.1.5条：输水干管管径应根据设计流量和经济流速确定...",
            "流速": "《给水排水设计手册》第3册：给水管道经济流速宜控制在0.6-2.0m/s..."
        }
        
        for k, v in 规范库.items():
            if 关键词 in k:
                st.info(f"📋 **{k}**\n\n{v}")
                break
        else:
            st.warning("未找到相关条文，请尝试其他关键词")

st.divider()
st.caption("本Demo展示：参数初算 + 规范检索两大核心功能 | 后端接SQLite后可实现完整案例调用与成果生成")