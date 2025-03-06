# List of purchase amounts (replace these values with the actual dataset)
purchase_amounts = [50, 60, 70, 50, 80, 70, 60, 50, 50, 70]

# Calculate the mean (average) purchase amount
mean_purchase_amount = sum(purchase_amounts) / len(purchase_amounts)

# Identify the mode of the purchase amounts
from statistics import mode as st_mode
mode_purchase_amount = st_mode(purchase_amounts)

print("Mean (average) purchase amount:", mean_purchase_amount)
print("Mode of purchase amounts:", mode_purchase_amount)

