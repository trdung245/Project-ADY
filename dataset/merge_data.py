import pandas as pd

gold_price_df = pd.read_csv('/Users/trdung/Documents/Project-ADY/cleaned_gold_prices.csv')
vnd_price_df = pd.read_csv('/Users/trdung/Documents/Project-ADY/usd_to_vnd_6_months_ago.csv')


merged_df = pd.merge(gold_price_df, vnd_price_df, on='Date', how='inner')
merged_df.to_csv('price.csv', index = False)