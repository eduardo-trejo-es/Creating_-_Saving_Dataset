import pandas as pd
import yfinance as yf


startDate='2022-08-23'
endDate= '2022-08-24'

df=yf.download('TWTR',start = startDate, end = endDate,interval='1m',utc=True,threads = True)