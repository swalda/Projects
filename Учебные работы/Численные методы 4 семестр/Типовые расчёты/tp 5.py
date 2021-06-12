import numpy as np
import copy


A = np.array([[8, -2, -5, -2],
              [-72, 13, 41, 9],
              [-16, -16, -5, -42],
              [72, -18, -40, -70]], float)

B = np.array([42, -369, 0, 626])

def GausSLAU(A0,B):
    
    m = copy.deepcopy(B)
    A = copy.deepcopy(A0)
    
    lena = len(A0[0])
    for i in range(0, lena):
        #ЭТО ЧАСТЬ АЛГОРИТМА РЕАЛИЗУЕТ ПЕРЕСТАНОВКУ СТРОК 
        for j in range(lena-1, i, -1): # И МЕТОД ЧАСТИЧНОГО ВыБОРА
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

print(GausSLAU(A, B))
