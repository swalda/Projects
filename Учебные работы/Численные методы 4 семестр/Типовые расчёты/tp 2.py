import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    res = math.cos(x) + 2 - x**3
    return res

x = np.linspace(-3.5,3.5,100)
y = np.zeros(100)
for i in range(0,100):
    y[i] = f(x[i])

plt.plot(x,y)
plt.grid()
plt.show()
a = 1.25
b = 1.5 
k = 0
for i in range(10):
    k += 1
    x0 = (a + b)/2
    print(k, x0, f(x0), a, b, abs(a-b))
    if f(x0) > 0:
        a = x0
    else:
        b = x0
        
