# 2.) Given the following data, which specify classifications for nine combinations of
# VAR1 and VAR2 predict a classification for a case where VAR1=0.906 and
# VAR2=0.606, using the result of k- means clustering with 3 means (i.e., 3
# centroids)
# VAR1 VAR2 CLASS
# 1.713 1.586 0
# 0.180 1.786 1
# 0.353 1.240 1
# 0.940 1.566 0
# 1.486 0.759 1
# 1.266 1.106 0
# 1.540 0.419 1
# 0.459 1.799 1
# 0.773 0.186 1
from sklearn.cluster import KMeans
dataset = [
    [1.713, 1.586, 0],
    [0.180, 1.786, 1],
    [0.353, 1.240, 1],
    [0.940, 1.566, 0],
    [1.486, 0.759, 1],
    [1.266, 1.106, 0],
    [1.540, 0.419, 1],
    [0.459, 1.799, 1],
    [0.773,0.186, 1 ]
]
new_data = [0.906, 0.606]
X = [[point[0], point[1]] for point in dataset if None not in point]
y = [[point[2]] for point in dataset if None not in point]
k = 3
kmeans = KMeans(n_clusters = k, random_state = 42)
kmeans.fit(X)
new_case_cluster = kmeans.predict([new_data])
cluster_points = [point[2] for point, cluster in zip(dataset, kmeans.labels_) if cluster == new_case_cluster]
predicted_class = max(set(cluster_points), key = cluster_points.count)
print("class assigned =" ,predicted_class)




