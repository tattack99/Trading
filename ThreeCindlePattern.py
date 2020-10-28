### Tim Johansson
### Three cindle pattern
### 24.10.2020

#Importing nessecasry library
import pandas as pd
import datetime
import yfinance as yf
from pandas_datareader import data as pdr


now_date_hour_min = str(datetime.date.today()) + " "+ str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().hour)
print(now_date_hour_min)

#Getting the data from yahoofinance
EURUSD = yf.Ticker("EURUSD=X")
EURUSD_intra = EURUSD.history(period="1mo",interval="5m")
EURUSD_max = EURUSD.history(period="max",interval="1d")

EURUSD_data_max = pdr.get_data_yahoo("EURUSD=X")
#EURUSD_data_intra = pdr.get_data_yahoo("EURUSD=X")

data = pd.read_csv(r'C:\Users\timmo\Google Drive\1.Trading\1.SampleData\TSLA.CSV')
data_rename = data.rename(columns = str.lower)

data_date_open_close = data_rename[["date" , "open" , "close"]]

data_rename["bull"] = data_date_open_close["open"] - data_date_open_close["close"] > 0

data_rename["bull"].values.tolist()

data_rename.to_excel('clean_data.xlsx', sheet_name='page1', index=False)



