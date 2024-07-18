import time 
from flask import Flask, render_template, jsonify, request 
import plotly.graph_objs as go 
import akshare as ak 
from plotly.subplots import make_subplots 
import datetime 

app = Flask(__name__)

end_date = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%Y%m%d')

def get_data(symbol, interval):
    try:
        df = ak.stock_us_hist(symbol=str(symbol), period=str(interval), start_date="20240101", end_date=end_date, adjust="qfq")
        df = df.sort_values(by='日期')
        time.sleep(0.2)
        return df
    except Exception as e:
        print(f"Exception occurred while fetching data for {symbol}: {str(e)}")
        return None

@app.route('/create_plot', methods=['GET'])
def create_plot():
    symbol = request.args.get('symbol', '105.AAPL')
    interval = request.args.get('interval', 'daily')
    print(symbol, interval)
    df = get_data(symbol, interval)

    if df is None:
        return jsonify({"error": "Data fetching failed"})

    x_values = df['日期'].tolist()
    close_line = df['收盘'].tolist()
    open_line = df['开盘'].tolist()
    high_line = df['最高'].tolist()
    low_line = df['最低'].tolist()
    volumes = df['成交量'].tolist()
    #定义一个画图fig,
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                        vertical_spacing=0.02,
                        row_heights=[0.7, 0.3],)
  
    fig.add_trace(go.Candlestick(x=x_values,
                                 open=open_line,
                                 high=high_line,
                                 low=low_line,
                                 close=close_line), row=1, col=1)
  
    fig.add_trace(go.Bar(x=x_values, y=volumes, opacity=0.7, name='Volume'),
                  row=2, col=1)

    fig.update_layout(
        title=f'{symbol}',
        title_x=0.5,
        xaxis_title='dates',
        yaxis_title='price',
        paper_bgcolor='rgba(255, 255, 255, 1)',
        plot_bgcolor='rgba(255, 255, 255, 1)',
        margin=dict(l=50, r=50, b=50, t=80),
        xaxis=dict(showline=True, linewidth=2, linecolor='black'),
        # yaxis=dict(showline=True, linewidth=2, linecolor='black'),
        height=1100,  
        width=2000,  
    )
    fig.update_layout(xaxis_rangeslider_visible=False)  

    fig.update_xaxes(type='category')

    plot_json = fig.to_json()
    time.sleep(0.005)

    return plot_json

@app.route('/')
def index():
    return render_template('plot.html')

if __name__ == "__main__":
    app.run(debug=True)



