import pandas as pd
import numpy as np
from scipy.stats import t

# Sample data
data = {
    'product_title': ['Pineapple slicer', 'Levis Jeans Pant', 'Wallet', 'Salwar'],
    'product_category': ['Apparel', 'Apparel', 'Apparel', 'Apparel'],
    'star_rating': [4, 5, 5, 5],
    'review_headline': ['Really good', 'Perfect Dress', 'Love it', 'Awesome'],
    'review_date': ['2013-01-14', '2014-04-22', '2015-07-28', '2015-06-12']
}

# Create a pandas DataFrame
df = pd.DataFrame(data)

# Filter dataset for the 'Apparel' product category
apparel_reviews = df[df['product_category'] == 'Apparel']

# Calculate mean and standard deviation
mean_rating = apparel_reviews['star_rating'].mean()
std_dev = apparel_reviews['star_rating'].std()

# Calculate sample size
n = len(apparel_reviews)

# Set confidence level (e.g., 95% confidence interval)
confidence_level = 0.95

# Calculate standard error of the mean
standard_error = std_dev / np.sqrt(n)

# Calculate t-score for given confidence level and degrees of freedom (n-1)
t_score = t.ppf((1 + confidence_level) / 2, n - 1)

# Calculate margin of error
margin_of_error = t_score * standard_error

# Calculate confidence interval
lower_bound = mean_rating - margin_of_error
upper_bound = mean_rating + margin_of_error

print("Average rating:", mean_rating)
print("Confidence Interval: ({:.2f}, {:.2f})".format(lower_bound, upper_bound))
