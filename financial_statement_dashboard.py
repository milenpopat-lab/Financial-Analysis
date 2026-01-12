import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Financial Statement Analysis Dashboard",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1e40af;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-positive { color: #10b981; font-weight: bold; }
    .metric-negative { color: #ef4444; font-weight: bold; }
    .insight-box {
        background-color: #f0f9ff;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1e40af;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="main-header">💼 Financial Statement Analysis Dashboard</p>', unsafe_allow_html=True)
st.markdown("**Comprehensive ratio analysis, trend evaluation, and peer comparison for informed investment decisions**")
st.markdown("---")

# Sidebar Configuration
with st.sidebar:
    st.header("⚙️ Analysis Configuration")
    
    # Company selection
    st.subheader("Select Company")
    ticker_input = st.text_input(
        "Enter Stock Ticker",
        value="AAPL",
        help="Examples: AAPL, MSFT, JPM, WMT, TSLA"
    ).upper()
    
    # Peer comparison (optional)
    st.subheader("Peer Comparison (Optional)")
    peer_input = st.text_input(
        "Enter Peer Tickers (comma-separated)",
        value="MSFT, GOOGL",
        help="Compare with industry peers"
    )
    peers = [p.strip().upper() for p in peer_input.split(",") if p.strip()]
    
    # Analysis period
    st.subheader("Analysis Settings")
    periods = st.slider("Number of Years", 1, 5, 3)
    
    st.markdown("---")
    st.info("💡 **Tip:** Use quarterly or annual data depending on your analysis needs.")

# Fetch financial data
@st.cache_data(ttl=3600)
def fetch_financial_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        
        # Get financial statements
        income_stmt = stock.financials
        balance_sheet = stock.balance_sheet
        cash_flow = stock.cashflow
        
        return {
            'info': info,
            'income_statement': income_stmt,
            'balance_sheet': balance_sheet,
            'cash_flow': cash_flow,
            'success': True
        }
    except Exception as e:
        return {'success': False, 'error': str(e)}

# Calculate financial ratios
def calculate_ratios(data):
    try:
        bs = data['balance_sheet']
        inc = data['income_statement']
        cf = data['cash_flow']
        
        ratios = {}
        
        # Get most recent column (most recent year)
        if bs.empty or inc.empty:
            return None
            
        latest_bs = bs.iloc[:, 0]
        latest_inc = inc.iloc[:, 0]
        latest_cf = cf.iloc[:, 0] if not cf.empty else None
        
        # Profitability Ratios
        net_income = latest_inc.get('Net Income', 0)
        revenue = latest_inc.get('Total Revenue', 1)
        total_assets = latest_bs.get('Total Assets', 1)
        total_equity = latest_bs.get('Total Stockholder Equity', 1)
        
        ratios['Net Profit Margin'] = (net_income / revenue * 100) if revenue != 0 else 0
        ratios['ROA'] = (net_income / total_assets * 100) if total_assets != 0 else 0
        ratios['ROE'] = (net_income / total_equity * 100) if total_equity != 0 else 0
        
        # Liquidity Ratios
        current_assets = latest_bs.get('Current Assets', 0)
        current_liabilities = latest_bs.get('Current Liabilities', 1)
        cash = latest_bs.get('Cash And Cash Equivalents', 0)
        inventory = latest_bs.get('Inventory', 0)
        
        ratios['Current Ratio'] = current_assets / current_liabilities if current_liabilities != 0 else 0
        ratios['Quick Ratio'] = (current_assets - inventory) / current_liabilities if current_liabilities != 0 else 0
        ratios['Cash Ratio'] = cash / current_liabilities if current_liabilities != 0 else 0
        
        # Leverage Ratios
        total_debt = latest_bs.get('Total Debt', 0)
        total_liabilities = latest_bs.get('Total Liabilities Net Minority Interest', 0)
        
        ratios['Debt to Equity'] = total_debt / total_equity if total_equity != 0 else 0
        ratios['Debt to Assets'] = total_debt / total_assets if total_assets != 0 else 0
        ratios['Equity Multiplier'] = total_assets / total_equity if total_equity != 0 else 0
        
        # Efficiency Ratios
        ratios['Asset Turnover'] = revenue / total_assets if total_assets != 0 else 0
        
        # Operating metrics
        operating_income = latest_inc.get('Operating Income', 0)
        ratios['Operating Margin'] = (operating_income / revenue * 100) if revenue != 0 else 0
        
        return ratios
    except Exception as e:
        st.error(f"Error calculating ratios: {str(e)}")
        return None

# Fetch data
with st.spinner(f"Fetching financial data for {ticker_input}..."):
    company_data = fetch_financial_data(ticker_input)

if not company_data['success']:
    st.error(f"❌ Could not fetch data for {ticker_input}. Please check the ticker symbol and try again.")
    st.stop()

# Company Info Section
st.header(f"📊 {company_data['info'].get('longName', ticker_input)}")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Sector", company_data['info'].get('sector', 'N/A'))
with col2:
    st.metric("Industry", company_data['info'].get('industry', 'N/A'))
with col3:
    market_cap = company_data['info'].get('marketCap', 0)
    st.metric("Market Cap", f"${market_cap/1e9:.2f}B" if market_cap else "N/A")
with col4:
    current_price = company_data['info'].get('currentPrice', 0)
    st.metric("Current Price", f"${current_price:.2f}" if current_price else "N/A")

st.markdown("---")

# Create tabs
tabs = st.tabs([
    "📈 Income Statement",
    "💰 Balance Sheet", 
    "💵 Cash Flow",
    "📊 Ratio Analysis",
    "📉 Trend Analysis",
    "🔄 Peer Comparison"
])

# Tab 1: Income Statement
with tabs[0]:
    st.header("Income Statement Analysis")
    
    inc_stmt = company_data['income_statement']
    
    if not inc_stmt.empty:
        # Display income statement
        st.subheader("Income Statement (Most Recent Years)")
        
        # Select key metrics
        key_metrics = [
            'Total Revenue',
            'Cost Of Revenue',
            'Gross Profit',
            'Operating Income',
            'EBIT',
            'Net Income'
        ]
        
        display_data = []
        for metric in key_metrics:
            if metric in inc_stmt.index:
                row_data = {'Metric': metric}
                for col in inc_stmt.columns[:periods]:
                    year = col.year
                    value = inc_stmt.loc[metric, col]
                    row_data[str(year)] = f"${value/1e9:.2f}B" if value else "N/A"
                display_data.append(row_data)
        
        if display_data:
            df_display = pd.DataFrame(display_data)
            st.dataframe(df_display, use_container_width=True, hide_index=True)
        
        # Revenue and Net Income Chart
        st.subheader("Revenue & Net Income Trend")
        
        fig = go.Figure()
        
        if 'Total Revenue' in inc_stmt.index:
            years = [col.year for col in inc_stmt.columns[:periods]]
            revenue = [inc_stmt.loc['Total Revenue', col]/1e9 for col in inc_stmt.columns[:periods]]
            
            fig.add_trace(go.Bar(
                x=years,
                y=revenue,
                name='Revenue',
                marker_color='#3b82f6'
            ))
        
        if 'Net Income' in inc_stmt.index:
            net_income = [inc_stmt.loc['Net Income', col]/1e9 for col in inc_stmt.columns[:periods]]
            
            fig.add_trace(go.Bar(
                x=years,
                y=net_income,
                name='Net Income',
                marker_color='#10b981'
            ))
        
        fig.update_layout(
            xaxis_title="Year",
            yaxis_title="Amount (Billions USD)",
            template="plotly_white",
            height=400,
            barmode='group'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Margins Analysis
        st.subheader("Profit Margins Over Time")
        
        fig_margins = go.Figure()
        
        for col in inc_stmt.columns[:periods]:
            revenue = inc_stmt.loc['Total Revenue', col] if 'Total Revenue' in inc_stmt.index else 1
            if revenue and revenue != 0:
                gross_margin = (inc_stmt.loc['Gross Profit', col] / revenue * 100) if 'Gross Profit' in inc_stmt.index else 0
                operating_margin = (inc_stmt.loc['Operating Income', col] / revenue * 100) if 'Operating Income' in inc_stmt.index else 0
                net_margin = (inc_stmt.loc['Net Income', col] / revenue * 100) if 'Net Income' in inc_stmt.index else 0
                
                fig_margins.add_trace(go.Bar(
                    name=str(col.year),
                    x=['Gross Margin', 'Operating Margin', 'Net Margin'],
                    y=[gross_margin, operating_margin, net_margin],
                ))
        
        fig_margins.update_layout(
            yaxis_title="Margin (%)",
            template="plotly_white",
            height=400,
            barmode='group'
        )
        
        st.plotly_chart(fig_margins, use_container_width=True)

# Tab 2: Balance Sheet
with tabs[1]:
    st.header("Balance Sheet Analysis")
    
    bs = company_data['balance_sheet']
    
    if not bs.empty:
        st.subheader("Balance Sheet (Most Recent Years)")
        
        key_bs_metrics = [
            'Total Assets',
            'Current Assets',
            'Cash And Cash Equivalents',
            'Total Liabilities Net Minority Interest',
            'Current Liabilities',
            'Total Debt',
            'Total Stockholder Equity'
        ]
        
        display_data = []
        for metric in key_bs_metrics:
            if metric in bs.index:
                row_data = {'Metric': metric}
                for col in bs.columns[:periods]:
                    year = col.year
                    value = bs.loc[metric, col]
                    row_data[str(year)] = f"${value/1e9:.2f}B" if value else "N/A"
                display_data.append(row_data)
        
        if display_data:
            df_display = pd.DataFrame(display_data)
            st.dataframe(df_display, use_container_width=True, hide_index=True)
        
        # Assets vs Liabilities Chart
        st.subheader("Assets vs Liabilities & Equity")
        
        fig_bs = go.Figure()
        
        years = [col.year for col in bs.columns[:periods]]
        
        if 'Total Assets' in bs.index:
            assets = [bs.loc['Total Assets', col]/1e9 for col in bs.columns[:periods]]
            fig_bs.add_trace(go.Bar(name='Total Assets', x=years, y=assets, marker_color='#3b82f6'))
        
        if 'Total Liabilities Net Minority Interest' in bs.index:
            liabilities = [bs.loc['Total Liabilities Net Minority Interest', col]/1e9 for col in bs.columns[:periods]]
            fig_bs.add_trace(go.Bar(name='Total Liabilities', x=years, y=liabilities, marker_color='#ef4444'))
        
        if 'Total Stockholder Equity' in bs.index:
            equity = [bs.loc['Total Stockholder Equity', col]/1e9 for col in bs.columns[:periods]]
            fig_bs.add_trace(go.Bar(name='Stockholder Equity', x=years, y=equity, marker_color='#10b981'))
        
        fig_bs.update_layout(
            xaxis_title="Year",
            yaxis_title="Amount (Billions USD)",
            template="plotly_white",
            height=400,
            barmode='group'
        )
        
        st.plotly_chart(fig_bs, use_container_width=True)

# Tab 3: Cash Flow
with tabs[2]:
    st.header("Cash Flow Analysis")
    
    cf = company_data['cash_flow']
    
    if not cf.empty:
        st.subheader("Cash Flow Statement (Most Recent Years)")
        
        key_cf_metrics = [
            'Operating Cash Flow',
            'Investing Cash Flow',
            'Financing Cash Flow',
            'Free Cash Flow',
            'Capital Expenditure'
        ]
        
        display_data = []
        for metric in key_cf_metrics:
            if metric in cf.index:
                row_data = {'Metric': metric}
                for col in cf.columns[:periods]:
                    year = col.year
                    value = cf.loc[metric, col]
                    row_data[str(year)] = f"${value/1e9:.2f}B" if value else "N/A"
                display_data.append(row_data)
        
        if display_data:
            df_display = pd.DataFrame(display_data)
            st.dataframe(df_display, use_container_width=True, hide_index=True)
        
        # Cash Flow Waterfall
        st.subheader("Cash Flow Components")
        
        fig_cf = go.Figure()
        
        years = [col.year for col in cf.columns[:periods]]
        
        if 'Operating Cash Flow' in cf.index:
            ocf = [cf.loc['Operating Cash Flow', col]/1e9 for col in cf.columns[:periods]]
            fig_cf.add_trace(go.Bar(name='Operating CF', x=years, y=ocf, marker_color='#10b981'))
        
        if 'Investing Cash Flow' in cf.index:
            icf = [cf.loc['Investing Cash Flow', col]/1e9 for col in cf.columns[:periods]]
            fig_cf.add_trace(go.Bar(name='Investing CF', x=years, y=icf, marker_color='#f59e0b'))
        
        if 'Financing Cash Flow' in cf.index:
            fcf_data = [cf.loc['Financing Cash Flow', col]/1e9 for col in cf.columns[:periods]]
            fig_cf.add_trace(go.Bar(name='Financing CF', x=years, y=fcf_data, marker_color='#ef4444'))
        
        fig_cf.update_layout(
            xaxis_title="Year",
            yaxis_title="Cash Flow (Billions USD)",
            template="plotly_white",
            height=400,
            barmode='group'
        )
        
        st.plotly_chart(fig_cf, use_container_width=True)

# Tab 4: Ratio Analysis
with tabs[3]:
    st.header("Financial Ratio Analysis")
    
    ratios = calculate_ratios(company_data)
    
    if ratios:
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.subheader("💰 Profitability Ratios")
            st.metric("Net Profit Margin", f"{ratios['Net Profit Margin']:.2f}%")
            st.metric("Return on Assets (ROA)", f"{ratios['ROA']:.2f}%")
            st.metric("Return on Equity (ROE)", f"{ratios['ROE']:.2f}%")
            st.metric("Operating Margin", f"{ratios['Operating Margin']:.2f}%")
        
        with col2:
            st.subheader("💧 Liquidity Ratios")
            st.metric("Current Ratio", f"{ratios['Current Ratio']:.2f}")
            st.metric("Quick Ratio", f"{ratios['Quick Ratio']:.2f}")
            st.metric("Cash Ratio", f"{ratios['Cash Ratio']:.2f}")
            
            # Interpretation
            if ratios['Current Ratio'] >= 1.5:
                st.success("✅ Strong liquidity position")
            elif ratios['Current Ratio'] >= 1.0:
                st.info("ℹ️ Adequate liquidity")
            else:
                st.warning("⚠️ Potential liquidity concerns")
        
        with col3:
            st.subheader("📊 Leverage Ratios")
            st.metric("Debt to Equity", f"{ratios['Debt to Equity']:.2f}")
            st.metric("Debt to Assets", f"{ratios['Debt to Assets']:.2f}")
            st.metric("Equity Multiplier", f"{ratios['Equity Multiplier']:.2f}")
            
            # Interpretation
            if ratios['Debt to Equity'] <= 1.0:
                st.success("✅ Conservative leverage")
            elif ratios['Debt to Equity'] <= 2.0:
                st.info("ℹ️ Moderate leverage")
            else:
                st.warning("⚠️ High leverage - increased risk")
        
        st.markdown("---")
        
        # Efficiency
        st.subheader("⚡ Efficiency Ratios")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Asset Turnover", f"{ratios['Asset Turnover']:.2f}x")
        
        # Ratio visualization
        st.subheader("Ratio Comparison Chart")
        
        # Normalize ratios for comparison (convert to 0-100 scale)
        normalized_ratios = {
            'ROE': min(ratios['ROE'], 50) / 50 * 100,
            'ROA': min(ratios['ROA'], 25) / 25 * 100,
            'Current Ratio': min(ratios['Current Ratio'], 3) / 3 * 100,
            'Debt/Equity': max(0, 100 - (ratios['Debt to Equity'] / 2 * 100)),
        }
        
        fig_radar = go.Figure()
        
        fig_radar.add_trace(go.Scatterpolar(
            r=list(normalized_ratios.values()),
            theta=list(normalized_ratios.keys()),
            fill='toself',
            name=ticker_input
        ))
        
        fig_radar.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            showlegend=True,
            height=500
        )
        
        st.plotly_chart(fig_radar, use_container_width=True)

# Tab 5: Trend Analysis
with tabs[4]:
    st.header("Trend Analysis")
    
    st.subheader("Key Metrics Growth Over Time")
    
    # Calculate growth rates
    inc_stmt = company_data['income_statement']
    bs = company_data['balance_sheet']
    
    if not inc_stmt.empty and len(inc_stmt.columns) >= 2:
        years = [col.year for col in inc_stmt.columns[:periods]]
        
        # Revenue growth
        if 'Total Revenue' in inc_stmt.index:
            revenue_values = [inc_stmt.loc['Total Revenue', col] for col in inc_stmt.columns[:periods]]
            revenue_growth = [(revenue_values[i] - revenue_values[i+1]) / revenue_values[i+1] * 100 
                             if i < len(revenue_values)-1 else 0 for i in range(len(revenue_values))]
            
            fig_growth = go.Figure()
            fig_growth.add_trace(go.Bar(
                x=years[:-1],
                y=revenue_growth[:-1],
                name='Revenue Growth',
                marker_color=['#10b981' if g > 0 else '#ef4444' for g in revenue_growth[:-1]]
            ))
            
            fig_growth.update_layout(
                title="Year-over-Year Revenue Growth",
                xaxis_title="Year",
                yaxis_title="Growth Rate (%)",
                template="plotly_white",
                height=400
            )
            
            st.plotly_chart(fig_growth, use_container_width=True)
        
        # Net Income trend
        if 'Net Income' in inc_stmt.index:
            net_income_values = [inc_stmt.loc['Net Income', col]/1e9 for col in inc_stmt.columns[:periods]]
            
            fig_ni = go.Figure()
            fig_ni.add_trace(go.Scatter(
                x=years,
                y=net_income_values,
                mode='lines+markers',
                name='Net Income',
                line=dict(color='#3b82f6', width=3),
                marker=dict(size=10)
            ))
            
            fig_ni.update_layout(
                title="Net Income Trend",
                xaxis_title="Year",
                yaxis_title="Net Income (Billions USD)",
                template="plotly_white",
                height=400
            )
            
            st.plotly_chart(fig_ni, use_container_width=True)

# Tab 6: Peer Comparison
with tabs[5]:
    st.header("Peer Comparison")
    
    if peers:
        st.subheader(f"Comparing {ticker_input} with Industry Peers")
        
        # Fetch peer data
        peer_ratios = {}
        peer_ratios[ticker_input] = calculate_ratios(company_data)
        
        with st.spinner("Fetching peer company data..."):
            for peer in peers:
                peer_data = fetch_financial_data(peer)
                if peer_data['success']:
                    peer_ratios[peer] = calculate_ratios(peer_data)
        
        if len(peer_ratios) > 1:
            # Create comparison dataframe
            comparison_data = []
            
            key_ratios = ['Net Profit Margin', 'ROE', 'ROA', 'Current Ratio', 'Debt to Equity']
            
            for ratio_name in key_ratios:
                row = {'Ratio': ratio_name}
                for company, ratios in peer_ratios.items():
                    if ratios:
                        row[company] = f"{ratios[ratio_name]:.2f}"
                comparison_data.append(row)
            
            df_comparison = pd.DataFrame(comparison_data)
            st.dataframe(df_comparison, use_container_width=True, hide_index=True)
            
            # Visual comparison
            st.subheader("Visual Comparison")
            
            # ROE Comparison
            fig_peer = go.Figure()
            
            companies = list(peer_ratios.keys())
            roe_values = [peer_ratios[c]['ROE'] for c in companies if peer_ratios[c]]
            
            fig_peer.add_trace(go.Bar(
                x=companies,
                y=roe_values,
                marker_color=['#3b82f6' if c == ticker_input else '#94a3b8' for c in companies]
            ))
            
            fig_peer.update_layout(
                title="Return on Equity (ROE) Comparison",
                xaxis_title="Company",
                yaxis_title="ROE (%)",
                template="plotly_white",
                height=400
            )
            
            st.plotly_chart(fig_peer, use_container_width=True)
    else:
        st.info("💡 Enter peer tickers in the sidebar to enable comparison analysis.")

# Footer with insights
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>💡 Built with Streamlit | Data source: Yahoo Finance (yfinance)</p>
        <p>⚠️ This dashboard is for educational and analytical purposes only. Not financial advice.</p>
        <p><strong>📊 Key Insights:</strong> Use ratio analysis to evaluate company performance, 
        compare with peers, and identify trends over time.</p>
    </div>
""", unsafe_allow_html=True)
