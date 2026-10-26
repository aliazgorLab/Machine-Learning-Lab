import numpy as np
import time

a = np.array([10, 20, 30, 40, 50])
matrix = np.arange(1,13).reshape(3,4)

print("shape: ", matrix.shape)
print("ndim: ", matrix.ndim)
print("size: ", matrix.size)
print("dtype: ", matrix.dtype)

print("First Row: ", matrix[0])
print("Column 2: ", matrix[:, 1])
print("Submatrix: ", matrix[0:2, 1:3])

print("Mean: ", a.mean() )
print("Std: ", a.std() )
print("Min: ", a.min() )
print("Max: ", a.max() )
print("Mean: ", a.mean() )
print("Argmin: ", a.argmin() )
print("Argmax: ", a.argmax() )

#Vectorization versus loop
x = np.arange(1000000)
t0 = time.perf_counter()
y_vector = 2 * x + 5
t1 = time.perf_counter()

t2 = time.perf_counter()
y_loop = []

for value in x:
    y_loop.append(2 * value + 5)
t3 = time.perf_counter()

print("Vectorization Time: ", t1 - t0)
print("Loop Time: ", t3 - t2)
