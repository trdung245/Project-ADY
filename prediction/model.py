import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('/Users/trdung/Documents/Project-ADY/price.csv', sep = ';')

df['Gold Price (VND)'] = df['Gold price (per ounce)'] * df['USDtoVND']
df['Date'] = pd.to_datetime(df['Date'], format = '%d/%m/%y')

# Prepare the data for regression
df['date_numeric'] = (df['Date'] - df['Date'].min()).dt.days  # Convert dates to numerical values

# Separate features and target variables for USD price
X_usd = df[['date_numeric']]
y_usd = df['USDtoVND']

# Train the model for USD price
model_usd = LinearRegression()
model_usd.fit(X_usd, y_usd)

# Predicting USD prices
df['predicted_usd'] = model_usd.predict(X_usd)

# Separate features and target variables for gold price
y_gold = df['Gold Price (VND)']

# Train the model for gold price
model_gold = LinearRegression()
model_gold.fit(X_usd, y_gold)

# Predicting gold prices
df['predicted_gold'] = model_gold.predict(X_usd)

# Plotting the actual vs predicted prices
plt.figure(figsize=(12, 10))

# USD Price plot
plt.subplot(2, 1, 1)
plt.plot(df['Date'], df['USDtoVND'], marker='o', label='Actual USD Price', color='blue')
plt.plot(df['Date'], df['predicted_usd'], linestyle='--', label='Predicted USD Price', color='lightblue')
plt.title('Actual vs Predicted USD Price in VND')
plt.xlabel('Date')
plt.ylabel('Price in VND')
plt.xticks(rotation=45)
plt.legend()

# Gold Price plot
plt.subplot(2, 1, 2)
plt.plot(df['Date'], df['Gold Price (VND)'], marker='o', label='Actual Gold Price', color='gold')
plt.plot(df['Date'], df['predicted_gold'], linestyle='--', label='Predicted Gold Price', color='orange')
plt.title('Actual vs Predicted Gold Price in VND')
plt.xlabel('Date')
plt.ylabel('Price in VND')
plt.xticks(rotation=45)
plt.legend()

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()
