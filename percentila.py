import numpy as np

# Sample response time data
response_times = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]

# Calculate percentiles
percentiles = np.percentile(response_times, [25, 50, 75])

print("25th percentile (Q1):", percentiles[0])
print("50th percentile (Median):", percentiles[1])
print("75th percentile (Q3):", percentiles[2])
import numpy as np

# Sample recovery time data
recovery_times = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23]

# Calculate percentiles
percentiles = np.percentile(recovery_times, [10, 50, 90])

print("10th percentile:", percentiles[0])
print("50th percentile (Median):", percentiles[1])
print("90th percentile:", percentiles[2])
