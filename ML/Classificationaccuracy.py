# 3.) Find the classification accuracy of K-means algorithm with MNIST dataset.

# pip install tensorflow

from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score

# Load the MNIST dataset
mnist = fetch_openml('mnist_784')
X = mnist.data
y = mnist.target

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Perform PCA for dimensionality reduction
pca = PCA(n_components=100)
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

# Apply the K-means algorithm
kmeans = KMeans(n_clusters=10, random_state=42)
kmeans.fit(X_train_pca)

# Assign labels to the clusters
y_train_pred = kmeans.labels_

# Evaluate the classification accuracy
accuracy = accuracy_score(y_train, y_train_pred)
print("Training Accuracy:", accuracy)
