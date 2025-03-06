import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (replace 'sales_data.csv' with the path to your dataset)
df = pd.read_csv('sales_data.csv')

# Assuming the dataset has columns 'Month' and 'Sales'

# Create a line plot for monthly sales data
plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Sales'], marker='o', color='blue', linestyle='-')
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Create a bar plot for monthly sales data
plt.figure(figsize=(10, 6))
plt.bar(df['Month'], df['Sales'], color='green')
plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()
