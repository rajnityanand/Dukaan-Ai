
import streamlit as st

st.set_page_config(
    page_title="DukaanAI | Retail Intelligence",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sidebar
with st.sidebar:
    st.title("🛍️ DukaanAI")
    st.caption("Retail Intelligence Platform")
    st.divider()

    st.markdown("### Navigation")
    st.page_link("app.py", label="Overview", icon="🏠")
    st.page_link("pages/1_Demand_Forecast.py", label="Demand Forecast", icon="📈")
    st.page_link("pages/2_Product_Segmentation.py", label="Product Segmentation", icon="📦")
    st.page_link("pages/3_Inventory_Insights.py", label="Inventory Insights", icon="🏪")
    st.page_link("pages/4_ML_Lab.py", label="ML Lab", icon="🧪")
# Main page
st.title("DukaanAI")
st.subheader("AI-powered Retail Intelligence")

st.markdown(
    """
    Understand sales patterns, forecast future demand, and explore
    product performance through machine learning.
    """
)

st.info(
    "Development status: Dashboard setup is complete in progress. "
    "Verified dataset insights and trained model results will be "
    "connected as the ML pipeline is developed."
)

st.divider()
st.header("Platform Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Dataset", "Under Audit")

with col2:
    st.metric("Forecast Model", "In Development")

with col3:
    st.metric("Dashboard", "Prototype")

st.divider()
st.header("Explore DukaanAI")

left, right = st.columns(2)

with left:
    st.subheader("📈 Demand Forecasting")
    st.write(
        "Explore historical sales trends and compare actual "
        "sales with model predictions."
    )

    st.subheader("📦 Product Segmentation")
    st.write(
        "Group products by sales behaviour and performance "
        "using clustering techniques."
    )

with right:
    st.subheader("🏪 Inventory Insights")
    st.write(
        "Explore potential inventory insights when the "
        "available dataset supports them."
    )

    st.subheader("🧪 ML Lab")
    st.write(
        "Compare model performance and visualize experiments "
        "such as PCA and clustering."
    )

st.divider()
st.caption("DukaanAI | Machine Learning Project | Development Build")
