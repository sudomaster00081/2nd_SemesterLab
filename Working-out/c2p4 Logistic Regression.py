import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
data = pd.read_csv("ML\Data\Breast Cancer.csv")
print (data)
X = data.drop(['Sample code number', 'Class'], axis = 1)
Y = data['Class']
model = LogisticRegression()
x_train,x_test, y_train,  y_test = train_test_split(X, Y, test_size= 0.2, random_state= 42)
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
confusion = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)
print(f"confusion = \n {confusion} \n accuracy = {accuracy}")