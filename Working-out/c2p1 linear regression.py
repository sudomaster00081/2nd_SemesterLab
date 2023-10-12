# Build a linear regression model on the given powerplantdataset. Create the training and testing set. Make predictions of the data points in the testset. Evaluate the model using appropriate performance matrix

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
dataset = pd.read_excel("ML\Data\Power Plant.xlsx")
print(dataset)
X = dataset[['AT', 'V', 'AP', 'RH']]
Y = dataset[['PE']]
x_train, x_test, y_train, y_test = train_test_split (X, Y, test_size = 0.3 , random_state = 42)
model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print (f"Mean Squared Error = {mse} \nRsquared = {r2}")

