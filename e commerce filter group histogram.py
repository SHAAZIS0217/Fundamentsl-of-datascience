import pandas as pd

# Assuming you have a dictionary containing the required columns
data = {
    'OrderID': [1, 2, 3, 4, 5],
    'CustomerID': [101, 102, 103, 101, 104],
    'ProductID': [201, 202, 203, 204, 205],
    'Quantity': [2, 3, 1, 2, 4],
    'TotalPrice': [20.50, 30.25, 15.75, 25.00, 40.50]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Create a new column called 'OrderDate' and extract the date information from the OrderID
df['OrderDate'] = ['10-10-22','20-03-21','07-09-22','25-06-23','10-09-24']
print(df)

# Filter the data to show only orders placed by a specific customer (choose a CustomerID)
specific_customer_id = 101
filtered_data = df[df['CustomerID'] == specific_customer_id]
print(filtered_data)

# Group the data by CustomerID and calculate the total amount spent by each customer
total_spent_per_customer = df.groupby('CustomerID')['TotalPrice'].sum()
print(total_spent_per_customer)

# Visualize the distribution of TotalPrice using a histogram
import matplotlib.pyplot as plt

plt.hist(df['TotalPrice'], bins=10, color='skyblue', edgecolor='black')
plt.xlabel('Total Price')
plt.ylabel('Frequency')
plt.title('Distribution of TotalPrice')
plt.show()
