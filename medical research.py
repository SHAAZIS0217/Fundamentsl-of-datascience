import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Assuming you have a DataFrame with columns 'smoking' and 'lung_cancer_rate'
# Load your dataset into a DataFrame
# For demonstration, let's create a sample dataset
data = {
    'smoking': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],  # 1 for smokers, 0 for non-smokers
    'lung_cancer_rate': [20, 10, 30, 15, 25, 10, 35, 20, 40, 15]  # Lung cancer rates
}
df = pd.DataFrame(data)

# Calculate correlation coefficient
correlation_coefficient = np.corrcoef(df['smoking'], df['lung_cancer_rate'])[0, 1]

print("Correlation Coefficient between Smoking and Lung Cancer Rate:", correlation_coefficient)

# Create scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df['smoking'], df['lung_cancer_rate'], color='blue')
plt.title("Smoking vs. Lung Cancer Rate")
plt.xlabel("Smoking (1 = Smoker, 0 = Non-smoker)")
plt.ylabel("Lung Cancer Rate")
plt.grid(True)
plt.show()
