import numpy as np
import copy 
import matplotlib.pyplot as plt
import math

def F(x):
    res = 0 
    if x < 2:
        res = 4 + 3*x + 3*x**2
    else:
        res = -16 + 23*x - 2*x**2
    return res


X = np.array([0, 1, 2, 3])
Y = np.array([4, 10, 22, 35])
Xlin = np.linspace(0, 3, 31, endpoint = True)
    
plt.scatter(X, Y)


Y1 = np.zeros(31)


for i in range(31):
    Y1[i] = F(Xlin[i])


plt.plot(Xlin, Y1)


plt.grid()
plt.show()