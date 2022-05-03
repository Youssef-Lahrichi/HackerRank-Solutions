import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

info = list(map(int, input().split()))
num_features, num_train = info[0], info[1]

x_train = []
y_train = []
for i in range(num_train):
    obs = list(map(float, input().split()))
    x_train.append(obs[:num_features])
    y_train.append(obs[-1])

num_test = int(input())
x_test = []

for i in range(num_test):
    x_test.append(list(map(float, input().split())))

poly_reg = PolynomialFeatures(degree=3, include_bias=False)
x_train_poly = poly_reg.fit_transform(x_train)

lin_reg = LinearRegression()
lin_reg.fit(x_train_poly, y_train)

y_pred = lin_reg.predict(poly_reg.fit_transform(x_test))
for pred in y_pred:
    print(round(pred, 2))
