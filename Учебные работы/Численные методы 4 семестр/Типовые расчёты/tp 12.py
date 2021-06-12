import numpy as np
import copy

A = np.array([[4, 3],
              [3, 3]], float)

b = np.array([3, 3])

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


B, C = ChangeArray(A, b)

x = np. zeros(2)

for t in range(10):
    x2 = copy.deepcopy(x)
    print(x)
    for i in range(0,2):
        x[i] = 0
        for j in range(0,2):
            x[i] += B[i][j]*x[j]
        x[i] += C[i]
print(x)