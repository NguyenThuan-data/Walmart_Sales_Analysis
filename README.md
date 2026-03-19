# 🛒 Walmart Sales Strategy Dashboard

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Framework-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![Analysis](https://img.shields.io/badge/Analysis-Predictive-green.svg)](#predictive-forecasting)

## 📋 Table of Contents
- [🎯 Executive Summary](#-executive-summary)
- [💻 Tech Stack](#-tech-stack)
- [🖥️ Interactive Dashboard](#-interactive-dashboard)
- [📈 Predictive Forecasting](#-predictive-forecasting)
- [🚦 Actionable Insights](#-actionable-insights)
- [🛠️ How to Run](#-how-to-run)

---

## 🎯 Executive Summary
This project transforms raw retail transaction data into a **Strategic Decision-Support System**. By leveraging an end-to-end ETL pipeline and a modern interactive dashboard, I've enabled Walmart branch managers to optimize staffing, identify high-profit product categories, and forecast future revenue with data-driven confidence.

---

## 💻 Tech Stack
- **Dashboard UI:** Streamlit, Plotly
- **Data Engineering:** Python (Pandas, NumPy)
- **Predictive Modeling:** Scikit-Learn (Linear Regression)
- **Database:** PostgreSQL (SQLAlchemy, Psycopg2)

---

## 🖥️ Interactive Dashboard
I have enhanced this project from a static notebook into a **Live Business Intelligence Platform**.

> [!TIP]
> **View the App Preview below!** (Implementing real-time filters for Branch, City, and Category).

![Dashboard Preview](./images/dashboard_preview.png)

---

## 📈 Predictive Forecasting
Unlike traditional past-tense analysis, this system includes a **Sales Forecaster** that predicts revenue for the next 7 days based on historical seasonality and day-of-week trends. This allows for proactive inventory and labor management.

---

## 🚦 Actionable Insights
- **⏰ Peak Hour Optimization:** Identified a critical transaction spike between **3 PM - 8 PM**. Strategy: Implement dynamic staffing to maximize conversion during these "Golden Hours."
- **🛍️ Profit Concentration:** 90% of profit is driven by **Fashion** and **Home** categories. Strategy: Bundle "Health & Beauty" items as loss-leaders to increase average basket size.
- **📍 Regional Scaling:** The **Bedford Branch** shows the highest volume-to-staffing efficiency. Strategy: Standardize Bedford's layout across underperforming branches.

---

## 🛠️ How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/NguyenThuan-data/Walmart_Sales_Analysis.git
cd Walmart_Sales_Analysis
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Launch the Dashboard
```bash
streamlit run dashboard.py
```
---

## 🎓 Lessons Learned
1. **Product > Code:** A recruiter spends 10 seconds on a repo. An interactive dashboard explains the value 10x faster than a 1,000-line script.
2. **Predictive over Descriptive:** Business value lies in answering "What next?", not just "What happened?".
