import math 
import matplotlib.pyplot as plt
import numpy as np

def fun(x):
    res = 36*math.sin(x) -18*math.sqrt(3)  + 9*math.sqrt(3)*(x**2) + math.sqrt(3)*(math.pi)**2 - 18*x - 6*math.sqrt(3)*math.pi*x + 6*math.pi
    return res

def dfun(x):
    res = 36*math.cos(x) + 18*math.sqrt(3)*x - 18 - 6*math.sqrt(3)*math.pi
    return res

def simplittrtn(f, x, e, a, q):
    i = 0 
    b = x +1
    while abs(x - b) > ((1-q)/q)*e:
        print(i, x, fun(x))
        i += 1
        b = x 
        x = x - a*f(x)
    return x

def Newton(f, df,x, e):
    i = 0
    b = x+1
    Ar = np.zeros(10)
    for i in range(0,10):
        Ar[i] = f(x)
        b = x
        x = x - f(x)/df(x)
        #print(i, x, f(x))
    print(i, x, f(x))
    return Ar

def Chords (f, x0, x1, e):
    i = 0
    temp = x0
    Ar = np.zeros(10)
    for i in range(0,10):
        Ar[i] = f(x1)
        i +=1
        temp = x1
        x1 = x1 - (((x0 - x1)/(f(x0) - f(x1)) * f(x1)))
        x0 = temp
       # print(i, x1)
    print(i, x1, f(x1))
    return Ar
    
x = np.linspace(0,10,10,endpoint = True)
"""
y = np. zeros(50)
for i in range(0,50):
    y[i] = fun(x[i])

plt.plot(x,y)

plt.show

for i in range(0, 50):
    y[i] = dfun(x[i])

plt.plot(x,y)
plt.show

"""
#Ar1N = Newton(fun,dfun,1,10**(-8))
#Ar2N = Newton(fun,dfun,3.1,10**(-8))

Ar1C = Chords(fun,1,1.01, 10**(-8))
Ar2C = Chords(fun,3,3.1, 10**(-8))

plt.plot(x,Ar2N)
plt.plot(x,Ar2C)

plt.grid()
plt.show
