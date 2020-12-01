"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.

"""

f = open("5_2_strings", "r", encoding="utf-8")
count = 0
for line in f:
    count += 1
    print(f"Количество строк - {count}")
f.seek(0)
for words in f:
    word = len(words.split())
    print(f"Количество слов  - {word}")
