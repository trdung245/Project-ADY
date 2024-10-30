import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('/Users/trdung/Documents/Project-ADY/price.csv')

df['Date'] = pd.to_datetime(df['Date'], format = '%Y-%m-%d')

df['Year-Month'] = df['Date'].dt.to_period('M')
monthly_avg = df.groupby('Year-Month').agg({
    'Buying_price': 'mean',
    'Selling_price': 'mean',
    'USD to VND': 'mean'
}).reset_index()

# Create subplots
fig, axs = plt.subplots(1, 3, figsize=(14, 6))

# Plotting the bar graph for USD Price
axs[0].bar(monthly_avg.index, monthly_avg['USD to VND'], color='blue', width=0.4)
axs[0].set_xlabel('Month')
axs[0].set_ylabel('USD to VND')
axs[0].set_title('Average USD Price in VND (May to October)')
axs[0].set_xticks(monthly_avg.index)
axs[0].set_xticklabels(['May', 'June', 'July', 'August', 'September', 'October'])

# Plotting the bar graph for Gold Price
axs[1].bar(monthly_avg.index, monthly_avg['Buying_price'], color='gold', width=0.4)
axs[1].set_xlabel('Month')
axs[1].set_ylabel('Buying Price')
axs[1].set_title('Average Gold Price in VND (May to October)')
axs[1].set_xticks(monthly_avg.index)
axs[1].set_xticklabels(['May', 'June', 'July', 'August', 'September', 'October'])

axs[2].bar(monthly_avg.index, monthly_avg['Selling_price'], color='orange', width=0.4)
axs[2].set_xlabel('Month')
axs[2].set_ylabel('Selling Price')
axs[2].set_title('Average Gold Price in VND (May to October)')
axs[2].set_xticks(monthly_avg.index)
axs[2].set_xticklabels(['May', 'June', 'July', 'August', 'September', 'October'])

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()