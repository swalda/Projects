import numpy as np
import copy

A = np.array([[77, 2, -3, -1], 
              [9, 101, -7, 4],
              [-2, 7, 84, 1],
              [-3, 3, -7, 102]], float)

b = np.array([502, 227, -1065, 147])

def ChangeArray(A, b):
    m = len(A)
    B = np.zeros((m,m))
    c = np.zeros(m)
    for i in range(0,m):
        for j in range(0,m):
            if i != j:
                B[i][j] = -A[i][j]/A[i][i]
        c[i] = b[i]/A[i][i]
    
    return B,c 

def Norma(U):
    U = abs(U)
    return np.max(U)

def NormaMat(A):
    m = len(A)
    res = np.zeros(m)
    for i in range(0,m):
        for j in range(0,m):    
            res[i] += abs(A[i][j])
    return np.max(res)

B, C = ChangeArray(A, b)
x = np.zeros(4)
print(B)
print(C)
print(Norma(np.dot(A,x) - b))
"""
for i in range (3):
    x2 = copy.deepcopy(x)
    x = (np.dot(B,x) + C)
    

print(Norma(np.dot(A,x) - b))

print((NormaMat(B)/(1 - NormaMat(B)))*Norma(x - x2))

"""

for t in range(3):
    x2 = copy.deepcopy(x)
    for i in range(0,4):
        x[i] = 0
        for j in range(0,4):
            x[i] += B[i][j]*x[j]
        x[i] +=C[i]

print(Norma(np.dot(A,x) - b))

B2 = np.zeros((4,4))
for i in range(0,4):
    for j in range(0,4):
        if j > i:
            B2[i][j] = B[i][j]
            

print((NormaMat(B2)/(1 - NormaMat(B)))*Norma(x - x2))