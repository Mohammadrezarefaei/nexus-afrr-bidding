import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Nexus aFRR Bidding", page_icon="🤖", layout="wide")

st.markdown("<style>.main {background-color: #0f172a; color: #f8fafc;}</style>", unsafe_allow_html=True)
st.title("🤖 Nexus aFRR: AI-Driven Bidding Strategy")

# Sidebar
st.sidebar.header("Strategy Controls")
battery_capacity = st.sidebar.number_input("Battery Capacity (MW)", value=2.5, step=0.5)
bid_markdown = st.sidebar.slider("Bid Markdown Strategy (%)", 70, 100, 92) / 100.0

# Mock Data Generation for Dashboard
np.random.seed(42)
hours = 336 # 14 days
time_index = pd.date_range(start="2026-08-01", periods=hours, freq="h")
actual_prices = np.clip(15 + 10 * np.sin(np.linspace(0, 10 * np.pi, hours)) + np.random.normal(0, 5, hours), 0, 100)
predicted_prices = actual_prices + np.random.normal(0, 1.5, hours) # Simulating an MAE of ~1.5

# Revenue Simulation
df = pd.DataFrame({'Actual': actual_prices, 'Pred': predicted_prices}, index=time_index)
df['Our_Bid'] = df['Pred'] * bid_markdown
df['Accepted'] = df['Our_Bid'] <= df['Actual']
df['Revenue'] = np.where(df['Accepted'], df['Actual'] * battery_capacity, 0.0)
df['Optimal'] = df['Actual'] * battery_capacity

total_revenue = df['Revenue'].sum()
optimal_revenue = df['Optimal'].sum()
win_rate = df['Accepted'].mean() * 100

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Capture Rate", f"{(total_revenue/optimal_revenue)*100:.1f}%")
col2.metric("Auction Win Rate", f"{win_rate:.1f}%")
col3.metric("Total Revenue", f"€{total_revenue:,.0f}")

st.markdown("---")

# Plotting Cumulative Revenue
st.subheader("📈 Cumulative Revenue Generation")
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(12, 5))
fig.patch.set_facecolor('#0f172a')
ax.set_facecolor('#0f172a')

ax.plot(df.index, df['Optimal'].cumsum(), color='#94a3b8', lw=2, linestyle=':', label='Perfect Oracle')
ax.plot(df.index, df['Revenue'].cumsum(), color='#4ade80', lw=3, label='AI Strategy')
ax.fill_between(df.index, df['Revenue'].cumsum(), color='#4ade80', alpha=0.2)

ax.grid(True, color='#1e293b', linestyle='-', alpha=0.6)
ax.legend(loc='upper left', frameon=True, facecolor='#1e293b', labelcolor='#f8fafc')

st.pyplot(fig)
