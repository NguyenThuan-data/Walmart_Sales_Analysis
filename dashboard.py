import streamlit as st
import pandas as pd
import plotly.express as px
from forecaster import SalesForecaster

# Page configuration
st.set_page_config(page_title="Walmart Sales Strategy Dashboard", layout="wide")

# Custom Styling
st.markdown("""
<style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
</style>
""", unsafe_allow_stdio=True)

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv('Walmart.csv', encoding_errors='ignore')
    df['unit_price'] = df['unit_price'].str.replace('$', '', regex=False).astype(float)
    df['total_amount'] = df['unit_price'] * df['quantity']
    df['date'] = pd.to_datetime(df['date'], dayfirst=True)
    df['hour'] = pd.to_datetime(df['time']).dt.hour
    return df

df = load_data()

# Sidebar Filters
st.sidebar.title("📊 Filter Insights")
selected_branch = st.sidebar.multiselect("Select Branch", options=df['Branch'].unique(), default=df['Branch'].unique())
selected_category = st.sidebar.multiselect("Select Category", options=df['category'].unique(), default=df['category'].unique())

filtered_df = df[df['Branch'].isin(selected_branch) & df['category'].isin(selected_category)]

# Header
st.title("🛒 Walmart Sales Strategy Dashboard")
st.markdown("Transforming raw retail data into actionable business intelligence.")

# Top Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"${filtered_df['total_amount'].sum():,.2f}")
col2.metric("Avg. Rating", f"{filtered_df['rating'].mean():.1f} ⭐")
col3.metric("Profit Margin", f"{filtered_df['profit_margin'].mean()*100:.1f}%")
col4.metric("Transactions", f"{len(filtered_df):,}")

# Row 1: Sales Trends & Forecasting
st.divider()
col_a, col_b = st.columns([2, 1])

with col_a:
    st.subheader("📈 Sales Trends Over Time")
    daily_sales = filtered_df.groupby('date')['total_amount'].sum().reset_index()
    fig = px.line(daily_sales, x='date', y='total_amount', title="Daily Revenue ($)")
    st.plotly_chart(fig, use_container_width=True)

with col_b:
    st.subheader("🔮 7-Day Sales Forecast")
    forecaster = SalesForecaster(filtered_df)
    forecast = forecaster.predict_next_week()
    fig_f = px.bar(forecast, x='date', y='predicted_sales', title="Predicted Revenue ($)", color_discrete_sequence=['#FF4B4B'])
    st.plotly_chart(fig_f, use_container_width=True)

# Row 2: Operational Insights
st.divider()
col_c, col_d = st.columns(2)

with col_c:
    st.subheader("⏰ Peak Hour Optimization")
    hourly_sales = filtered_df.groupby('hour')['invoice_id'].count().reset_index()
    fig_h = px.area(hourly_sales, x='hour', y='invoice_id', title="Transaction Volume by Hour", labels={'invoice_id': 'Transactions'})
    st.plotly_chart(fig_h, use_container_width=True)
    st.info("💡 **Strategy:** Staffing should peak between 3 PM and 8 PM to match customer density.")

with col_d:
    st.subheader("🛍️ Profitability by Category")
    cat_profit = filtered_df.groupby('category')['total_amount'].sum().reset_index()
    fig_p = px.pie(cat_profit, values='total_amount', names='category', hole=0.4, title="Revenue Contribution")
    st.plotly_chart(fig_p, use_container_width=True)

# Strategy Footer
st.sidebar.markdown("---")
st.sidebar.subheader("🎯 Actionable Strategy")
st.sidebar.write("- **Upsell Opportunity:** Focus 'Health & Beauty' bundles during peak 7 PM hours.")
st.sidebar.write("- **Inventory Alert:** High Fashion demand in Bedford Branch requires weekly restock.")
