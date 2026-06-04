"""
Реализуйте функцию convert() , которая принимает один аргумент:
string — произвольная строка
Функция должна возвращать строку string :
полностью в нижнем регистре, если букв в нижнем регистре в этой строке больше
полностью в верхнем регистре, если букв в верхнем регистре в этой строке больше
полностью в нижнем регистре, если количество букв в верхнем и нижнем регистрах в этой
строке совпадает
Примечание 1. Символы строки, не являющиеся буквами, следует игнорировать.
"""


def convert(string: str) -> str:
    upper_chars, lower_chars = 0, 0
    for char in string:
        if char.islower():
            lower_chars += 1
        elif char.isupper():
            upper_chars += 1
    return string.upper() if upper_chars > lower_chars else string.lower()


print(convert("BEEgeek"))
print(convert("pyTHON"))
print(convert("pi31415!"))
print(convert("ABCDEF"))
print(convert("abcdef"))
print(convert("12345!?"))
print(convert("PI31415!"))
print(convert("ABCdef"))
print(convert("ABCdef123"))
print(convert("AbCdEf12345"))
print(convert("dEfAbC"))
