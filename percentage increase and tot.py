import numpy as np

# Example sales data for each quarter (replace this with your actual sales data)
sales_data = np.array([50000, 60000, 70000, 80000])

# Step 1: Calculate the total sales for the year
total_sales = np.sum(sales_data)

# Step 2: Calculate the percentage increase in sales from the first quarter to the fourth quarter
# Calculate the increase in sales
increase_in_sales = sales_data[3] - sales_data[0]

# Calculate the percentage increase
percentage_increase = (increase_in_sales / sales_data[0]) * 100

print(f"The total sales for the year is: ${total_sales}")
print(f"The percentage increase in sales from the first quarter to the fourth quarter is: {percentage_increase:.2f}%")
