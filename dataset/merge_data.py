import pandas as pd

gold_price_df = pd.read_csv("/Users/trdung/Documents/Project-ADY/gold_price.csv")
vnd_price_df = pd.read_csv("/Users/trdung/Documents/Project-ADY/vnd_price.csv")

vnd_price_df = vnd_price_df[vnd_price_df['Date'].isin(gold_price_df['Date'])]

merged_df = gold_price_df.merge(vnd_price_df, how = 'inner', on = 'Date')

merged_df.to_csv('test.csv', index = False)