"""
Реализуйте функцию same_parity() , которая принимает один аргумент:
numbers — список целых чисел
Функция должна возвращать новый список, элементами которого являются числа из
списка numbers , имеющие ту же четность, что и первый элемент этого списка.
Примечание 1. Числа в возвращаемом функцией списке должны располагаться в своем
исходном порядке.
"""


def same_parity(numbers: list) -> list:
    if not numbers:
        return []
    return [number for number in numbers if number % 2 == numbers[0] % 2]


print(same_parity([2, 2, 2, 2, 3, 0, 2, 3]))
print(same_parity([-1, 1248234832443, 8]))
print(same_parity([1, 2, 4, 6, 8]))
print(same_parity([1, 3, 5, 7, 9]))
