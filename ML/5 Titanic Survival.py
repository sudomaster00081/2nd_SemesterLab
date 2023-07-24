




# 5.)Construct a Bayesian classifier using Titanic survival prediction dataset. Calculatethe accuracy, precision,and recall for the dataset

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Load the dataset
data = pd.read_csv('ML\Data\Titanic_dataset.csv')

# Prepare the dataset
data = data[['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch']]
data = data.dropna()
data['Sex'] = data['Sex'].map({'female': 0, 'male': 1})

# Split the dataset into features and target variable
X = data.drop('Survived', axis=1)
y = data['Survived']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the Bayesian classifier
model = GaussianNB()
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Calculate accuracy, precision, and recall
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
