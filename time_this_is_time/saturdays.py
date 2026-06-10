from datetime import date, timedelta

"""Реализуйте функцию saturdays_between_two_dates() , которая принимает два аргумента в
следующем порядке:
start — начальная дата, тип date
end — конечная дата, тип date
Функция должна возвращать количество суббот между датами start и end включительно.
Примечание 1. Даты могут передаваться в любом порядке, то есть не гарантируется, что первая
дата меньше второй."""


def saturdays_between_two_dates(start: date, end: date) -> int:
    start, end = min(start, end), max(start, end)
    result = 0
    while start <= end:
        if start.isoweekday() == 6:
            result += 1
        start = start + timedelta(days=1)
    return result


date1 = date(2021, 11, 1)
date2 = date(2021, 11, 22)
print(saturdays_between_two_dates(date1, date2))

date1 = date(2020, 7, 26)
date2 = date(2020, 7, 2)
print(saturdays_between_two_dates(date1, date2))

date1 = date(2018, 7, 13)
date2 = date(2018, 7, 13)
print(saturdays_between_two_dates(date1, date2))
