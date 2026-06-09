import numpy as np

results = np.array(
    [[12, 15, 14, 16], [18, 17, 19, 20], [10, 11, 13, 12], [21, 22, 20, 23]]
)
avar_every_athlet = results.mean(axis=1)
print(avar_every_athlet)
max_index = np.where(results.mean(axis=1) == avar_every_athlet.max())
print(*max_index)
best_chance = results.argmax(axis=1)
print(best_chance)
new_results = np.where(results < results.mean(), 0, results)
print(new_results)
print(results[(results > 15) & (results < 22)])
