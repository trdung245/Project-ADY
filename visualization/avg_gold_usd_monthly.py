import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('/Users/trdung/Documents/Project-ADY/price.csv', sep = ';')

df['Gold Price (VND)'] = df['Gold price (per ounce)'] * df['USDtoVND']
df['Date'] = pd.to_datetime(df['Date'], format = '%d/%m/%y')

df['Year-Month'] = df['Date'].dt.to_period('M')
monthly_avg = df.groupby('Year-Month').agg({
    'Gold Price (VND)': 'mean',
    'USDtoVND': 'mean'
}).reset_index()

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Plotting the bar graph for USD Price
axs[0].bar(monthly_avg.index, monthly_avg['USDtoVND'], color='blue', width=0.4)
axs[0].set_xlabel('Month')
axs[0].set_ylabel('USD Price (VND)')
axs[0].set_title('Average USD Price in VND (April to October)')
axs[0].set_xticks(monthly_avg.index)
axs[0].set_xticklabels(['April', 'May', 'June', 'July', 'August', 'September', 'October'])

# Plotting the bar graph for Gold Price
axs[1].bar(monthly_avg.index, monthly_avg['Gold Price (VND)'], color='gold', width=0.4)
axs[1].set_xlabel('Month')
axs[1].set_ylabel('Gold Price (VND)')
axs[1].set_title('Average Gold Price in VND (April to October)')
axs[1].set_xticks(monthly_avg.index)
axs[1].set_xticklabels(['April', 'May', 'June', 'July', 'August', 'September', 'October'])

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()