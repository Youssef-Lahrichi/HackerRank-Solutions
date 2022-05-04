import math
import os
import random
import re
import sys
from sklearn.linear_model import LinearRegression
import numpy as np



if __name__ == '__main__':
    timeCharged = float(input().strip())
    
    f = open('trainingdata.txt', 'r')
    x_train = []
    y_train = []
    
    for line in f:
        data = list(map(float, line.split(',')))
        if data[0] >= 4:
            continue
        x_train.append(data[0])
        y_train.append(data[1])
        
    x_train = np.array(x_train).reshape(-1,1)
    
    lin_reg = LinearRegression()
    lin_reg.fit(x_train, y_train)
    
    
    if timeCharged >= 4:
        print(8)
    else:
        print(lin_reg.predict(np.array(timeCharged).reshape(-1,1))[0])
