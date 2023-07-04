# 3. Download any numerical dataset with more than 1000 features. Reduce the
# feature dimension with the help of PCA.
# Do the following experiments
# a. Reduce the feature dimension to 300, 400, 500
# b. Perform the machine learning with svm for the different dimensions
# mentioned in a.
# c. Find precision recall and F1 score of all the experiments said in b.
# d. Prepare a comparison table of c



import pandas as pd
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import precision_score, recall_score, f1_score

# Load the dataset
data = pd.read_csv('1000_features.csv')

# Split the dataset into features (X) and target variable (y)
X = data.drop(data.columns[0], axis=1)  # Drop the first column as features
y = data[data.columns[0]]  # Use the first column as the target variable

# Define the desired PCA dimensions (300, 400, 500)
pca_dims = [300, 400, 500]

# Perform the experiments
results = []
for dim in pca_dims:
    # Create PCA object
    pca = PCA(n_components=dim)

    # Fit and transform the data
    X_pca = pca.fit_transform(X)

    # Perform machine learning with SVM
    X_train, X_test, y_train, y_test = train_test_split(X_pca, y, test_size=0.2, random_state=42)
    svm = SVC()
    svm.fit(X_train, y_train)
    y_pred = svm.predict(X_test)

    # Calculate precision, recall, and F1 score
    precision = precision_score(y_test, y_pred, average='macro')
    recall = recall_score(y_test, y_pred, average='macro')
    f1 = f1_score(y_test, y_pred, average='macro')

    # Append the results
    results.append({'Dimension': dim, 'Precision': precision, 'Recall': recall, 'F1 Score': f1})

# Create a DataFrame for the comparison table
results_df = pd.DataFrame(results)

# Print the comparison table
print(results_df)
