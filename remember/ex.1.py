import numpy as np

array = np.array([i for i in range(1, 6)])
print(array)
print(array.dtype)
sum_array = sum(i for i in np.nditer(array))
print(sum_array / array.size)
