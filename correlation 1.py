import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Sample data (replace this with your actual data)
sales_data = [100, 120, 130, 140, 150, 160, 170, 180, 190, 200]
advertising_data = [500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400]

# Create a pandas DataFrame
df = pd.DataFrame({'Sales': sales_data, 'Advertising': advertising_data})

# Calculate correlation coefficient
correlation_coefficient = df['Sales'].corr(df['Advertising'])

print("Correlation Coefficient:", correlation_coefficient)

# Create a scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df['Advertising'], df['Sales'], color='blue')
plt.title('Scatter Plot of Sales vs Advertising')
plt.xlabel('Advertising')
plt.ylabel('Sales')
plt.grid(True)
plt.show()
