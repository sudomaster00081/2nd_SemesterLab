from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import f1_score, r2_score, precision_score
data = pd.read_csv('ML\Data\Dataset.csv')
X = data.iloc[:, 2:]
Y = data.iloc[:,1]
Y = Y.map({'B' : 0, 'M' : 1})
x_train, x_test, y_train, y_test = train_test_split(X, Y, train_size= 0.2, random_state= 42)
svmmodel = SVC()
naivemodel = GaussianNB()
svmmodel.fit(x_train, y_train)
naivemodel.fit(x_train, y_train)
sv_pred = svmmodel.predict(x_test)
nm_pred = naivemodel.predict(x_test)
svmf1 = f1_score(y_test, sv_pred)
svmr2 = r2_score(y_test, sv_pred)
svmpre =precision_score(y_test, sv_pred)
nmf1 =f1_score(y_test, nm_pred)
nmr2 =r2_score(y_test, nm_pred)
nmpre =precision_score(y_test, nm_pred)

print(f"nmpre{nmpre},{nmf1},{nmr2}\nsvm,{svmpre},{svmf1},{svmr2}")
  
