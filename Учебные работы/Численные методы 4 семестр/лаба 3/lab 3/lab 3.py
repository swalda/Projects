import numpy as np
import matplotlib.pyplot
import math
import copy

A0 = np.array([[-29.5, 20, 70, 120, 172],
               [100, 90.5, 170, 70, -28],
               [-30, 20, 130.5, 140, 92],
               [70, 110,240, 190.5, 142],
               [40, 130, 370, 330, 232.5]], float)

A0 = np.array([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 11]], float)

B = np.array([22.9, 8.9, 14.5, 31.7, 46.3])

#B = np.array([14, 32, 56], float)

B1 = np.array([23, 8.9, 15, 31, 46], float)

def Gaus(m):
    A = copy.deepcopy(m)
            
    lena = len(A[0])
    for i in range(0, lena):
        for j in range(lena-1, i, -1):
            if A[j][i] > A[j-1][i]:
                A[[j, j-1]] = A[[j-1, j]]
        
        for j in range (i, lena-1):
            if A[i][i] != 0:
                k = A[j+1][i]/A[i][i]
                for f in range(i, lena):
                    A[j+1][f] = A[j+1][f] - (A[i][f]*k)
                    
    for i in range(0, len(A)):
        for j in range(0, len(m[0])):
            if abs(A[i][j]) < 10**(-13):
                A[i][j] = 0
    return A

def GausSLAU(A0,B):
    
    m = copy.deepcopy(B)
    A = copy.deepcopy(A0)
    
    lena = len(A0[0])
    for i in range(0, lena):
        for j in range(lena-1, i, -1):
            if A[j][i] > A[j-1][i]:
                A[[j, j-1]] = A[[j-1, j]]
                m[j],m[j-1] = m[j-1],m[j]
        
        for j in range (i, lena-1):
            k = A[j+1][i]/A[i][i]
            for f in range(i, lena):
                A[j+1][f] = A[j+1][f] - (A[i][f]*k)
            m[j+1] = m[j+1] - (m[i]*k)
    
    x = np.zeros(lena)
    
    for i in range(lena-1, -1, -1):
        q = 0
        for j in range (lena-1, i, -1):
            q += A[i][j]*x[j]
        x[i] = (m[i] - q)/A[i][i]

    
    return x

def Norma(x):
    res = 0
    for i in range(0, len(x)):
        res += abs(x[i])        
    return res


A = Gaus(A0)
#print(A)
x = GausSLAU(A0, B)
x1 = GausSLAU(A0, B1)
print(x, x1)
 
dB1 = Norma(B-B1)/Norma(B1)
dx1 = Norma(x-x1)/Norma(x1)

print(abs(B-B1), dB1)
print(abs(x-x1), dx1)

CondA = np.linalg.cond(A0, 1)
print(dx1, CondA*dB1)





