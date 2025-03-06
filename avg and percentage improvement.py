import numpy as np

# Example fuel efficiency data for different car models (replace this with your actual data)
fuel_efficiency = np.array([30, 35, 25, 28, 32])

# Step 1: Calculate the average fuel efficiency across all car models
average_fuel_efficiency = np.mean(fuel_efficiency)

# Step 2: Determine the percentage improvement in fuel efficiency between two car models
# For example, let's compare the first and third car models
car_model_1_efficiency = fuel_efficiency[0]
car_model_2_efficiency = fuel_efficiency[2]

# Calculate the improvement in fuel efficiency
improvement = car_model_2_efficiency - car_model_1_efficiency

# Calculate the percentage improvement
percentage_improvement = (improvement / car_model_1_efficiency) * 100

print(f"The average fuel efficiency across all car models is: {average_fuel_efficiency} miles per gallon")
print(f"The percentage improvement in fuel efficiency between the first and third car models is: {percentage_improvement:.2f}%")
