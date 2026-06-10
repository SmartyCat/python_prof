from datetime import date, timedelta

"""Реализуйте функцию get_date_range() , которая принимает два аргумента в следующем
порядке:
start — начальная дата, тип date
end — конечная дата, тип date
Функция get_date_range() должна возвращать список, состоящий из дат (тип date )
от start до end включительно. Если start > end , функция должна вернуть пустой список."""


def get_date_range(start: date, end: date) -> list[date] | list:
    result = []
    if start > end:
        return result
    while start <= end:
        result.append(start)
        start = start + timedelta(days=1)
    return result


date1 = date(2021, 10, 1)
date2 = date(2021, 10, 5)
print(*get_date_range(date1, date2), sep="\n")

date1 = date(2019, 6, 5)
date2 = date(2019, 6, 5)
print(get_date_range(date1, date2))
