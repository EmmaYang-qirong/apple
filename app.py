import streamlit as st
import requests
import time

def fetch_live_stock_price(symbol, api_key):
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    price = data['Global Quote']['05. price']
    return float(price)

def main():
    st.title('Live Apple Stock Price')
    
    symbol = 'AAPL'
    api_key = 'HACEOOYV5ZU75PNO'
    
    placeholder = st.empty()
    
    while True:
        live_price = fetch_live_stock_price(symbol, api_key)
        placeholder.metric(label="Apple Stock Price", value=f"${live_price}")
        time.sleep(60)  # Refresh every 60 seconds

if __name__ == "__main__":
    main()

