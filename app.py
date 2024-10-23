import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import random
import csv
import pickle

# Function to determine gas result based on gas level
def get_gas_result(gas_level):
    if gas_level > 3500:
        return "safe"
    elif 2000 <= gas_level < 3500:
        return "caution"
    else:
        return "danger"

# Generate dataset
records = []
for _ in range(200):
    gas_level = random.randint(0, 4000)  # Random gas level between 0 and 4000
    gas_result = get_gas_result(gas_level)
    records.append({"gas_level": gas_level, "gas_result": gas_result})

# Write records to a CSV file
csv_file = 'gas_data.csv'
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["gas_level", "gas_result"])
    writer.writeheader()
    writer.writerows(records)

# Load the dataset
data = pd.read_csv(csv_file)

# Preprocessing
X = data[['gas_level']]
y = data['gas_result']

# Encode target labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Create and train the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=label_encoder.classes_)

# Output results
print(f"Accuracy: {accuracy:.2f}")
print("Classification Report:")
print(report)

# Save the model as a pickle file
with open('logistic_regression_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)
    pickle.dump(label_encoder, model_file)  # Save the label encoder as well

print("Model and label encoder saved as 'logistic_regression_model.pkl'.")
