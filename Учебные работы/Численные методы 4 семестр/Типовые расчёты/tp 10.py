import numpy as np

A = np.array([[-9.769, -0.19, 1.4, -1.102],
              [-0.259, -7.833, -1.166, 0.967],
              [-0.945, 1.179, -2.007, 6.836],
              [-1.501, 0.967, -6.76, -2.391]], float)

B = np.array([7.2, 8, 5.2, 8])

print(np.linalg.cond(A, np.inf))
print(np.linalg.norm(A, ord = np.inf))

