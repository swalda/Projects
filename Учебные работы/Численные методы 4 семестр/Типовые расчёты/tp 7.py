import numpy as np
import copy
import math

A = np.array([[25, 20, 15],
              [20, 20, 18],
              [15, 18, 22]], float)
"""
A = np.array([[6.25, -1, 0.5],
              [-1, 5, 2.12],
              [0.5, 2.12, 3.6]], float)
"""
B = np.array([-370, -324, -256])

#B = np.array([7.5, -8.68, -0.24])


def HolecL(A0):
    A = copy.deepcopy(A0)
    lena = len(A)
    L = np.zeros((lena,lena))
    for j in range (0, lena):
        for i in range(j, lena):            
            if i == j:
                q = 0
                for t in range(0,i):
                    q += L[i][t]**2
                L[i][i] = math.sqrt(A[i][i] - q)
            
            q = 0
            for t in range(0, j):
                q += L[i][t]*L[j][t]
            L[i][j] = (A[i][j] - q)/L[j][j]
    return L

def HolecSLAU(L0, B):
    L = copy.deepcopy(L0)
    Lt = np.transpose(L)
    m = copy.deepcopy(B)
    lena = len(L)
    for i in range(0,lena):
        for j in range(0, i):
            m[i] = m[i] - m[j]*L[i][j]
        m[i] = m[i]/L[i][i]
        
    x = np.zeros(lena)
        
    for i in range(lena-1, -1, -1):
        q = 0
        for j in range (lena-1, i, -1):
            q += Lt[i][j]*x[j]
        x[i] = (m[i] - q)/Lt[i][i]

    
    return x
    
L = HolecL(A)
print(L)
X = HolecSLAU(L, B)
print(X)