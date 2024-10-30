import pandas as pd

# Load the data (replace 'your_file.csv' with the path to your file)
df = pd.read_csv('/Users/trdung/Documents/Project-ADY/gold_price_6_months_ago.csv')

# Convert the Date column to datetime format and keep only the year-month-day part
df['Date'] = pd.to_datetime(df['Date']).dt.date

# Remove duplicate rows based on the Date column, keeping only the second occurrence for each day
df = df.drop_duplicates(subset='Date', keep='last')

# Save the cleaned data to a new file (optional)
df.to_csv('cleaned_gold_prices.csv', index=False)

# Display the cleaned data
print(df)
