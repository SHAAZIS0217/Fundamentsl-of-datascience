import numpy as np

# Define the student_scores NumPy array
# Assuming the data is arranged in a 4x4 matrix as per the given order: Math, Science, English, and History
student_scores = np.array([
    [85, 90, 88, 92],  # Scores for Math
    [78, 85, 80, 88],  # Scores for Science
    [90, 92, 94, 88],  # Scores for English
    [82, 88, 86, 90]   # Scores for History
])

# Calculate the average score for each subject
average_scores = np.mean(student_scores, axis=0)

# Determine the subject with the highest average score
highest_average_subject_index = np.argmax(average_scores)

# Print the average score for each subject and the subject with the highest average score
subjects = ['Math', 'Science', 'English', 'History']
for i, subject in enumerate(subjects):
    print(f"Average score for {subject}: {average_scores[i]}")

print(f"The subject with the highest average score is: {subjects[highest_average_subject_index]}")
