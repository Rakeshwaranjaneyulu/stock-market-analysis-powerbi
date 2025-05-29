# Stock Market Analysis Project 📈

This project uses Power BI and Python to perform ETL (Extract, Transform, Load) and visualize insights from stock market data. It tracks trends, volume, volatility, and investment performance over time for major companies.

## 📊 Dashboards Overview

### 1. **Stock Price Trend Dashboard**
- **Visual**: Area Chart
- **Data**: Sum of Close price over time by ticker
- **Purpose**: Analyze stock closing price trends over time.

### 2. **Volume Traded Comparison**
- **Visuals**: 
  - Horizontal Bar Chart (Sum of Volume by Ticker)
  - Alternative: Count of Volume per ticker for frequency comparison
- **Purpose**: Identify stocks with higher trading activity.

### 3. **High vs. Low Price Range**
- **Visual**: Clustered Bar Chart
- **Data**: Sum of High vs Sum of Low price by Ticker
- **Purpose**: Compare price fluctuation range per stock.

### 4. **Investment Growth Over Time by Ticker**
- **Visual**: Line Chart
- **DAX Measures**: 
  - `Initial_Investment` (e.g. ₹1,00,000)
  - `Investment_Value` = Average Current Price / First Price × Initial Investment
- **Purpose**: Show hypothetical investment value growth over years.

### 5. **Price Volatility Tracker**
- **Visual**: Bar Chart
- **Measure**: `(High - Low) / Low`
- **Slicer**: Date-wise comparison
- **Purpose**: Identify which stock had the highest % price fluctuation daily.

### 6. **Moving Averages Comparison**
- **Visual**: Line Chart with Ticker filter
- **Measures**:
  - 7-Day Moving Average
  - 30-Day Moving Average
- **Purpose**: Detect short-term and long-term price trends for signals.

---

## ⚙️ Tech Stack
- **Power BI**
- **Python (yfinance, pandas)**
- **Git & GitHub**
- **VS Code**

## 📁 Project Structure

```
├── Dashboards.pbix               # Power BI file
├── fetch_data.py                 # Python ETL script
├── final_stock_data.csv          # Final dataset
├── output/                       # Contains raw stock CSVs
├── README.md                     # Project description
```

---

## 🚀 How to Run This Project

1. Clone the repo:
    ```bash
    git clone https://github.com/rakeshwaranjaneyulu/stock-market-analysis-powerbi.git
    ```

2. Run Python ETL:
    ```bash
    python fetch_data.py
    ```

3. Open `Dashboards.pbix` in Power BI to explore dashboards.

---

## 📌 Insights Gained
- TSLA had the highest volatility on several days.
- AAPL showed consistent long-term growth.
- Volume traded varied significantly between companies.

---

## 🙌 Credits
Created by Rakesh Waranjaneyulu using real-time stock data.
