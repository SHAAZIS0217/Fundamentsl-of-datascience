import numpy as np

# Assuming house_data is a NumPy array containing the dataset with columns: [bedrooms, square footage, sale price]

# Sample house_data
house_data = np.array([
    [3, 2000, 300000],   # House 1: 3 bedrooms, 2000 sqft, $300,000
    [4, 2500, 350000],   # House 2: 4 bedrooms, 2500 sqft, $350,000
    [5, 3000, 400000],   # House 3: 5 bedrooms, 3000 sqft, $400,000
    [6, 2800, 380000],   # House 4: 6 bedrooms, 2800 sqft, $380,000
    [4, 2200, 320000]    # House 5: 4 bedrooms, 2200 sqft, $320,000
])

# Step 1: Filter the rows where the number of bedrooms is greater than four
bedrooms_greater_than_four = house_data[house_data[:, 0] > 4]

# Step 2: Extract the sale prices from the filtered rows
sale_prices = bedrooms_greater_than_four[:, 2]

# Step 3: Calculate the average sale price
average_sale_price = np.mean(sale_prices)

print(f"The average sale price of houses with more than four bedrooms is: ${average_sale_price}")
