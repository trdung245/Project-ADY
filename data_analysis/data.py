import pandas as pd

df = pd.read_csv('/Users/trdung/Documents/Project-ADY/price.csv', sep = ';')

df['Gold Price (VND)'] = df['Gold price (per ounce)'] * df['USDtoVND']
df['Date'] = pd.to_datetime(df['Date'], format = '%d/%m/%y')

