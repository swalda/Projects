import matplotlib.pyplot as plt
import pylab
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math
import copy




def makeSet (m):
    x = np.arange (0, m, 1)
    y = np.arange (0, m, 1)
    xgrid, ygrid = np.meshgrid(x, y)

    return xgrid, ygrid


def CreateArrays(m):
    A = np.zeros((m,m))    
    X = np.zeros(m)
    for i in range(0,m):
        X[i] = 29
        
    bet = 42*m
    for i in range(0,m):
        for j in range(0,m):
            A[i][j] = (math.cos(i+j))/(0.1*bet) + 0.1*bet*math.exp(-((i-j)**2))
    B = np.dot(A,X)
    return A, X, B

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


def Norma(A):
    A = abs(A)
    return np.max(A)

def NormaMat(A):
    m = len(A)
    res = np.zeros(m)
    for i in range(0,m):
        for j in range(0,m):    
            res[i] += abs(A[i][j])
    return np.max(res)
    
m = 80
A, X, B = CreateArrays(m)
"""
X0 = np.linspace(1,m,m)
Y = np.zeros(m)
Y += 10**(-6)

plt.plot(X0,Y)

lamb = np.zeros(m)
lamb, qwerty = np.linalg.eig(A)
lambmax = np.max(lamb)
lambmin = np.min(lamb)
q = (lambmax - lambmin)/(lambmax + lambmin)
t = 2/(lambmax + lambmin)

C = np.eye(m) - t*A
d = B*t
"""
X = np.zeros(m) 
Epsi = 10**(-6)
"""
A = np.array([[6.25, -1, 0.5],
             [-1, 5 ,2.12],
             [0.5, 2.12, 3.6]])

B = np.array([7.5, -8.68, -0.24])
"""
B0, c = ChangeArray(A, B)

B2 = np.zeros((m,m))
for i in range(0,m):
    for j in range(0,m):
        if j > i:
            B2[i][j] = B0[i][j]

NormB0 = NormaMat(B0)    
NormB2 = NormaMat(B2)        
Epsi2 = ((1 - NormB0)/NormB2) * Epsi

X = np.zeros(m) 
X2 = np.ones(m)

k=0

while Norma(X - X2) > Epsi2:
    X2 = copy.deepcopy(X)
    k +=1
    for i in range(0,m):
        X[i] = 0
        for j in range(0,m):
            X[i] += B0[i][j]*X[j]
        X[i] +=c[i]
    #print(X)
    #print(Norma(X - X2))
print(X,k,Norma(29 - X))

"""
X2 = np.ones(m)
x
k = 0

r0 = Norma(np.dot(A,X) - B)
rk =r0
while rk/r0 > Epsi:
    X = np.dot(C,X) + d
    rk = Norma(np.dot(A,X) - B)
    k += 1
    
plt.plot(X0,X-29)

print(k, X, Norma(29 - X))

k = 0
X = np.zeros(m)


while Norma(X - X2) > Epsi*((1-q)/q):
    X2 = X
    X = np.dot(C,X) + d
    k += 1
X2 = X
print(k, X, Norma(29 - X))




plt.plot(X0,abs(X-29))
plt.yscale('log')
plt.title('log')
plt.grid()
plt.show()
"""







"""
x, y = makeSet(m)

fig = pylab.figure()
axes = Axes3D(fig)

axes.plot_surface(x, y, A, cmap = cm.Oranges, rstride=1, cstride=1)
pylab.show()
"""
"""
fig, ax = plt.subplots()

ax.pcolormesh(x, y, A, cmap = cm.Oranges)

fig.set_figwidth(10)    
fig.set_figheight(10)    
fig.set_facecolor('floralwhite')
#ax.set_facecolor('seashell')
plt.show()
"""
