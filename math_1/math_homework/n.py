import numpy as np
A = np.array([[1,1,0,1],
             [0,1,8,1],
             [1,0,9,1],
             [-1,-1,0,1]])
det = np.linalg.det(A)
print(det)