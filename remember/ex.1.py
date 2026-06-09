import numpy as np

scores = np.array(
    [
        [72, 85, 90, 88],
        [60, 58, 65, 70],
        [95, 92, 96, 98],
        [40, 55, 50, 45],
        [80, 82, 84, 86],
    ]
)

middle_score = scores.mean(axis=1)
print(middle_score)
print(np.where(scores.mean(axis=1) > scores.mean())[0])
print(scores.argmax(axis=0))
new_array = np.where(scores < 60, 60, scores)
print(new_array)
print(scores[(scores >= 80) & (scores <= 95)])