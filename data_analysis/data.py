import pandas as pd

df = pd.read_csv('/Users/trdung/Documents/Project-ADY/price.csv')

df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')

