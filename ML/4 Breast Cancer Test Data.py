# 4.) Build a model to perform classification based on logistic regression on the given
# Breast cancer classification dataset Breast Cancer.csv . Display confusion matrix and accuracy for
# the test data
# pip install pandas scikit-learn numpy
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score
# Load the dataset
data = pd.read_csv('ML\Data\Breast Cancer.csv')
# Split the data into features and target variable
X = data.drop('Class', axis=1)
y = data['Class']
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Create a logistic regression model
model = LogisticRegression()
# Fit the model on the training data
model.fit(X_train, y_train)
# Make predictions on the test data
y_pred = model.predict(X_test)
# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Calculate confusion matrix
confusion = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(confusion)
