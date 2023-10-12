import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import SVC 
from sklearn.datasets import load_wine
from sklearn.metrics import f1_score
def crossvalsvm(X,y):
    svm = SVC(kernel= 'linear') 
    f1s = cross_val_score(svm, X, y, cv= 10, scoring='f1_weighted')
    result = f1s.mean()
    return result
def svmvary(X,y,vary):
    xtest, xtrain, ytest, ytrain = train_test_split(X, y, test_size=vary , random_state=42)
    model = SVC(kernel='linear')
    model.fit(xtrain, ytrain)
    ypred = model.predict(xtest)
    f1 = f1_score(ytest, ypred, average='micro')
    return f1
dataset = load_wine()
X, y = dataset.data, dataset.target 
vary = [0.2,0.3,0.4]
result =[]
for test in vary:
    result.append(svmvary(X,y,test))
cross=crossvalsvm(X,y)
print('Result :')
for re in result :
    print(re)
print ("cross", cross)
