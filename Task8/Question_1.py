import numpy as np
v=input("Enter the first number: ")
k=input("Enter the last number: ")
v=int(v)
k=int(k)
A = np.arange(v,k+1)
print(A)
B=input("Enter the no. of zeros to be interleaved: ")
B=int(B)
C = np.zeros(len(A) + (len(A)-1)*(B))

C[::B+1]=A
print()
print(C)