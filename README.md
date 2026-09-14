# 🤖 Nexus aFRR: AI-Driven BESS Bidding Strategy

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://nexus-afrr-bidding-mtjctujz7tq2mddbcd85gm.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Machine Learning](https://img.shields.io/badge/Model-XGBoost-orange.svg)]()
[![Domain](https://img.shields.io/badge/Domain-Quantitative_Trading-brightgreen.svg)]()

**Nexus aFRR** is an industry-grade machine learning framework designed to optimize Battery Energy Storage System (BESS) participation in the German secondary reserve (aFRR) capacity market. By forecasting clearing prices using gradient boosting and applying a strategic bid markdown, the model maximizes the Value Capture Rate in a Pay-as-Cleared auction environment.

---

## 🌐 Live Interactive Dashboard

Experience the trading strategy and revenue simulation live:  
👉 **[Launch the Nexus aFRR Streamlit App](https://nexus-afrr-bidding-mtjctujz7tq2mddbcd85gm.streamlit.app/)**

---

## 📈 Quantitative Performance Metrics

Tested on an unseen chronological dataset (to strictly prevent data leakage), the algorithmic trading strategy demonstrated institutional-grade performance:

| Metric | Result | Description |
| :--- | :---: | :--- |
| **Value Capture Rate** | `86.6%` | Revenue generated compared to a Perfect Foresight Oracle. |
| **Auction Win Rate** | `73.8%` | Percentage of hours the AI bid successfully cleared the market. |
| **Prediction Error (MAE)** | `1.31` | Mean Absolute Error [EUR/MW] for price forecasting. |
| **Total Revenue** | `€13,878` | Simulated earnings over a 428-hour test window (2.5 MW Asset). |

---

## 📊 Strategy Execution & Value Creation

### Cumulative Revenue: AI Strategy vs. Perfect Foresight
*The chart below illustrates the accumulated revenue of the XGBoost-driven strategy tracking closely behind the theoretical maximum revenue.*

![Cumulative Revenue](https://raw.githubusercontent.com/Mohammadrezarefaei/nexus-afrr-bidding/main/images/linkedin_nexus_cumulative_revenue.png)

---

## 🧠 Core Pipeline & Methodology

The repository is structured as a complete end-to-end quantitative data pipeline:

* **Data Engineering (`nexus_afrr/`):** Synthesizes market data, extracting temporal features, auto-regressive lags, and rolling statistics to capture seasonality.
* **Machine Learning Model:** Utilizes an `XGBoost Regressor` trained chronologically (80/20 split) to predict short-term capacity clearing prices.
* **Strategic Bidding:** Implements a mathematical markdown strategy to increase auction clearing probability while retaining high margins.
* **Validation (`tests/`):** Includes automated `pytest` suites to strictly verify chronological data splitting and guarantee zero future data leakage.

---

## 💻 Installation & Quick Start

Clone the repository to run the predictive model and revenue simulator locally:

```bash
# 1. Clone the repository
git clone [https://github.com/Mohammadrezarefaei/nexus-afrr-bidding.git](https://github.com/Mohammadrezarefaei/nexus-afrr-bidding.git)
cd nexus-afrr-bidding

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the robust data leakage tests
pytest tests/test_leakage.py -v

# 4. Launch the local Streamlit dashboard
streamlit run dashboard/app.py
