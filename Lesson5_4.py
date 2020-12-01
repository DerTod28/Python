"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и
считывающую построчно данные. При этом английские числительные
должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

"""

translated_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('5_4_translation', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.split(" ", 1)
        new_file.append(translated_dict[line[0]] + ' ' + line[1])
        #new_dict = {line.split()[0]: line.split()[2]}
    print(new_file)

with open('5_4_translation', 'w', encoding='utf-8') as file_2:
    file_2.writelines(new_file)
