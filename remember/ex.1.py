import numpy as np

array = np.array([[78, 92, 85], [60, 55, 70], [95, 88, 91], [40, 72, 65]])

avar_grades = array.mean(axis=1)
one_job = array.mean(axis=0)
print(np.where(avar_grades > 80))
new_array = np.where(array < 60, 60, array)
print(new_array)