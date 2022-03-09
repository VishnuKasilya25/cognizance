#1.Addition of two numpy arrays
import numpy as np
v = np.array([4,1,5,7,2])
k = np.array([3,2,1,3,7])
S=np.add(v,k)
print("The addition  of two arrays: ")
print()
print(S)

print()
#2.Multiplying a matrix
import numpy as np
A = ([1, 2, 5],[4 ,-4, 8],[9, -2, -3])
B = ([2, 4, -1],[2, 7, 3],[1,-6, 0])
print("Matrix A")
print(A)
print("Matrix B")
print(B)
C = np.dot(A,B)
print()
print("The multiplication of two matrices is ")
print()
print(C)


