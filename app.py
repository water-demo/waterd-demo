import streamlit as st

st.set_page_config(page_title="给水设计AI辅助工具", layout="wide")
st.title("给水工程设计AI辅助工具（原型Demo）")

# ===== 左侧：参数初算 =====
col1, col2 = st.columns(2)

with col1:
    st.subheader("📐 给水厂关键单元参数推荐")
    
    设计规模 = st.number_input("处理规模 (万m³/d)", value=5.0, min_value=0.1, step=0.5, format="%.1f")
    进水负荷 = st.number_input("进水SS (mg/L)", value=200, min_value=10, max_value=2000)
    投加量 = st.number_input("混凝剂投加量 (mg/L)", value=30, min_value=5, max_value=200)
    
    if st.button("开始计算", type="primary"):
        有效容积 = 设计规模 * 10000 / 24
        固体负荷 = 进水负荷 * 设计规模 * 10 / 24
        加药量 = 投加量 * 设计规模 * 10000 / 1000 / 24
        
        st.success("关键参数推荐：")
        st.metric("有效容积", f"{有效容积:.0f} m³")
        st.metric("固体负荷", f"{固体负荷:.0f} kg/h")
        st.metric("加药量", f"{加药量:.1f} kg/h")
        st.caption("参数推荐依据：《给水排水设计手册》第三册")

# ===== 右侧：规范检索 =====
with col2:
    st.subheader("🔍 规范条文检索")
    
    关键词 = st.text_input("输入关键词", placeholder="例如：水头损失")
    
    if 关键词:
        规范库 = {
            "水头损失": "《室外给水设计标准》GB 50013-2018 第7.3.2条：管道沿程水头损失可采用海曾-威廉姆斯公式计算...",
            "管径": "《室外给水设计标准》GB 50013-2018 第7.1.5条：输水干管管径应根据设计流量和经济流速确定...",
            "流速": "《给水排水设计手册》第3册：给水管道经济流速宜控制在0.6-2.0m/s...",
            "混凝": "《室外给水设计标准》GB 50013-2018 第9.2.1条：混凝剂投加量应根据原水水质和药剂种类通过试验确定...",
            "沉淀": "《室外给水设计标准》GB 50013-2018 第9.4.1条：沉淀池设计应保证出水浊度满足后续处理要求..."
        }
        
        找到 = False
        for k, v in 规范库.items():
            if 关键词 in k or 关键词 in v:
                st.info(f"📋 **{k}**\n\n{v}")
                找到 = True
                break
        
        if not 找到:
            st.warning("未找到相关条文，请尝试其他关键词")

st.divider()
st.caption("本Demo展示：参数初算 + 规范检索两大核心功能 | 后端接SQLite后可实现完整案例调用与成果生成")
st.caption("📅 后续版本规划：接入SQLite案例库实现历史项目调用 | python-docx一键生成计算书 | 微信小程序适配移动端查询")
