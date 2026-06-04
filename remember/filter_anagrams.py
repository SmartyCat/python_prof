"""
Анаграммы — это слова, которые состоят из одинаковых букв. Например:
адаптер — петарда
адресочек — середочка
азбука — базука
аистенок — осетинка
Реализуйте функцию filter_anagrams() , которая принимает два аргумента в следующем
порядке:
word — слово в нижнем регистре
words — список слов в нижнем регистре
Функция должна возвращать список, элементами которого являются слова из списка words ,
которые представляют анаграмму слова word . Если список words пуст или не содержит
анаграмм, функция должна вернуть пустой список.
Примечание 1. Слова в возвращаемом функцией списке должны располагаться в своем
исходном порядке.
Примечание 2. Считайте, что слово является анаграммой самого себя.
"""


def filter_anagrams(word: str, words: list[str]) -> list:
    if not words:
        return []
    word_chars = {i: word.count(i) for i in word}
    return [word for word in words if {i: word.count(i) for i in word} == word_chars]


word = "abba"
anagrams = ["aabb", "abcd", "bbaa", "dada"]
print(filter_anagrams(word, anagrams))


print(filter_anagrams("отсечка", ["сеточка", "стоечка", "тесачок", "чесотка"]))

print(
    filter_anagrams(
        "tommarvoloriddle",
        ["iamlordvoldemort", "iamdevolremort", "mortmortmortmort", "remortvolremort"],
    )
)
print(filter_anagrams("стекло", []))

print(filter_anagrams("крона", ["кротко", "укроп", "норка"]))

print(filter_anagrams("чулки", ["лучик", "чутко", "кочка"]))

print(filter_anagrams("клоун", ["колдун", "кулон", "уклон", "кол"]))

word = "abba"
anagrams = ["aaab", "dbcd", "bdaa", "badb"]
print(filter_anagrams(word, anagrams))
