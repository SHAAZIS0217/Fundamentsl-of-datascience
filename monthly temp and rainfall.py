import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (replace 'data.csv' with the path to your dataset)
df = pd.read_csv('data.csv')

# Assuming the dataset has columns 'Month', 'Temperature', and 'Rainfall'

# Line plot for temperature
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='Month', y='Temperature', marker='o', color='blue')
plt.title('Monthly Temperature Variation')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Scatter plot for rainfall
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Month', y='Rainfall', color='green', s=100)
plt.title('Monthly Rainfall Variation')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
