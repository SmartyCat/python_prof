from datetime import timedelta, datetime

"""Во время визита очередного гостя сотрудникам отеля приходится проверять, доступна ли та
или иная дата для бронирования номера.
Реализуйте функцию is_available_date() , которая принимает два аргумента в следующем
порядке:
booked_dates — список строковых дат, недоступных для бронирования. Элементом списка
является либо одиночная дата, либо период (две даты через дефис). Например:
['04.11.2021', '05.11.2021-09.11.2021']
date_for_booking — одиночная строковая дата или период (две даты через дефис), на
которую гость желает забронировать номер. Например:
'01.11.2021' или '01.11.2021-04.11.2021'
Функция is_available_date() должна возвращать True , если дата или
период date_for_booking полностью доступна для бронирования. В противном случае функция
должна возвращать False .
Примечание 1. Гарантируется, что в периоде левая дата всегда меньше правой.
Примечание 2. В периоде (две даты через дефис) граничные даты включены"""


def func(
    arg: list[str],
) -> set[
    datetime
]:  # создал вспомогательную функцию для преобразования, исходил что множество наиболее оптимальная структура
    result = set()
    for d in arg:
        if "-" not in d:
            result.add(datetime.strptime(d, "%d.%m.%Y"))
        else:
            start, end = d.split("-")
            start, end = datetime.strptime(start, "%d.%m.%Y"), datetime.strptime(
                end, "%d.%m.%Y"
            )
            while start <= end:
                result.add(start)
                start = start + timedelta(days=1)
    return result


def is_available_date(booked_dates: list[str], date_for_booking: str) -> bool:
    result = func(booked_dates) & func(date_for_booking.split())  # ищем пересечение
    return True if not result else False


dates = ["04.11.2021", "05.11.2021-09.11.2021"]
some_date = "01.11.2021"
print(is_available_date(dates, some_date))

dates = ["04.11.2021", "05.11.2021-09.11.2021"]
some_date = "01.11.2021-04.11.2021"
print(is_available_date(dates, some_date))

dates = ["04.11.2021", "05.11.2021-09.11.2021"]
some_date = "06.11.2021"
print(is_available_date(dates, some_date))

dates = ["01.11.2021", "05.11.2021-09.11.2021", "12.11.2021", "15.11.2021-21.11.2021"]
some_date = "12.11.2021"
print(is_available_date(dates, some_date))

dates = ["01.11.2021", "05.11.2021-09.11.2021", "12.11.2021", "15.11.2021-21.11.2021"]
some_date = "09.11.2021"
print(is_available_date(dates, some_date))

dates = ["01.11.2021", "05.11.2021-09.11.2021", "12.11.2021", "15.11.2021-21.11.2021"]
some_date = "15.11.2021"
print(is_available_date(dates, some_date))

dates = ["01.11.2021", "05.11.2021-09.11.2021", "12.11.2021", "15.11.2021-21.11.2021"]
some_date = "17.11.2021"
print(is_available_date(dates, some_date))

dates = ["01.11.2021", "05.11.2021-09.11.2021", "12.11.2021", "15.11.2021-21.11.2021"]
some_date = "22.11.2021-25.11.2021"
print(is_available_date(dates, some_date))
dates = ["01.11.2021", "05.11.2021-09.11.2021", "12.11.2021", "15.11.2021-21.11.2021"]
some_date = "01.11.2021-04.11.2021"
print(is_available_date(dates, some_date))

dates = ["01.11.2021", "05.11.2021-09.11.2021", "12.11.2021", "15.11.2021-21.11.2021"]
some_date = "02.11.2021-05.11.2021"
print(is_available_date(dates, some_date))

dates = ["01.11.2021", "05.11.2021-09.11.2021", "12.11.2021", "15.11.2021-21.11.2021"]
some_date = "10.11.2021-14.11.2021"
print(is_available_date(dates, some_date))

dates = ["01.11.2021", "05.11.2021-09.11.2021", "12.11.2021", "15.11.2021-21.11.2021"]
some_date = "03.11.2021-05.11.2021"
print(is_available_date(dates, some_date))

dates = ["01.11.2021", "05.11.2021-09.11.2021", "12.11.2021", "15.11.2021-21.11.2021"]
some_date = "09.11.2021-10.11.2021"
print(is_available_date(dates, some_date))

dates = ["01.11.2021", "05.11.2021-09.11.2021", "12.11.2021", "15.11.2021-21.11.2021"]
some_date = "06.11.2021-08.11.2021"
print(is_available_date(dates, some_date))

dates = ["01.11.2021", "05.11.2021-09.11.2021", "12.11.2021", "15.11.2021-21.11.2021"]
some_date = "14.11.2021-22.11.2021"
print(is_available_date(dates, some_date))

dates = ["14.09.2022-14.10.2022"]
some_date = "20.09.2022"
print(is_available_date(dates, some_date))

dates = ["14.09.2022-14.10.2022"]
some_date = "14.11.2022"
print(is_available_date(dates, some_date))

dates = ["14.09.2022-14.10.2022"]
some_date = "15.11.2022-16.11.2022"
print(is_available_date(dates, some_date))

dates = ["14.09.2022-14.10.2022"]
some_date = "14.09.2022-22.09.2022"
print(is_available_date(dates, some_date))
dates = ["02.11.2021", "05.11.2021-09.11.2021"]
some_date = "04.11.2021"
print(is_available_date(dates, some_date))
