import copy 
import numpy as np

A = np.array([[2, -1, 0, 0, 0],
              [0, 7, -4, 0, 0],
              [0, 1, 5, 2, 0],
              [0, 0, -3, 15, 5],
              [0, 0, 0, 5, 9]], float)

B = np.array([-15, 37, 38, 71, -32])

def Thomas(A0, B0):
    A = copy.deepcopy(A0)
    B = copy.deepcopy(B0)
    lena = len(A[0])
    X = np.zeros(lena)
    alf = np.zeros(lena)
    bet = np.zeros(lena)
    alf[0] = -A[0][1]/A[0][0]
    bet[0] = B[0]/A[0][0]
    for i in range(1, lena-1):
        alf[i] = -A[i][i+1]/(A[i][i] + A[i][i-1]*alf[i-1])
        bet[i] = (B[i] - A[i][i-1]*bet[i-1])/(A[i][i] + A[i][i-1]*alf[i-1])
    
    i = lena - 1
    bet[i] =  (B[i] - A[i][i-1]*bet[i-1])/(A[i][i] + A[i][i-1]*alf[i-1])
    
    X[lena - 1] = bet[lena - 1]
    for i in range(lena - 2, -1, -1):
        X[i] = alf[i]*X[i+1] + bet[i]
    return X
    
X = Thomas(A,B)
print(X)

        