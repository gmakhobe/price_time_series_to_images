import csv
import matplotlib.pyplot as plt
import pandas as pd
import json
import mplfinance as mpf

data = pd.read_csv("price_data_eurusd_2020-2024.csv")

open = []
close = []
high = []
low = []
for index, row in data.iterrows():
  open.append(row['Open'])
  close.append(row['Close'])
  high.append(row['High'])
  low.append(row['Low'])

data['Date'] = pd.to_datetime(data['Date'])
priceInformation = pd.DataFrame({
  "Open": open,
  "Close": close,
  "High": high,
  "Low": low}, index=data['Date'])

testDataFrame = priceInformation.loc['2020-03-26 22:00:00':'2020-03-27 22:00:00',:]
#print(testDataFrame)

mpf.plot(testDataFrame,type='candle', axisoff=True)
mpf.figure

plt.savefig('my_candlestick_chart.png') 

{"content": "gs://sourcebucket/datasets/images/source_image.jpg", "mimeType": "image/jpeg"}