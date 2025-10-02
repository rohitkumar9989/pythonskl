import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('Salary_data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

print ("Years of Experience in CSV...")
print (X)
print ("Salary based upon of Experience in CSV...")
print (y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

poly_features = PolynomialFeatures(degree=2)
X_train_poly = poly_features.fit_transform(X_train)
X_test_poly = poly_features.transform(X_test)

regressor = LinearRegression()
regressor.fit(X_train_poly, y_train)

import matplotlib.pyplot as plt
X_plot = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
X_plot_poly = poly_features.transform(X_plot)
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_plot, regressor.predict(X_plot_poly), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

y_pred = regressor.predict(poly_features.transform(np.array([[15]])))
print ("\n\nPredicted salary for 15 years of experience:")
print (y_pred)
y_pred = regressor.predict(poly_features.transform(np.array([[25]])))
print ("\n\nPredicted salary for 25 years of experience:")
print (y_pred)
y_pred = regressor.predict(poly_features.transform(np.array([[13]])))
print ("\n\nPredicted salary for 13 years of experience:")
print (y_pred)
