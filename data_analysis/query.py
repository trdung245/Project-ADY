from data import *

# Show the 5 days with the highest gold price and USD price
highest_gold_price = df.sort_values(by = 'Selling_price', ascending = False).head(5)
print("5 days with the highest gold price")
print(highest_gold_price[['Date','Buying_price','Selling_price']])

highest_USD_price = df.sort_values(by = 'USD to VND', ascending = False).head(5)
print("5 days with the highest USD price")
print(highest_USD_price[['Date','USD to VND']])

# Calculate the average gold price and USD price by month
df['Year-Month'] = df['Date'].dt.to_period('M')
monthly_avg = df.groupby('Year-Month').agg({
    'Buying_price': 'mean',
    'Selling_price': 'mean',
    'USD to VND': 'mean'
}).reset_index()
print("Average gold price and USD price by month")
print(monthly_avg)

# Show the 2 months with the highest average gold price and USD price
top_2_gold = monthly_avg[['Year-Month', 'Selling_price']].sort_values(by = 'Selling_price', ascending = False).head(2)
top_2_usd = monthly_avg[['Year-Month', 'USD to VND']].sort_values(by = 'USD to VND', ascending = False).head(2)
print("2 months with the highest average gold price")
print(top_2_gold)
print("2 months with the highest average USD price")
print(top_2_usd)
