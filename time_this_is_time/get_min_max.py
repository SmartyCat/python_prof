from datetime import date

"""Реализуйте функцию get_min_max() , которая принимает один аргумент:
dates — список дат (тип date )
Функция должна возвращать кортеж, первым элементом которого является минимальная дата
из списка dates , вторым — максимальная дата из списка dates . Если список dates пуст,
функция должна вернуть пустой кортеж."""


def get_min_max(dates: list[date]) -> tuple[date, date]:
    if not dates:
        return ()
    return min(dates), max(dates)


dates = [date(2021, 10, 5), date(1992, 6, 10), date(2012, 2, 23), date(1995, 10, 12)]
print(get_min_max(dates))
print(get_min_max([]))
