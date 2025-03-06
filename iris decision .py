import pandas as pd
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Load Iris dataset
iris = load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['target'] = iris.target

# Split data into features and target
X = iris_df.drop('target', axis=1)
y = iris_df['target']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Decision Tree classifier
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# User input for new flower attributes
sepal_length = float(input("Enter sepal length: "))
sepal_width = float(input("Enter sepal width: "))
petal_length = float(input("Enter petal length: "))
petal_width = float(input("Enter petal width: "))

# Predict the species of the new flower
new_flower_data = [[sepal_length, sepal_width, petal_length, petal_width]]
predicted_species = clf.predict(new_flower_data)

# Map predicted label to species name
species_names = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
predicted_species_name = species_names[predicted_species[0]]

print("Predicted species:", predicted_species_name)
