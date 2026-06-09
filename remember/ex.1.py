import numpy as np

sales = np.array(
    [
        [120, 150, 130, 170],
        [90, 110, 105, 100],
        [200, 180, 220, 210],
        [70, 85, 80, 75],
        [160, 155, 165, 170],
    ]
)
middle_sale = sales.mean(axis=1)
print(middle_sale)
print(middle_sale.argmax())
print(sales.argmax(axis=1))
new_array = np.where(sales < sales.mean(),0,sales)
print(new_array)
print(sales[(sales > sales.mean()) & (sales < 200)])