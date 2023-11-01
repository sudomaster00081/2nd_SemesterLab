import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import pairwise_distances_argmin_min

# Step 1: Generate a synthetic dataset
n_samples = 300
n_features = 2
n_clusters = 3

X, _ = make_blobs(n_samples=n_samples, n_features=n_features, centers=n_clusters, random_state=42)

# Step 2: K-means with Euclidean distance
kmeans_euclidean = KMeans(n_clusters=n_clusters, init='k-means++', random_state=42)
kmeans_euclidean.fit(X)
labels_euclidean = kmeans_euclidean.labels_
centers_euclidean = kmeans_euclidean.cluster_centers_

# Step 3: K-means with Manhattan distance
def custom_manhattan(X, centers):
    return np.linalg.norm(X[:, np.newaxis] - centers, ord=1, axis=2)

labels_manhattan = pairwise_distances_argmin_min(X, centers_euclidean, metric=custom_manhattan)
labels_manhattan = labels_manhattan[0]

# Step 4: Compare the results
wcss_euclidean = sum(np.min(np.linalg.norm(X - centers_euclidean[labels_euclidean], ord=2, axis=1)**2))
wcss_manhattan = sum(np.min(np.linalg.norm(X - centers_euclidean[labels_manhattan], ord=1, axis=1)))

print("WCSS (Euclidean Distance):", wcss_euclidean)
print("WCSS (Manhattan Distance):", wcss_manhattan)

# Visualization (you can use a plotting library for this)
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.scatter(X[:, 0], X[:, 1], c=labels_euclidean, cmap='viridis')
plt.scatter(centers_euclidean[:, 0], centers_euclidean[:, 1], c='red', marker='x')
plt.title("K-means (Euclidean Distance)")

plt.subplot(122)
plt.scatter(X[:, 0], X[:, 1], c=labels_manhattan, cmap='viridis')
plt.scatter(centers_euclidean[:, 0], centers_euclidean[:, 1], c='red', marker='x')
plt.title("K-means (Manhattan Distance)")

plt.show()
