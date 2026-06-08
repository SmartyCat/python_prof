"""Вам доступен текстовый файл files.txt , содержащий информацию о файлах. Каждая строка
файла содержит три значения, разделенные символом пробела — имя файла, его размер (целое
число) и единицы измерения:
cant-help-myself.mp3 7 MB
keep-yourself-alive.mp3 6 MB
bones.mp3 5 MB
...
Напишите программу, которая группирует данные файлы по расширению, определяя общий
объем файлов каждой группы, и выводит полученные группы файлов, указывая для каждой ее
общий объем. Группы должны быть расположены в лексикографическом порядке названий
расширений, файлы в группах — в лексикографическом порядке их имен.
Примечание 1. Например, если бы файл files.txt имел вид:
input.txt 3000 B
scratch.zip 300 MB
output.txt 1 KB
temp.txt 4 KB
boy.bmp 2000 KB
mario.bmp 1 MB
data.zip 900 MB
то программа должна была бы вывести:
boy.bmp
mario.bmp
----------
Summary: 3 MB
input.txt
output.txt
temp.txt
----------
Summary: 8 KB
data.zip
scratch.zip
----------
Summary: 1 GB
где Summary — общий объем файлов группы.
Примечание 2. Гарантируется, что все имена файлов содержат расширение.
Примечание 3. Общий объем файлов группы записывается в самых крупных (максимально
возможных) единицах измерения с округлением до целых. Другими словами, сначала следует
определить суммарный объем всех файлов группы, скажем, в байтах, а затем перевестиполученное значение в самые крупные (максимально возможные) единицы измерения.
Примеры перевода:
1023 B -> 1023 B
1300 B -> 1 KB
1900 B -> 2 KB
Примечание 4. Значения единиц измерения такие же, какие приняты в информатике:
1 KB = 1024 B
1 MB = 1024 KB
1 GB = 1024 MB
Примечание 5. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
Примечание 6. При открытии файла используйте явное указание кодировки UTF-8."""


def change(sum_size: int) -> str:  # вспомогательная функция для преобразования числа
    if sum_size // 1073741824 != 0:
        sum_size = str(round(sum_size / 1073741824)) + " GB"
    elif sum_size // 1048576 != 0:
        sum_size = str(round(sum_size / 1048576)) + " MB"
    elif sum_size // 1024 != 0:
        sum_size = str(round(sum_size / 1024)) + " KB"
    else:
        sum_size = str(sum_size) + " B"
    return sum_size


with open("/home/kostya/Загрузки/files.txt", mode="r", encoding="utf-8") as file:
    files = file.readlines()
    names = {}
    for file in files:
        name, size, unit = file.rstrip().split()  # распаковка плюс обрезание переносов
        size = int(size)
        extend = name[name.index(".") :]  # вычленяю разширение
        if unit == "KB":  # все преобразовую в байты
            size = size * 1024
        elif unit == "MB":
            size = size * 1048576
        elif unit == "GB":
            size = size * 1073741824

        names.setdefault(extend, {})[
            name
        ] = size  # добавляю разширение с их файлами и размерами
    names = dict(sorted(names.items()))  #  сортировка по разширению
    for name in names:
        sum_size = sum(names[name].values())  # суммирую
        sum_size = change(sum_size)  # преобразовую
        print(*sorted(names[name].keys()), sep="\n")  # сортирую и вывожу имена файлов
        print("----------")
        print(f"Summary: {sum_size}")  # вывожу сумму
        print()
