import yfinance as yf

net = yf.Ticker("NET")

recommendations = net.recommendations
print(recommendations.tail())