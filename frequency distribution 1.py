# Sample data
data = {
    'Disease_Name': ['Common Cold', 'Diabetes', 'Bronchitis', 'Influenza', 'Kidney Stones'],
    'Diagnosed_Patients': [320, 120, 100, 150, 60]
}

# Create a pandas DataFrame
import pandas as pd
df = pd.DataFrame(data)

# Calculate frequency distribution
frequency_distribution = df.set_index('Disease_Name')['Diagnosed_Patients'].to_dict()

# Find the most common disease
most_common_disease = max(frequency_distribution, key=frequency_distribution.get)
most_common_patients = frequency_distribution[most_common_disease]

print("Most common disease:", most_common_disease)
print("Number of diagnosed patients with the most common disease:", most_common_patients)
