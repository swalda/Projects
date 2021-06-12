import random
import numpy as np
import matplotlib.pyplot as plt

N = 200
n = 1000
A = []
for i in range(0, n):
    A.append(random.randint(0, N))
B = np.zeros(N + 1)
for i in range(0, n):
    B[A[i]] += 1
    
X = np.linspace(0, N, N + 1)
Y = np.array(B)

plt.scatter(X, Y, s = 0.5)
plt.plot(X, Y, linewidth = 0.9)

plt.minorticks_on()
plt.grid(which='major', color = 'k', linewidth = 0.5) 
plt.grid(which='minor', color = 'k', linestyle = ':', linewidth = 0.4) 

plt.savefig('Graph.png', dpi = 1000)
plt.show()
