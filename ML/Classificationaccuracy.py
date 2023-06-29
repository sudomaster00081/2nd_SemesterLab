from keras.datasets import mnist
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
import numpy as np

# Load the MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Reshape the training and testing data
X_train = x_train.reshape(len(x_train), -1)
X_test = x_test.reshape(len(x_test), -1)

# Apply K-means clustering
k = len(np.unique(y_train))  # Number of unique classes
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(X_train)

# Assign cluster labels to test samples
y_pred = kmeans.predict(X_test)

# Convert cluster labels to integer values
cluster_labels = kmeans.labels_
cluster_centers = kmeans.cluster_centers_
mapped_labels = np.zeros_like(y_pred)
for i in range(k):
    mask = (y_pred == i)
    mapped_labels[mask] = np.argmax(np.bincount(y_train[cluster_labels == i]))

# Evaluate the classification accuracy
accuracy = accuracy_score(y_test, mapped_labels)

print("Classification Accuracy:", accuracy)
