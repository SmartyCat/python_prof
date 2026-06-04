"""
Реализуйте функцию index_of_nearest() , которая принимает два аргумента в следующем
порядке:
numbers — список целых чисел
number — целое число
Функция должна находить в списке numbers ближайшее по значению число к числу number и
возвращать его индекс. Если список numbers пуст, функция должна вернуть число −1.
Примечание 1. Если в функцию передается список, содержащий несколько чисел, одновременно
являющихся ближайшими к искомому числу, функция должна возвращать наименьший из
индексов ближайших чисел.
Примечание 2. Рассмотрим третий тест. Ближайшими числами к числу 4 являются 5 и 3,
имеющие индексы 1 и 2 соответственно. Наименьший из индексов равен 1.
"""


def index_of_nearest(numbers: list[int], number: int) -> int:
    if not numbers:
        return -1
    return numbers.index(min(numbers, key=lambda x: abs(number - x)))


print(index_of_nearest([], 17))

print(index_of_nearest([7, 13, 3, 5, 18], 0))

print(index_of_nearest([9, 5, 3, 2, 11], 4))

print(index_of_nearest([7, 5, 4, 4, 3], 4))

print(index_of_nearest([6, 100, 101, 2], 4))

print(
    index_of_nearest([734234423423423, 5343423423546463423, 934234423423423423, -1], 0)
)

print(index_of_nearest([1, 14, 100, 65, 6], 5))

print(index_of_nearest([10, 164, 100, 265, 16], 8))

print(index_of_nearest([10, 99, 0, -12, 16], -9))

print(index_of_nearest([1, 1, 1, 1, 1], 1))
