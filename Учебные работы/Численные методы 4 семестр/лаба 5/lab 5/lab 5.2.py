import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    return(abs(math.cos(x) + 0.5))

def Lagrange(dim, x, y):
    n = dim + 1
    temp = np.zeros(n)  #полином - один из членов L_n
    res = np.zeros(n)  # Конечный полином
    for i in range(0, n, 1):
        mnoj = y[i]
        for j in range(0, n, 1):
            if i == j:
                continue
            else:
                mnoj /= (x[i] - x[j])
                if temp[1] == 0:
                    temp[0] = -x[j]
                    temp[1] = 1
                else:
                    tempcopy = np.array(temp * (-x[j]))
                    for k in range(n-1, 0, -1):
                        temp[k] = temp[k - 1]
                    temp[0] = 0
                    temp = temp + tempcopy
        res = res + (temp * mnoj)
        temp = np.zeros(n)
    return res

def Chebish(a, b, c):
    n = c + 1
    res = np.zeros(n)
    for k in range(0, n, 1):
        res[k] =(a + b)/2 + ((b - a)*math.cos(math.pi*((2*k + 1)/(2*c + 2)))/2)
    return res
        
def P(x, a):
    res = 0
    for i in range(0, len(a), 1):
        res += a[i]*(x**i)
    return res


a = 0
b = math.pi*2/3
q = 10
Q = 1000


#x = np.linspace(a, b, q+1, endpoint = True)

x = Chebish(a, b, q)
x = x[::-1]
cheb = x

y = np.zeros(q + 1)
for i in range(0, q + 1, 1):
    y[i] = f(x[i])   
plt.scatter(x, y)

pol = Lagrange(q, x, y)
x = np.linspace(a, b, Q, endpoint = True)
y = np.zeros(Q)
for i in range(0, Q, 1):
    y[i] = P(x[i], pol)    
plt.plot(x, y)

x = np.linspace(a, b, Q, endpoint = True)
y = np.zeros(Q)
for i in range(0, Q, 1):
    y[i] = f(x[i])
plt.plot(x, y)




plt.grid()
plt.show()

x = np.linspace(a, b, Q, endpoint = True)
y = np.zeros(Q)
for i in range(0, Q, 1):
    y[i] = abs(f(x[i]) - P(x[i], pol))
plt.plot(x, y)

plt.grid()
plt.show()

print(pol)






