import pandas as pd

# Load the dataset into a DataFrame
df = pd.read_csv("orders.csv")

# Display the first few rows of the DataFrame to understand its structure
print(df.head())
# Summary statistics
print(df.describe())
# Total revenue
total_revenue = df['TotalPrice'].sum()
print("Total Revenue: $", total_revenue)
# Most popular products
popular_products = df['ProductID'].value_counts().head(10)
print("Top 10 Popular Products:")
print(popular_products)
# Number of orders per customer
orders_per_customer = df.groupby('CustomerID')['OrderID'].nunique()
print("Number of Orders per Customer:")
print(orders_per_customer)
# Order quantity distribution
order_quantity_distribution = df['Quantity'].value_counts().sort_index()
print("Order Quantity Distribution:")
print(order_quantity_distribution)
# Average order value
average_order_value = df.groupby('OrderID')['TotalPrice'].sum().mean()
print("Average Order Value: $", average_order_value)
