import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/trdung/Documents/Project-ADY/price.csv', sep = ';')

df['Gold Price (VND)'] = df['Gold price (per ounce)'] * df['USDtoVND']
df['Date'] = pd.to_datetime(df['Date'], format = '%d/%m/%y')

# Create subplots
fig, axs = plt.subplots(2, 1, figsize=(10, 10))

# Plotting the line chart for USD Price
axs[0].plot(df['Date'], df['USDtoVND'], marker='o', color='blue')
axs[0].set_title('USD Price in VND (April to October)')
axs[0].set_xlabel('Date')
axs[0].set_ylabel('Price in VND')
axs[0].tick_params(axis='x', rotation=45)

# Plotting the line chart for Gold Price
axs[1].plot(df['Date'], df['Gold Price (VND)'], marker='o', color='gold')
axs[1].set_title('Gold Price in VND (April to October)')
axs[1].set_xlabel('Date')
axs[1].set_ylabel('Price in VND')
axs[1].tick_params(axis='x', rotation=45)

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()
