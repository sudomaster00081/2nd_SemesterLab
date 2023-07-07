import pandas as pd
import numpy as np

# Set the number of rows and features
num_rows = 1000  # Set the desired number of rows
num_features = 1008  # Set the desired number of features

# Generate random integer data
data = np.random.randint(low=0, high=100, size=(num_rows, num_features))

# Create column names for the features
feature_names = ['num' + str(i) for i in range(1, num_features+1)]

# Create a DataFrame from the generated data
df = pd.DataFrame(data, columns=feature_names)

# Save the DataFrame to a CSV file
df.to_csv('1000_features.csv', index=False)
