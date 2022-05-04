import math

x_mean = float(sum(x)/len(x))
y_mean = float(sum(y)/len(y))

numer, denom1, denom2 = 0, 0, 0

for i in range(len(x)):
    numer += (x[i] - x_mean)*(y[i]-y_mean)
    denom1 += (x[i] - x_mean)**2
    denom2 += (y[i] - y_mean)**2

denom = (math.sqrt(denom1)*math.sqrt(denom2))
return numer / denom if denom != 0 else 0
print(r)
