import numpy as np

X = np.array([2, 2.4, 3.2, 4, 4.4])
Y = np.array([6.4, 8.3, 13, 19, 22.5])

def F(X0, Y0):
    res = 0
    if len(X0) == 2:
        res = (Y0[1] - Y0[0])/(X0[1] - X0[0])
    else:
        res = (F(X0[1:],Y0[1:])-F(X0[:len(X0)-1],Y0[:len(X0)-1]))
        res = res / (X0[len(X0)-1]-X0[0])
    
    print (X0, res)
    return res

print(F(X,Y))