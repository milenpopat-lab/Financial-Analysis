# Financial Statement Analysis Dashboard

Comprehensive financial statement analyzer with ratio calculations, trend analysis, and peer comparison.

## Features

**Financial Statements**
- Income statement analysis
- Balance sheet evaluation
- Cash flow statement review
- Multi-year historical data

**Ratio Analysis**
- Profitability: Net Margin, ROE, ROA, Operating Margin
- Liquidity: Current Ratio, Quick Ratio, Cash Ratio
- Leverage: Debt-to-Equity, Debt-to-Assets, Equity Multiplier
- Efficiency: Asset Turnover

**Trend Analysis**
- Year-over-year growth rates
- Multi-year performance trends
- Revenue and profit margin evolution
- Visual trend identification

**Peer Comparison**
- Side-by-side company analysis
- Industry benchmarking
- Competitive positioning
- Multi-company ratio comparison

**Visualizations**
- Interactive charts (Plotly)
- Radar plots for ratio comparison
- Waterfall diagrams for cash flow
- Bar charts for financial metrics

## Tech Stack

- Python 3.8+
- Streamlit - Web framework
- yfinance - Financial data API
- Plotly - Interactive charts
- Pandas - Data analysis
- NumPy - Calculations

## Installation

```bash
pip install -r requirements.txt
streamlit run financial_statement_dashboard.py
```

## Usage

**Basic Analysis**
1. Enter stock ticker (e.g., AAPL, MSFT, JPM)
2. Select analysis period (1-5 years)
3. Navigate through tabs for different views

**Peer Comparison**
1. Enter main company ticker
2. Add peer tickers (comma-separated)
3. View comparison in Peer Comparison tab

## Example Companies

**Technology:** AAPL, MSFT, GOOGL, AMZN
**Finance:** JPM, BAC, WFC, GS
**Retail:** WMT, TGT, COST, HD
**Consumer:** PG, KO, PEP, NKE

## Ratio Interpretations

**Current Ratio**
- Good: >1.5
- Adequate: >1.0
- Concerning: <1.0

**Debt to Equity**
- Conservative: <1.0
- Moderate: 1.0-2.0
- High: >2.0

**ROE (Return on Equity)**
- Good: >10%
- Excellent: >15-20%

**Net Profit Margin**
- Good: >10%
- Excellent: >20%

## Key Features

**Automatic Calculations**
- 13+ financial ratios
- Growth rate computations
- Multi-year averages
- Trend extrapolations

**Color-Coded Indicators**
- Green: Strong performance
- Yellow: Adequate performance
- Red: Potential concerns

**Interactive Elements**
- Adjustable time periods
- Dynamic peer selection
- Expandable visualizations
- Downloadable data views

## File Structure

```
financial-statement-analysis/
├── financial_statement_dashboard.py    # Main application
├── requirements.txt                    # Dependencies
└── README.md                          # Documentation
```

## Live Demo

https://financial-analysis-m11126.streamlit.app/

## Data Source

Yahoo Finance via yfinance library. Annual financial statements with automatic updates.

## Requirements

```
streamlit>=1.28.0
yfinance>=0.2.28
pandas>=2.0.0
plotly>=5.17.0
numpy>=1.24.0
openpyxl>=3.1.0
```

## Deployment

Deploy to Streamlit Cloud:
1. Push code to GitHub
2. Connect at share.streamlit.io
3. Select financial_statement_dashboard.py
4. Deploy

## Data Limitations

- Annual data only
- Historical availability varies by company
- Dependent on Yahoo Finance accuracy
- Some companies may have incomplete data

## Use Cases

- Investment analysis
- Company valuation
- Competitive research
- Academic projects
- Portfolio screening
- Financial education
