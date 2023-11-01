# Download any binary class numerical dataset from UCI repostiory and do the classification with 
# a.SVM 
# b.NaiveBayesclassification 
# c.Findouttheprecision, recall and F1 score of the above classiication method Swith 20% of the dataset
import pandas as pd
import numpy as np
import urllib.request
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import precision_score, recall_score, f1_score
# Download the dataset from UCI repository
#url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data'
filename = 'ML\Data\Dataset.csv'
#urllib.request.urlretrieve(url, filename)
# Load the dataset
data = pd.read_csv(filename, header=None)
# Prepare the dataset
X = data.iloc[:, 2:]  # Features (columns 2 onwards)
y = data.iloc[:, 1]   # Target variable (column 1)
# Convert 'B' and 'M' labels to 0 and 1
y = y.map({'B': 0, 'M': 1})
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# SVM Classifier
svm_model = SVC()
svm_model.fit(X_train, y_train)
y_pred_svm = svm_model.predict(X_test)
# Naive Bayes Classifier
nb_model = GaussianNB()
nb_model.fit(X_train, y_train)
y_pred_nb = nb_model.predict(X_test)
# Calculate precision, recall, and F1 score for SVM classifier
precision_svm = precision_score(y_test, y_pred_svm)
recall_svm = recall_score(y_test, y_pred_svm)
f1_svm = f1_score(y_test, y_pred_svm)
# Calculate precision, recall, and F1 score for Naive Bayes classifier
precision_nb = precision_score(y_test, y_pred_nb)
recall_nb = recall_score(y_test, y_pred_nb)
f1_nb = f1_score(y_test, y_pred_nb)
# Print the results
print("SVM Precision:", precision_svm)
print("SVM Recall:", recall_svm)
print("SVM F1 Score:", f1_svm)
print("Naive Bayes Precision:", precision_nb)
print("Naive Bayes Recall:", recall_nb)
print("Naive Bayes F1 Score:", f1_nb)
