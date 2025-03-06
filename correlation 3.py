import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
data = {
    'Age': [22, 25, 39, 45, 33],
    'Salary': [40000, 45000, 150000, 200000, 120000]
}

# Create a pandas DataFrame
df = pd.DataFrame(data)

# Calculate correlation matrix
correlation_matrix = df.corr()

print("Correlation Matrix:")
print(correlation_matrix)

# Calculate covariance matrix
covariance_matrix = df.cov()

print("\nCovariance Matrix:")
print(covariance_matrix)

# Plot correlation plot
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlation Plot of Age and Salary')
plt.show()
