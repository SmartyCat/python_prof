import numpy as np

sales = np.array([50, 10, 30, 20, 50, 10, 40, 30])

u = np.unique(sales)
print(u)
print(u.size)

print(np.argsort(sales))
new_array = np.sort(sales)
sales.sort()
print(new_array)
print(sales)
print(sales[sales.argsort()])