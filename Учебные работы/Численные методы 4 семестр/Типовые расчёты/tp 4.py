import numpy as np
import math
import matplotlib.pyplot as plt

#fuck if all bullshit TP 4, and fuck you sweety 

def f(x):
    res = (1/(2*((x+1)**(1/2)))) - (1/x)
    return res

def df(x):
    res = (-1/4)*((x+1)**(-3/2)) + (1/(x**2))
    return res

print(5,f(5), df(5))
B = 1000
X = np.linspace(4, 6, B)

Y = np.zeros(B)
for i in range(0, B):
    Y[i] = f(X[i])
    
plt.plot(X,Y)

for i in range(0, B):
    Y[i] = df(X[i])
    
plt.plot(X,Y)

plt.grid()
plt.show()

x1 = 5.1
x = 5
k = 0
Eps = (10**(-8))
while abs(x - x1) > Eps:
    x1 = x
    x = x - f(x)/df(x)
    k  += 1
    print(k, x ,f(x))