import pandas as pd

# Load the dataset
data = pd.read_csv('1000_features.csv')

# Get the number of features
num_features = data.shape[1]
print("Number of features:", num_features)
