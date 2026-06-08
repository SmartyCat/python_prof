import numpy as np

array = np.array([[120, 150, 90], [80, 200, 110], [300, 100, 250]])


print(array.argmax())
print(array.argmin())
max_sale = array.max()
print(max_sale)
min_sale = array.min()
print(min_sale)
print(array.argmax(axis=1))
print(array.argmin(axis=0))
