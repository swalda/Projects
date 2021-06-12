import numpy as np
import copy 
import matplotlib.pyplot as plt
import math

def F(x):
    return(3.6*x + 1.4*(3**(x-4)))

X = np.array([0.3, 1.5, 2.2, 3.2, 3.4, 5.6])
Y = np.array([1.104, 5.49, 8.114, 12.101, 12.964, 28.279])
Xlin = np.linspace(0, 6, 1000)
    
plt.scatter(X, Y)

sum = 0
for i  in range(6):
    sum += (3**(X[i] - 4))*Y[i]
print(sum)

Y1 = np.zeros(1000)


for i in range(1000):
    Y1[i] = F(Xlin[i])


plt.plot(Xlin, Y1)


plt.grid()
plt.show()