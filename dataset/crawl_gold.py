from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import json
from datetime import datetime

def Crawl_gold():
    # Calculate the date range
    end_date = datetime.now()
    start_date = end_date - pd.DateOffset(months=6)

    # Initialize the WebDriver
    driver = webdriver.Chrome()
    driver.get('https://giavangvietnam.com/bieu-do-gia-vang-sjc-1-nam-truoc/')
    html = driver.page_source

    # Extract data
    data_chart = driver.find_element(By.CLASS_NAME, 'j-data-chart')
    date = data_chart.get_attribute('data-date')
    value = data_chart.get_attribute('data-value')

    # Clean data
    while ",00" in value:
        value = value.replace(",00",",0")
    buy = json.loads(value)['buy']
    sell = json.loads(value)['sell']
    date = json.loads(date)
    for i in range(len(buy) - 1, -1, -1):
        if ((buy[i] == 0) or (sell[i]==0)):
            del buy[i]
            del sell[i]
            del date[i]

    # Create DataFrame
    df = pd.DataFrame({'Date': date, 'Buying_price': buy, 'Selling_price': sell})
    df['Date'] = pd.to_datetime(df['Date'])
    df.sort_values(by=['Date'], ascending=True, inplace=True)

    # Filter the data based on date range
    cond = (df['Date'] >= start_date) & (df['Date'] <= end_date)
    gold_price = df.loc[cond]
    gold_price.reset_index(drop=True, inplace=True)

    # Close the WebDriver
    driver.quit()

    gold_price['Date'] = pd.to_datetime(gold_price['Date']).dt.date
    gold_price = gold_price.drop_duplicates(subset='Date', keep='last')

    return gold_price
