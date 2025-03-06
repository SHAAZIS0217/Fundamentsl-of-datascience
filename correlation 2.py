import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Mock dataset
data = {
    'Year': [2015, 2016, 2017, 2018, 2019],
    'Smoking Patients': [200, 220, 240, 260, 300],
    'Lung Cancer Patients': [25, 30, 35, 40, 55]
}

# Create a pandas DataFrame
df = pd.DataFrame(data)

# Calculate correlation coefficient
correlation_coefficient = df['Smoking Patients'].corr(df['Lung Cancer Patients'])

print("Correlation Coefficient:", correlation_coefficient)

# Create a scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df['Smoking Patients'], df['Lung Cancer Patients'], color='red')
plt.title('Scatter Plot of Smoking Patients vs Lung Cancer Patients')
plt.xlabel('Smoking Patients')
plt.ylabel('Lung Cancer Patients')
plt.grid(True)
plt.show()
