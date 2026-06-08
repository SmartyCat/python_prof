import numpy as np

array = np.arange(10,100,10)
array = array.reshape(3,3)
print(array.sum(axis=0))
print(array.sum(axis=1))
print(array[array > 50])