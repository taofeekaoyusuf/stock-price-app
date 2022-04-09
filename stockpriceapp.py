import pandas as pd
import streamlit as st
import yfinance as yf

from urllib.error import URLError

st.write(
    """
        # Stock Price for Exxon Mobil

        These are the stock Price Metrics for Exxon Mobil.
    """
)

companyData = []
dataHistory = []


@st.cache
def get_company_data():
    company_stock_ticker_symbols = {
        'Companies': ['Google', 'Apple', 'Exxon Mobil'],
        'Symbols': ['GOOGL', 'AAPL', 'XOM']
    }
    df_company = pd.DataFrame(company_stock_ticker_symbols)
    for _, value in df_company.values:
        companyData.append(yf.Ticker(value))

    for data_ in companyData:
        dataHistory.append(data_.history(
            period='1d', start='2010-5-31', end='2020-5-31'))
    return dataHistory


company_data = get_company_data()

st.write('### Exxon Mobile Data')
st.write(company_data[2])

st.write('### Exxon Mobile Open Stock')
st.line_chart(company_data[2].Open)

st.write('### Exxon Mobile Volume Stock')
st.line_chart(company_data[2].Volume)

st.write('### Exxon Mobile Closing Stock')
st.line_chart(company_data[2].Close)

st.write('### Exxon Mobile High Stock')
st.line_chart(company_data[2].High)

st.write('### Exxon Mobile Low Stock')
st.line_chart(company_data[2].Low)

st.write('### Exxon Mobile Dividends')
st.line_chart(company_data[2].Dividends)

# try:
#     company_data = get_company_data()
#     companies = st.multiselect(
#         "Choose company", list(company_data.index), ["Google", "Apple"]
#     )
#     if not companies:
#         st.error("Please select at least one company.")
#     else:
#         data = company_data.loc[companies]
#         # Visualization also available for Dividends, High, Low, Stock Splits
#         st.write(""" ### Stock Closing Price """, data.sort_index())
#         st.line_chart(data.Open)

#         st.write(""" ### Stock Volume Price """)
#         st.line_chart(data.High)

# except URLError as e:
#     st.error(
#         """
#         **This demo requires internet access.**
#         Connection error: %s
#     """
#         % e.reason
#     )
