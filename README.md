# Stock Dashboard Web Application
This is a Python web application that allows users to track their favorite stocks and get the latest news for better investing decisions. The application is built with Streamlit, a Python library for building interactive web applications.

# How to Use
To use the application, follow these steps:

Clone the repository to your local machine.
Install the required dependencies listed in the requirements.txt file.
Open the terminal and navigate to the directory where the repository is cloned.
Type streamlit run stock_dashboard.py to run the application.
Enter the ticker symbol of your favorite stock in the sidebar.
Select the start and end date for the stock data you want to retrieve.
View the stock price movements, fundamental data, and news.
# Dependencies
This application uses the following Python libraries:

Streamlit
Pandas
NumPy
yfinance
Plotly Express
alpha_vantage
stocknews
# Features
## Stock Price Movements
The application retrieves stock price data from Yahoo Finance using the yfinance library. It then plots the data using Plotly Express to show the stock's price movements over the selected time period. In addition, the application calculates the annual return, annualized risk, and risk-adjusted return of the stock using the price data.

## Fundamental Data
The application uses the alpha_vantage library to retrieve the balance sheet, income statement, and cash flow statement of the stock from Alpha Vantage. It then displays the data in a table format using Pandas.

## Latest News
The application uses the stocknews library to retrieve the latest news related to the stock. It displays the news in a tabular format and shows the sentiment analysis of the news title and summary.

# Acknowledgments
This application was built using the following resources:

Streamlit Documentation
yfinance Documentation
Plotly Express Documentation
Alpha Vantage Documentation
Stock News Documentation
