import pandas as pd
from sklearn.metrics import precision_score, recall_score, accuracy_score
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
data = pd.read_csv('ML\Data\Titanic_dataset.csv')
data = data[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Survived']]
data['Sex'] = data['Sex'].map({'female': 0 , 'male' : 1})
data = data.dropna()
X = data.drop('Survived', axis = 1)
Y = data['Survived']
x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size=0.2, random_state= 42)
model = GaussianNB()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
accuracy_scor =  accuracy_score(y_test, y_pred)
recall_scor = recall_score (y_test, y_pred)
precision_scor = precision_score(y_test, y_pred)
print(f"accuracy = {accuracy_scor}, recall = {recall_scor}, precision = {precision_scor}")