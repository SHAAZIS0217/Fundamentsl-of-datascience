import numpy as np

# Define the sales_data NumPy array
# Assuming the data is stored in a 3x3 matrix where each row represents the sales for a different product
sales_data = np.array([
    [100, 150, 120],  # Sales data for product 1
    [80, 90, 110],    # Sales data for product 2
    [120, 130, 140]   # Sales data for product 3
])

# Calculate the average price of all the products sold in the past month
average_price = np.mean(sales_data)

print(f"The average price of all the products sold in the past month is: {average_price}")
