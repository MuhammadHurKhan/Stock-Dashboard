#Importing dependencies 
import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.express as px
from alpha_vantage.fundamentaldata import FundamentalData
from stocknews import StockNews

#Designing Streamlit Webapplication
st.title("Stock Dashboard ")
st.subheader("This app helps you track your favourite stocks. Also provide latest NEWS to for better investing decisions")
ticker=st.sidebar.text_input('Write Ticker of your favourite stock:')
start_date=st.sidebar.date_input("Select starting date:")
end_date=st.sidebar.date_input("Select ending date:")

#Retrieving the Data
data = yf.download(ticker, start=start_date, end=end_date)

#Plotting Data
fig = px.line(data, x=data.index, y=data['Adj Close'], title = ticker)
st.plotly_chart(fig)

#Creating tabs
price_data, fundamental_data, news = st.tabs(['Price Data', 'Fundamental Data', 'News'])
with price_data:
    st.header('Pricing Movements')
    data2= data
    data2['%Change']= data['Adj Close']/data['Adj Close'].shift(1)
    data2.dropna(inplace=True)
    st.write(data2)
    annual_return = data2['% Change'].mean()*252
    st.subheader('The annual return is', annual_return, "%")
    risk = np.std(data2['% Change'])*np.sqrt(252)
    st.subheader("The annualized risk is", risk, "%")
    st.subheader('The risk adjusted return is ', annual_return/risk, '%')
    
with fundamental_data:
    key = '7VZ1DSZYTKJQ6DME'
    fd = FundamentalData(key, output_format= 'pandas')
    st.subheader('Balance Sheet')
    balance_sheet = fd.get_balance_sheet_annual(ticker)[0]
    bs = balance_sheet.T[2:]
    bs.columns = list(balance_sheet.T.iloc[0])
    st.write(bs)
    st.subhheader('Income Statement')
    income_statement = fd.get_income_statement_annual(ticker)[0]
    is1 = income_statement.T[2:]
    isl.columns = list(income_statement.T.iloc[0])
    st.write(is1)
    st.subheader('Cashflow Statement')
    cash_flow = fd.get_cash_flow_annual(ticker)[0]
    cf = cash_flow.T[2:]
    cf.columns = list(cash_flow.T.iloc[0])
    st.write(cf)
    
    
with news:
    st.header("Latest NEWS for {ticker}")
    sn = StockNews(ticker, save_news=False)
    df_news = sn.read_rss()
    for i in range(10):
        st.subheader(f'News{i+1}')
        st.write(df_news['published'][i])
        st.write(df_news['title'][i])
        st.write(df_news['summary'][i])
        title_sentiment = df_news['sentiment_title'][i]
        st.write(f'Title Sentiment{title_sentiment}')
        news_sentiment = df_news['sentiment_summary'][i]
        st.write(f'News Sentiment {news_sentiment}')
        
        
