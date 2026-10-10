# CodeAlpha - Task 2: Stock Portfolio Tracker

A Python console application to track and manage personal stock investments, calculate portfolio valuation, and analyze real-time profit and loss metrics. Developed for the **CodeAlpha Python Programming Internship**.

---

## 📌 Features
- **Portfolio Management**: Add new stock purchases with share quantity and buy price.
- **Average Cost Calculation**: Automatically calculates weighted average buy price when purchasing more shares of an existing stock.
- **Sell / Remove Stocks**: Sell partial shares or entire holdings.
- **Valuation & Metrics**: Computes invested capital, current market value, net profit/loss, and percentage return.
- **Data Persistence**: Saves and loads portfolio data automatically using JSON (`portfolio.json`).

---

## 🛠️ Concepts & Libraries
- **Language**: Python 3
- **File Handling & Persistence**: `json` and `os` module for data storage.
- **Data Structures**: Nested dictionaries, lists, and tuples.
- **Formatting**: Tabular data formatting using f-strings.
- **Error Handling**: `try-except` blocks for graceful input validation.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed.

### Setup and Execution
1. Clone the repository:
   ```bash
   git clone https://github.com/<YOUR_USERNAME>/CodeAlpha_StockPortfolioTracker.git
   ```
2. Navigate to project directory:
   ```bash
   cd CodeAlpha_StockPortfolioTracker
   ```
3. Run the application:
   ```bash
   python portfolio_tracker.py
   ```

---

## 📋 Sample Output
```text
===========================================================================
                      YOUR STOCK PORTFOLIO SUMMARY                     
===========================================================================
Symbol   Shares   Buy Price    Curr Price   Invested     Current Val  P/L ($)   
---------------------------------------------------------------------------
AAPL     10       $170.00      $180.50      $1700.00     $1805.00     +$105.00  
TSLA     5        $220.00      $210.00      $1100.00     $1050.00     -$50.00   
---------------------------------------------------------------------------
Total Invested Capital : $2800.00
Total Current Value    : $2855.00
Total Profit / Loss    : +$55.00 (+1.96%) [PROFIT]
===========================================================================
```

---

## 👤 Author
- **Author**: Vidhi
- **Internship**: Python Programming Internship at **CodeAlpha**
- **Website**: [CodeAlpha](https://www.codealpha.tech)
