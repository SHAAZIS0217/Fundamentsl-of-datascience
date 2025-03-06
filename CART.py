import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor, export_text

# Load dataset (replace 'dataset.csv' with your dataset)
# Assuming the dataset has columns: 'mileage', 'age', 'brand', 'engine_type', 'price'
data = {
    'mileage': [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000, 150000],
    'age': [2, 3, 5, 1, 4, 6, 2, 3, 4, 5, 1, 2, 3, 4, 5],
    'brand': ['Toyota', 'Toyota', 'Toyota', 'Honda', 'Honda', 'Honda', 'Ford', 'Ford', 'Ford', 'Chevrolet', 'Chevrolet', 'Chevrolet', 'Nissan', 'Nissan', 'Nissan'],
    'engine_type': ['Gasoline', 'Gasoline', 'Gasoline', 'Diesel', 'Diesel', 'Diesel', 'Gasoline', 'Gasoline', 'Gasoline', 'Diesel', 'Diesel', 'Diesel', 'Gasoline', 'Gasoline', 'Gasoline'],
    'price': [22000, 18000, 15000, 25000, 20000, 17000, 18000, 15000, 12000, 22000, 20000, 18000, 16000, 14000, 12000]
}

df = pd.DataFrame(data)

# Convert categorical variables into dummy/indicator variables
df = pd.get_dummies(df, columns=['brand', 'engine_type'])

# Prepare the data for training
X = df.drop('price', axis=1)
y = df['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Decision Tree Regressor model
model = DecisionTreeRegressor(random_state=42)
model.fit(X_train, y_train)

# Allow user to input features of a new car
new_car = {}
new_car['mileage'] = int(input("Enter mileage of the car: "))
new_car['age'] = int(input("Enter age of the car: "))
brand = input("Enter brand of the car (Toyota, Honda, Ford, Chevrolet, Nissan): ")
new_car['brand_' + brand] = 1 if 'brand_' + brand in X.columns else 0
engine_type = input("Enter engine type of the car (Gasoline, Diesel): ")
new_car['engine_type_' + engine_type] = 1 if 'engine_type_' + engine_type in X.columns else 0

# Create a DataFrame for the new car input, including all possible one-hot encoded columns
new_car_df = pd.DataFrame([new_car], columns=X.columns)

# Predict the price of the new car
predicted_price = model.predict(new_car_df)[0]

# Display predicted price
print("Predicted Price:", predicted_price)

# Display decision path
tree_rules = export_text(model, feature_names=list(X.columns))
print("Decision Path:\n", tree_rules)
