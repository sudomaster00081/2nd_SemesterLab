# 3.) Find the classification accuracy of K-means algorithm with MNIST dataset.

# pip install tensorflow

from sklearn.datasets import fetch_openml
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score

# Load MNIST dataset
mnist = fetch_openml('mnist_784')

# Prepare the data
X = mnist.data
y = mnist.target

# Create KMeans model
kmeans = KMeans(n_clusters=10, random_state=42)

# Fit the model
kmeans.fit(X)

# Get the predicted labels
labels = kmeans.labels_

# Calculate accuracy
accuracy = accuracy_score(y, labels)

print("Classification accuracy of K-means algorithm with MNIST dataset:", accuracy)
