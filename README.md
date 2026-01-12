# 💼 Financial Statement Analysis Dashboard

A comprehensive Streamlit web application for analyzing company financial statements, calculating key ratios, identifying trends, and comparing peer performance.

## 🌟 Features

### 📊 **Financial Statement Analysis**
- **Income Statement**: Revenue trends, profit margins, operating performance
- **Balance Sheet**: Assets, liabilities, equity analysis over time
- **Cash Flow**: Operating, investing, and financing cash flows

### 📈 **Ratio Analysis**
- **Profitability Ratios**: Net Profit Margin, ROA, ROE, Operating Margin
- **Liquidity Ratios**: Current Ratio, Quick Ratio, Cash Ratio
- **Leverage Ratios**: Debt-to-Equity, Debt-to-Assets, Equity Multiplier
- **Efficiency Ratios**: Asset Turnover

### 📉 **Trend Analysis**
- Year-over-year growth rates
- Multi-year performance trends
- Visual trend identification

### 🔄 **Peer Comparison**
- Compare multiple companies side-by-side
- Industry benchmarking
- Competitive position analysis

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Install required packages:**
```bash
pip install -r requirements_fs.txt
```

### Running the Dashboard

```bash
streamlit run financial_statement_dashboard.py
```

The dashboard will open automatically in your browser at `http://localhost:8501`

## 📖 How to Use

### Basic Analysis
1. **Enter Stock Ticker**: Type any publicly traded company ticker (e.g., AAPL, MSFT, JPM)
2. **Select Analysis Period**: Choose 1-5 years of historical data
3. **Explore Tabs**: Navigate through different financial statement views

### Peer Comparison
1. Enter main company ticker
2. Add peer tickers in sidebar (comma-separated): `MSFT, GOOGL, META`
3. View side-by-side comparison in the "Peer Comparison" tab

### Example Companies to Analyze

**Technology:**
- Apple (AAPL)
- Microsoft (MSFT)
- Google (GOOGL)
- Amazon (AMZN)

**Finance:**
- JPMorgan Chase (JPM)
- Bank of America (BAC)
- Wells Fargo (WFC)
- Goldman Sachs (GS)

**Retail:**
- Walmart (WMT)
- Target (TGT)
- Costco (COST)
- Home Depot (HD)

**Consumer Goods:**
- Procter & Gamble (PG)
- Coca-Cola (KO)
- PepsiCo (PEP)
- Nike (NKE)

## 📊 Understanding the Ratios

### Profitability Ratios

**Net Profit Margin**
- Formula: Net Income / Revenue × 100
- Interpretation: Higher is better (shows efficiency in generating profit)
- Good: >10%, Excellent: >20%

**Return on Assets (ROA)**
- Formula: Net Income / Total Assets × 100
- Interpretation: Efficiency in using assets to generate profit
- Good: >5%, Excellent: >10%

**Return on Equity (ROE)**
- Formula: Net Income / Shareholder Equity × 100
- Interpretation: Return generated for shareholders
- Good: >10%, Excellent: >15-20%

### Liquidity Ratios

**Current Ratio**
- Formula: Current Assets / Current Liabilities
- Interpretation: Ability to pay short-term obligations
- Good: >1.5, Adequate: >1.0

**Quick Ratio**
- Formula: (Current Assets - Inventory) / Current Liabilities
- Interpretation: Immediate liquidity (excluding inventory)
- Good: >1.0

### Leverage Ratios

**Debt to Equity**
- Formula: Total Debt / Shareholder Equity
- Interpretation: Financial leverage and risk
- Conservative: <1.0, Moderate: 1.0-2.0, High: >2.0

**Debt to Assets**
- Formula: Total Debt / Total Assets
- Interpretation: Percentage of assets financed by debt
- Good: <0.5 (50%)

## 💡 Analysis Tips

### For Growth Companies
- Focus on revenue growth trends
- Watch operating margin expansion
- Monitor cash flow from operations

### For Value Companies
- Look for strong ROE and ROA
- Check debt levels (lower is better)
- Analyze dividend sustainability

### For Cyclical Companies
- Compare ratios across business cycles
- Focus on liquidity during downturns
- Monitor debt levels carefully

### Red Flags to Watch
- ⚠️ Declining revenue over multiple years
- ⚠️ Negative cash flow from operations
- ⚠️ Current ratio < 1.0
- ⚠️ Increasing debt-to-equity ratio
- ⚠️ Declining profit margins

### Positive Signals
- ✅ Consistent revenue growth
- ✅ Improving profit margins
- ✅ Strong and growing cash flows
- ✅ Decreasing debt levels
- ✅ ROE > 15%

## 🎯 Use Cases

### Investment Analysis
- Evaluate potential stock purchases
- Compare investment alternatives
- Identify undervalued companies

### Academic Projects
- Financial statement analysis assignments
- Corporate finance case studies
- Investment analysis presentations

### Professional Development
- Practice ratio calculations
- Learn financial analysis
- Build portfolio projects

### Business Analysis
- Competitive analysis
- Industry benchmarking
- Company valuation preparation

## 🛠️ Technical Stack

- **Streamlit**: Interactive web framework
- **yfinance**: Real-time financial data API
- **Plotly**: Interactive data visualizations
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations

## 📝 Data Source

Financial data is sourced from **Yahoo Finance** via the yfinance API, providing:
- Income statements (annual)
- Balance sheets (annual)
- Cash flow statements (annual)
- Company information and metrics

**Data Limitations:**
- Annual data only (not quarterly)
- Historical data may be limited for some companies
- Data accuracy depends on Yahoo Finance
- Some companies may have incomplete data

## 🎓 Skills Demonstrated

This project showcases:
- ✅ Financial statement analysis
- ✅ Ratio calculation and interpretation
- ✅ Data visualization
- ✅ Python programming (Pandas, NumPy)
- ✅ Web application development (Streamlit)
- ✅ API integration (yfinance)
- ✅ Business analytics and insights

## 🚀 Deployment

### Deploy on Streamlit Cloud

1. **Push to GitHub:**
```bash
git init
git add .
git commit -m "Financial statement analysis dashboard"
git remote add origin YOUR_REPO_URL
git push -u origin main
```

2. **Deploy:**
- Go to [share.streamlit.io](https://share.streamlit.io)
- Connect your GitHub repository
- Select `financial_statement_dashboard.py` as main file
- Deploy!

## 📊 Example Analysis Workflow

1. **Start with Overview**
   - Review company info (sector, industry, market cap)
   - Get familiar with the business

2. **Analyze Income Statement**
   - Check revenue trends (growing or declining?)
   - Examine profit margins
   - Look at operating income

3. **Review Balance Sheet**
   - Assess asset composition
   - Evaluate debt levels
   - Check equity trends

4. **Examine Cash Flows**
   - Operating cash flow positive?
   - Capital expenditure trends
   - Free cash flow generation

5. **Calculate & Interpret Ratios**
   - Compare to industry averages
   - Look for trends over time
   - Identify strengths and weaknesses

6. **Peer Comparison**
   - How does the company stack up?
   - Competitive advantages/disadvantages
   - Industry position

## ⚠️ Disclaimer

This dashboard is for **educational and analytical purposes only**. It is not financial advice. Always conduct thorough research and consult with financial professionals before making investment decisions.

## 🤝 Contributing

Suggestions for improvements:
- Additional financial ratios
- Quarterly data support
- Export functionality (PDF/Excel)
- More advanced visualizations
- Industry-specific metrics

## 📫 Contact

Built as part of a business analytics portfolio project demonstrating financial analysis and data visualization skills.

---

**💼 Perfect for:** Finance students, aspiring analysts, investment enthusiasts, and anyone learning financial statement analysis!
