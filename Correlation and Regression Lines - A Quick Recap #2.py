import math

x = [15,  12,  8,   8,   7,   7,   7,   6,   5,   3]
y = [10,  25,  17,  11,  13,  17,  20,  13,  9,   15]

x_mean = float(sum(x)/len(x))
y_mean = float(sum(y)/len(y))


numer, denom1, denom2, s_x, s_y = 0, 0, 0, 0, 0

for i in range(len(x)):
    numer += (x[i] - x_mean)*(y[i]-y_mean)
    denom1 += (x[i] - x_mean)**2
    denom2 += (y[i] - y_mean)**2
    
    s_x += (x[i] - x_mean)**2
    s_y += (y[i] - y_mean)**2

r = numer / (math.sqrt(denom1)*math.sqrt(denom2))

s_x = math.sqrt(s_x/(len(x)-1))
s_y = math.sqrt(s_y/(len(x)-1))

slope = r*(s_y/s_x)
print(round(slope, 3))
