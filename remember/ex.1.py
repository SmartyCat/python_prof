import numpy as np

array = np.array([[5, 12, 7], [18, 3, 25], [9, 30, 1]])

print(array[array > 10])
array[array < 10] = 0
print(array.max(axis=1))
print(array.max(axis=0))