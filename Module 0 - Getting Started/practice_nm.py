
import numpy as np

#Array 

A = np.array([[3, 0, 2],
            [0, 4, -1],
            [-5, -5, 20]])
B = np.array([5, -8, 0])

currents = np.linalg.solve(A, B)
print(currents)

