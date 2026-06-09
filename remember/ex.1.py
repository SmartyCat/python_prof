import numpy as np

data = np.array(
    [
        [120, 80, 90, 100],
        [60, 70, 65, 75],
        [200, 180, 210, 190],
        [50, 55, 60, 65],
        [150, 160, 155, 165],
    ]
)
avarage = data.mean(axis=1)
print(avarage)
print(avarage.argmax())
print(data.argmax(axis=1))
new_array = np.where(data < data.mean(), 0, data)
print(data[(data > data.mean()) & (data < data.max())])
data = data.reshape(data.size)
print(data[data.argsort()])