import requests
import csv
import pandas as pd
from datetime import datetime

def Crawl_dollar():
    end_date = datetime.now()
    start_date = end_date - pd.DateOffset(months=6)

    start_date_str = start_date.strftime('%Y-%m-%d')
    end_date_str = end_date.strftime('%Y-%m-%d')

    url = 'http://api.currencylayer.com/timeframe'
    params = {
        'access_key': 'f968cc591b0e7af669b56fdaa5209cba',
        'start_date': start_date_str,
        'end_date': end_date_str,
        'currencies': 'VND',
        'source': 'USD'
    }

    USD_price = pd.DataFrame()

    response = requests.get(url, params=params)
    data = response.json()

    # Check if the request was successful
    if data['success']:
        quotes = data['quotes']

        records = []

        for date, rate in quotes.items():
            records.append({'Date': date, 'USD to VND': rate['USDVND']})

        df = pd.DataFrame(records)
        df.sort_values(by=['Date'], ascending=True, inplace=True)
        cond = (df['Date'] >= start_date_str) & (df['Date'] <= end_date_str)
        USD_price = df.loc[cond]
        USD_price.reset_index(drop=True, inplace=True)

    else:
        print("Error retrieving data:", data['error']['info'])
    
    return USD_price


