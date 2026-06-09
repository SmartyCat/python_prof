import numpy as np

temps = np.array(
    [
        [18, 21, 19, 22, 20],
        [25, 27, 26, 24, 28],
        [15, 17, 16, 18, 19],
        [30, 32, 31, 29, 33],
    ]
)

avar_temp = temps.mean(axis=1)
print(avar_temp)
most_hottest_city = np.where(avar_temp == avar_temp.max())
print(most_hottest_city[0])
hotest_day = temps.argmax(axis=1)
print(hotest_day)
new_array = np.where(temps < 20, 20, temps)
print(new_array)
print(temps[temps > temps.mean()])