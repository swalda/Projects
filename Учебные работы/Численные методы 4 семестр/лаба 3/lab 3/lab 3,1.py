import numpy as np
import math 
import matplotlib.pyplot as plt

def GODPLSNO(m, a, b, c):
    A = np.zeros(m)
    A = A + a
    
    B = np.zeros(m - 3)
    B = B + b
    
    C = np.zeros(m - 4)
    C = C + c    
    return A,B,C

def GODPLSYES(m):
    b = np.zeros(m)
    for i in range(0, m):
        b[i] = i**2 - m
    
    return b

def roots(a,b,c,B):
    m = len(a)-1
    x = np.zeros(m+1)
    x[0] = B[m]/a[0]
    x[1] = B[m-1]/a[1]
    x[2] = B[m-2]/a[2]
    x[3] = (B[m-3] - x[0]*b[0])/a[3]
    for i in range (4, m+1):
        x[i] = (B[m-i] - x[i-4]*c[i-4] - x[i-3]*b[i-3])/a[i]
        
    return x

a,b,c = GODPLSNO(80, 100, 15, 15)

B = GODPLSYES(80)

#a = np.array([1,1,1,1,1,1])
#b = np.array([2,2,2])
#c = np.array([3,3])

#B = np.array([6,6,3,1,1,1])

X = roots(a,b,c,B)
print(X)

Y = np.linspace(1,80,80,endpoint = True)
plt.plot(Y,X)
plt.grid()
plt.show()
