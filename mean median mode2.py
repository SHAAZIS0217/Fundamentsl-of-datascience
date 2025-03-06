import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

# Provided data
data = {
    'age': [23, 23, 27, 27, 39, 41, 47, 49, 50, 52, 54, 54, 56, 57, 58, 58, 60, 61],
    'body_fat': [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2, 34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate mean, median, and standard deviation
mean_age = df['age'].mean()
median_age = df['age'].median()
std_age = df['age'].std()

mean_body_fat = df['body_fat'].mean()
median_body_fat = df['body_fat'].median()
std_body_fat = df['body_fat'].std()

print("Age:")
print("Mean:", mean_age)
print("Median:", median_age)
print("Standard Deviation:", std_age)
print()

print("Body Fat:")
print("Mean:", mean_body_fat)
print("Median:", median_body_fat)
print("Standard Deviation:", std_body_fat)
print()

# Draw boxplots
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
df['age'].plot(kind='box')
plt.title('Boxplot of Age')

plt.subplot(1, 2, 2)
df['body_fat'].plot(kind='box')
plt.title('Boxplot of Body Fat')
plt.show()

# Draw scatter plot
plt.figure(figsize=(6, 6))
plt.scatter(df['age'], df['body_fat'])
plt.title('Scatter Plot of Age vs Body Fat')
plt.xlabel('Age')
plt.ylabel('Body Fat')
plt.grid(True)
plt.show()

# Draw q-q plot
plt.figure(figsize=(6, 6))
stats.probplot(df['age'], dist="norm", plot=plt)
plt.title('Q-Q Plot of Age')
plt.xlabel('Theoretical Quantiles')
plt.ylabel('Ordered Values')
plt.grid(True)
plt.show()

plt.figure(figsize=(6, 6))
stats.probplot(df['body_fat'], dist="norm", plot=plt)
plt.title('Q-Q Plot of Body Fat')
plt.xlabel('Theoretical Quantiles')
plt.ylabel('Ordered Values')
plt.grid(True)
plt.show()
