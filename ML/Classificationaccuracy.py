# 3.) Find the classification accuracy of K-means algorithm with MNIST dataset.

from sklearn.cluster import KMeans
from sklearn.datasets import fetch_openml
from sklearn.metrics import accuracy_score

# Load the MNIST dataset
mnist = fetch_openml('mnist_784')

# Preprocess the data by scaling it to [0, 1] range
X = mnist.data / 255.0
y = mnist.target

# Number of clusters (equal to the number of classes in MNIST)
num_clusters = len(set(y))

# Apply K-means clustering
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(X)

# Assign labels to clusters based on majority vote
labels = []
for i in range(num_clusters):
    cluster_indices = (kmeans.labels_ == i)
    cluster_labels = y[cluster_indices]
    majority_label = max(set(cluster_labels), key=cluster_labels.tolist().count)
    labels.append(majority_label)

# Predict the cluster labels for the original data
predicted_labels = [labels[label] for label in kmeans.labels_]

# Calculate the classification accuracy
accuracy = accuracy_score(y, predicted_labels)
print("Classification Accuracy:", accuracy)
