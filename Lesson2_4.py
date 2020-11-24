couple_words = input("Введите несколько слов, разделенных пробелами: ")  # пользователь вводит строку из неск слов
split_words = couple_words.split(' ')  # создаем лист с разъединенными словами
for i, word in enumerate(split_words):  # нумеруем и выводим на отдельной строке наши слова
    print(i + 1, word)
