import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score
data = pd.read_csv('ML\Data\iris.csv', header=None)
X = data.iloc[:, :-1]
y = data.iloc[:, -1]
x_train, x_test, y_train, y_test = train_test_split(X, y,test_size=0.2 , random_state=42)
svmmodel1 = SVC(kernel = 'linear')
svmmodel2 = SVC(kernel = 'rbf')
svmmodel3 = SVC(kernel= 'poly')
voting_model =VotingClassifier(estimators=[('svm1', svmmodel1), ('svm2', svmmodel2), ('svm3', svmmodel3)], voting='hard')
voting_model.fit(x_train, y_train)
y_pred = voting_model.predict(x_test)
accuracy_scor = accuracy_score(y_test, y_pred)
print (f"accuracy of the voting model = {accuracy_scor}")
