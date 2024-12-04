import numpy as np

matrix_a = np.arange(9 , dtype = float).reshape(3 , 3)
print("Matrix 'matrix_a' :")
print(matrix_a)

array_b = np.array([10 , 10 , 10])
print("\nArray 'array_b' :")
print(array_b)

print("\nElement-wise addition of 'matrix_a' and 'array_b' :")
print(np.add(matrix_a , array_b))

print("\nElement-wise subtraction of 'matrix_a' and 'array_b' :")
print(np.subtract(matrix_a , array_b))

print("\nElement-wise multiplicaition of 'matrix_a' and 'array_b' :")
print(np.multiply(matrix_a , array_b))

print("\nElement-wise divition of 'matrix_a' and 'array_b' :")
print(np.divide(matrix_a , array_b))