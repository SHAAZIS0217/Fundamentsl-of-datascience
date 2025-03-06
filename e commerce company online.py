import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample sales data (replace with your actual data)
data = {
    'Product Category': ['Electronics', 'Clothing', 'Books', 'Electronics', 'Books', 'Clothing', 'Electronics'],
    'Sales': [1000, 1500, 800, 1200, 900, 1600, 1100]
}

# Load the data into a DataFrame
df = pd.DataFrame(data)

# Group by product category and calculate total sales
category_sales = df.groupby('Product Category')['Sales'].sum().reset_index()

# Create line plot
plt.figure(figsize=(10, 6))
sns.lineplot(data=category_sales, x='Product Category', y='Sales', marker='o', color='blue')
plt.title('Total Sales Across Different Product Categories (Line Plot)')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Create scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=category_sales, x='Product Category', y='Sales', color='green', s=100)
plt.title('Total Sales Across Different Product Categories (Scatter Plot)')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Create bar plot
plt.figure(figsize=(10, 6))
sns.barplot(data=category_sales, x='Product Category', y='Sales', color='orange')
plt.title('Total Sales Across Different Product Categories (Bar Plot)')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
