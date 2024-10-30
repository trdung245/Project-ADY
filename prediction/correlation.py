import pandas as pd

df = pd.read_csv('/Users/trdung/Documents/Project-ADY/price.csv')

df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')

buying_correlation = df['Buying_price'].corr(df['USD to VND'])
print(f'Correlation between the buying price of gold and USD: {buying_correlation}')
selling_correlation = df['Selling_price'].corr(df['USD to VND'])
print(f'Correlation between the selling price of gold and USD: {selling_correlation}')