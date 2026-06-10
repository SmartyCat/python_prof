from datetime import date

"""Реализуйте функцию is_correct() , которая принимает три аргумента в следующем порядке:
day — натуральное число, день
month — натуральное число, месяц
year — натуральное число, год
Функция должна возвращать True , если дата с компонентами day , month и year является
корректной, или False в противном случае.
Примечание 1. Вспомните про конструкцию try-except ."""


def is_correct(day: int, month: int, year: int) -> bool:
    try:
        date(year, month, day)
        return True
    except:
        return False


print(is_correct(31, 12, 2021))
print(is_correct(31, 13, 2021))
