import pandas as pd
from sklearn.decomposition import PCA
from sklearn.metrics import precision_score
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
dataset = pd.read_csv(r"ML\Data\1000_features.csv")
X = dataset.drop(dataset.columns[0], axis=1)
y = dataset[dataset.columns[0]]
dimensions = [300, 400 , 500]
result = []
for dim in dimensions:
    pca = PCA(n_components=dim)
    x_pca = pca.fit_transform(X)
    model=SVC()
    x_train, x_test, y_train, y_test = train_test_split(x_pca, y, test_size=0.2, random_state=42)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    precision = precision_score(y_test, y_pred , average= 'macro')
    result.append(f"dimension = {dim}, precision score = {precision}")
print(result)