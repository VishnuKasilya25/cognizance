import numpy as np
v = np.random.randint(0,2,6)
print("First array:")
print(v)
k = np.random.randint(0,2,6)
print("Second array:")
print(k)
print("To check if two arrays are equal ")
array_equal = np.allclose(v, k)
print(array_equal)