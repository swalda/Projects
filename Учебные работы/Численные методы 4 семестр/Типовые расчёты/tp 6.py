import numpy as np
import copy


A = np.array([[8, -2, -5, -2],
              [-72, 13, 41, 9],
              [-16, -16, -5, -42],
              [72, -18, -40, -70]], float)

B = np.array([42, -369, 0, 626])

def GausLU(A0,B):
    
    m = copy.deepcopy(B)
    A = copy.deepcopy(A0)
    L = np.eye(4)
    lena = len(A0[0])
    for i in range(0, lena):
        for j in range (i, lena-1):
            k = A[j+1][i]/A[i][i]
            L[j+1][i] = k
            for f in range(i, lena):
                A[j+1][f] = A[j+1][f] - (A[i][f]*k)
            m[j+1] = m[j+1] - (m[i]*k)
       
    return L, A

def GausSLAU(L0,U0,B):
    m = copy.deepcopy(B)
    L = copy.deepcopy(L0)
    U = copy.deepcopy(U0)
    
    lena = len(U[0])
    for i in range(0, lena):
        for j in range (i, lena-1):
            k = L[j+1][i]        
            m[j+1] = m[j+1] - (m[i]*k)
       
    x = np.zeros(lena)
    
    for i in range(lena-1, -1, -1):
        q = 0
        for j in range (lena-1, i, -1):
            q += U[i][j]*x[j]
        x[i] = (m[i] - q)/U[i][i]

    
    return x
    
L, U = GausLU(A, B)
print(U)
print(L)
print(np.dot(L,U))
print(GausSLAU(L,U,B))
