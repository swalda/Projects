import math
import numpy as np
import matplotlib.pyplot as plt

def F(x):
    return(math.cos(x) + 2 - (x**3))
def f(x):
    res = (math.cos(x) + 2)**(1/3)
    return res

def df(x):
    res = float(0)
    res = (math.cos(x) + 2)**(-2)
    res = res**(1/3)
    res = res*(1/3)
    res = res*(-math.sin(x))
    return res

def df2(x):
    res = float(0)
    res = (-(math.sin(x)*x) - 2*(math.cos(x)) + 4)/x**3
    return res

def df3(x):
    res = float(0)
    res = (3*(x**2))
    res = res/((1-((x**3) - 2)**2)**(1/2))
    return res
    
    
X = np.linspace(1.2,1.4, 1000)

Y = np.zeros(1000)
for i in range(0,1000):
    Y[i] = df(X[i])
    
print(df(1.4))
plt.plot(X,Y)
plt.grid()
plt.show()


x1 = 0.1
x = 1.3
k = 0
Eps = (10**(-4))*((1-0.196)/0.196)
print (Eps)
while abs(x - x1) > Eps:
    x1 = x
    x = f(x)
    k  += 1
    print(k, x, x-x1 ,F(x))
    
